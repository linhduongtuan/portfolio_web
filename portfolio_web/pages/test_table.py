import reflex as rx
from reflex_ag_grid import ag_grid
import pandas as pd
from sqlmodel import select


class Country(rx.Model, table=True):
    country: str
    population: int
    continent: str


class AGGridDatabaseState(rx.State):
    countries: list[Country]

    # Insert data from a csv loaded dataframe to the database (Do this on the page load)
    @rx.event
    def insert_dataframe_to_db(self):
        data = pd.read_csv(
            "https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv"
        )
        with rx.session() as session:
            for _, row in data.iterrows():
                db_record = Country(
                    country=row["country"],
                    population=row["pop"],
                    continent=row["continent"],
                )
                session.add(db_record)
            session.commit()

    # Fetch data from the database using a computed variable
    @rx.var
    def data(self) -> list[dict]:
        with rx.session() as session:
            results = session.exec(select(Country)).all()
            self.countries = [result.dict() for result in results]
        return self.countries

    # Update the database when a cell value is changed
    @rx.event
    def cell_value_changed(self, row, col_field, new_value):
        self.countries[row][col_field] = new_value
        with rx.session() as session:
            country = Country(**self.countries[row])
            session.merge(country)
            session.commit()
        yield rx.toast(
            f"Cell value changed, Row: {row}, Column: {col_field}, New Value: {new_value}"
        )


column_defs = [
    ag_grid.column_def(field="country"),
    ag_grid.column_def(
        field="population",
        header_name="Population",
        editable=True,
        cell_editor=ag_grid.editors.number,
    ),
    ag_grid.column_def(
        field="continent",
        editable=True,
        cell_editor=ag_grid.editors.select,
        cell_editor_params={
            "values": [
                "Asia",
                "Europe",
                "Africa",
                "Americas",
                "Oceania",
            ]
        },
    ),
]


def test_table():
    return ag_grid(
        id="ag_grid_basic_editing",
        row_data=AGGridDatabaseState.data,
        column_defs=column_defs,
        on_cell_value_changed=AGGridDatabaseState.cell_value_changed,
        width="100%",
        height="40vh",
    )
