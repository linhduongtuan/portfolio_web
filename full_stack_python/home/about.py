import reflex as rx

# from sqlmodel import col
from ..ui.base import base_page
from ..components.styles import Size, MAX_WIDTH, Color, TextColor, Font
from ..navigation import routes as Links


@rx.page(route="/about")
def about_page() -> rx.Component:
    # return
    my_child = rx.box(
        rx.box(
            rx.vstack(
                # Header Section
                rx.hstack(
                    rx.heading(
                        "ABOUT ME?",
                        style={"font_family": Font.TITLES.value},  # type: ignore
                        font_size=Size.BIG.value,
                        color=TextColor.PRIMARY.value,
                    ),
                    rx.spacer(),
                    rx.link(
                        rx.button(
                            "Tell me more...",
                            rx.icon("book-open"),
                        ),
                        color=TextColor.SECONDARY.value,
                        href=Links.GOOGLE_SCHOLAR_URL,
                        is_external=True,
                    ),
                    padding_right=Size.BIG.value,
                    width="100%",
                ),
                # Introduction Text
                rx.text(
                    "I am Linh Duong, a Ph.D. in Biotechnology currently working as a postdoctoral researcher at KTH Royal Institute of Technology, Sweden. My research journey focuses on bridging molecular biology with computational approaches to understand complex biological systems. With extensive experience in both wet-lab techniques and computational methods, I am passionate about decoding the molecular mechanisms of bacterial pathogenesis and host-pathogen interactions, particularly in the context of infectious diseases.",
                    color=TextColor.SECONDARY.value,
                    padding_left=Size.MEDIUM.value,
                    style={"list_style_type": "disc"},  # type: ignore
                    font_size=Size.ABIT_BIG.value,
                ),
                # Subheading: Research Interests
                rx.heading(
                    "Research Interests:",
                    font_size=Size.LIGHT_BIG.value,
                    color=TextColor.PRIMARY.value,
                    padding_top=Size.SMALL.value,
                ),
                # Bullet List of Research Interests
                rx.unordered_list(
                    rx.list_item(
                        rx.text.strong("Bacterial Pathogenesis: "),
                        "Investigating virulence factors and their regulation in pathogenic bacteria, with a focus on antibiotic resistance mechanisms and bacterial adaptation strategies",
                    ),
                    rx.list_item(
                        rx.text.strong("Cellular Biology: "),
                        "Studying host cell responses during infection, including membrane trafficking, signal transduction, and cellular stress responses",
                    ),
                    rx.list_item(
                        rx.text.strong("Molecular Interactions: "),
                        "Exploring the complex interplay between bacterial proteins and host cell receptors, using both experimental and computational approaches",
                    ),
                    rx.list_item(
                        rx.text.strong("Microbiome Research: "),
                        "Investigating how microbial communities influence human health and disease, with particular interest in gut-brain axis and immune system modulation",
                    ),
                    color=TextColor.SECONDARY.value,
                    padding_left=Size.MEDIUM.value,
                    style={"list_style_type": "disc"},  # type: ignore
                    font_size=Size.ABIT_BIG.value,
                ),
                # Subheading: Computational Biology Leveraging
                rx.heading(
                    "Computational Biology Expertise:",
                    font_size=Size.LIGHT_BIG.value,
                    color=TextColor.PRIMARY.value,
                    padding_top=Size.SMALL.value,
                ),
                # Bullet List of Computational Biology Applications
                rx.unordered_list(
                    rx.list_item(
                        rx.text.strong("Genomic Analysis: "),
                        "Implementing next-generation sequencing data analysis pipelines for bacterial genome assembly and annotation",
                    ),
                    rx.list_item(
                        rx.text.strong("Machine Learning Applications: "),
                        "Developing predictive models for protein-protein interactions and drug-target bindings",
                    ),
                    rx.list_item(
                        rx.text.strong("Systems Biology: "),
                        "Creating mathematical models to understand disease progression and treatment responses",
                    ),
                    rx.list_item(
                        rx.text.strong("Bioinformatics Tools: "),
                        "Building custom tools for analyzing high-throughput biological data and medical imaging",
                    ),
                    color=TextColor.SECONDARY.value,
                    padding_left=Size.MEDIUM.value,
                    style={"list_style_type": "disc"},  # type: ignore
                    font_size=Size.ABIT_BIG.value,
                ),
                rx.heading(
                    "Data Science & Analysis:",
                    font_size=Size.LIGHT_BIG.value,
                    color=TextColor.PRIMARY.value,
                    padding_top=Size.SMALL.value,
                ),
                # Bullet List of Computational Biology Applications
                rx.unordered_list(
                    rx.list_item(
                        rx.text.strong("Epidemiological Studies: "),
                        "Analyzing large-scale health datasets to identify disease patterns and risk factors",
                    ),
                    rx.list_item(
                        rx.text.strong("Predictive Modeling: "),
                        "Developing time-series models for disease outbreak prediction and progression",
                    ),
                    rx.list_item(
                        rx.text.strong("Deep Learning: "),
                        "Implementing neural networks for biomedical image analysis and classification",
                    ),
                    rx.list_item(
                        rx.text.strong("Statistical Analysis: "),
                        "Applying advanced statistical methods to interpret complex biological experiments",
                    ),
                    color=TextColor.SECONDARY.value,
                    padding_left=Size.MEDIUM.value,
                    style={"list_style_type": "disc"},  # type: ignore
                    font_size=Size.ABIT_BIG.value,
                ),
                rx.heading(
                    "Current Research Focus:",
                    font_size=Size.LIGHT_BIG.value,
                    color=TextColor.PRIMARY.value,
                    padding_top=Size.SMALL.value,
                ),
                rx.text(
                    "I am currently working on integrating multi-omics data with machine learning approaches to better understand host-pathogen interactions. This involves developing novel computational methods to analyze large-scale biological datasets while validating findings through targeted experimental approaches.",
                    color=TextColor.SECONDARY.value,
                    padding_left=Size.MEDIUM.value,
                    style={"list_style_type": "disc"},  # type: ignore
                    font_size=Size.ABIT_BIG.value,
                ),
            ),
            bg=Color.SECONDARY.value,
            padding=Size.BIG.value,
            border_radius="25px",
            style=MAX_WIDTH,  # type: ignore
            margin_top="5em",  # Space from nav bar
            margin_bottom="5em",  # Space from nav bar
            margin_x="auto",  # Center horizontally
            id="my-child",
        ),
        rx.box(
            rx.vstack(
                # Header Section
                rx.hstack(
                    rx.heading(
                        "My Education",
                        style={"font_family": Font.TITLES.value},  # type: ignore
                        font_size=Size.BIG.value,
                        color=TextColor.PRIMARY.value,
                    ),
                    rx.spacer(),
                    # rx.link(
                    #     rx.button(
                    #         "Tell me more...",
                    #         rx.icon("book-open"),
                    #     ),
                    #     color=TextColor.SECONDARY.value,
                    #     href=Links.GOOGLE_SCHOLAR_URL,
                    #     is_external=True,
                    # ),
                    padding_right=Size.BIG.value,
                    width="100%",
                ),
                # Introduction Text
                rx.text(
                    "In 2014, I obtained Ph.D in Medical Microbiology from the University of Greifswald, Germany, where I focused on understanding the molecular mechanisms of bacterial pathogenesis and host-pathogen interactions. My research journey has been a blend of wet-lab experiments and computational analyses, allowing me to develop a unique skill set that bridges molecular biology with bioinformatics. I have also been involved in teaching and supervising students at both undergraduate and graduate levels, which has further enriched my academic experience.",
                    color=TextColor.SECONDARY.value,
                    padding_left=Size.MEDIUM.value,
                    style={"list_style_type": "disc"},  # type: ignore
                    font_size=Size.ABIT_BIG.value,
                ),
                rx.unordered_list(
                    rx.list_item(
                        rx.text.strong(
                            "My Ph.D. title: ", color=TextColor.PRIMARY.value
                        ),
                        rx.link(
                            "Characterization of putative virulence-associated genes of",
                            rx.text.em(" Burkholderia pseudomallei"),
                            href=Links.PHD_THESIS_URL,
                            is_external=True,
                            color=TextColor.PRIMARY.value,
                        ),
                        font_size=Size.ABIT_BIG.value,
                    ),
                    rx.unordered_list(
                        rx.list_item(
                            rx.text.strong("Abstract: "),
                            "The Gram-negative rod Burkholderia pseudomallei (Bp) is the causative agent of the disease melioidosis, an often fatal infection of humans and animals. The bacteria can be isolated from soil and water in tropical and sub-tropical areas around the world. Moreover, Bp is a facultative intracellular bacterium that can survive in phagocytic cells. Bp possesses a wide array of virulence genes including numerous secretion systems such as three type 3 secretion system clusters (T3SS) and six type VI secretion clusters (T6SS). Furthermore, the genome of Bp consists of 88 paralogous LysR-type transcriptional regulator (LTTR) genes including BPSL0117 gene that may regulate other virulence factors. In the first part of this study, we characterised a role of the putative LTTR BPSL0117 of Bp for the virulence of this pathogen. For this purpose, a Bp ΔBPSL0117 transposon mutant that was already available was successfully complemented by using pUC18T-mini-Tn7T-FRT-Zeo vector. The Bp ΔBPSL0117 transposon mutant exhibited impaired biofilm formation, motility, exoproteases activity, and intracellular growth. Bp ΔBPSL0117 also showed more sensitivity to beta-lactamse antibiotics. Besides in vitro phenotypes, Bp ΔBPSL0117 presented reduced bacterial load in organs and highly attenuated virulence in the BALB/c mouse model of melioidosis. All observed phenotypes were reverted to wild type level in the complemented mutant strain. Next, a protein expression profile analysis should help to examine BPSL0117 dependent protein expression. Using stable isotope labeling by amino acids in cell culture (SILAC), we were able to detect 1608 cytoplasmic proteins. Beside others, we found that BPSL0117 regulates the expression of T3SS3 and T6SS1 associated proteins and enzymes involved in metabolic pathways. In silico analysis, predicted BPSL0117 structure showed high similarity with full-length crystal structures of LTTR proteins like CbnR and CrgA. Collectively, BPSL0117 works as both a positive and a negative regulator. Finally, due to the high attenuation in mice of the Bp ΔBPSL0117 transposon mutant, we examined whether this strain might serve as a promising live vaccine candidate. BALB/c mice were intranasally immunized with a high dose of Bp ΔBPSL0117 and then challenged with Bp E8 wild type via either the intranasal, intraperitoneal or intravenous route. Vaccinated mice showed increased titers of specific IgG anti-Bp antibodies and a delayed time to death compared to unvaccinated mice. Thus, Bp ΔBPSL0117 could partially protect mice against melioidosis but was less protective efficiency compared to other experimental vaccine strategies against Bp. In the second part of this study, the focus was to unravel function for the genes bapA, bapB and bapC, which are encoded within the T3SS cluster 3 of Bp and have rarely been addressed in other studies so far. In a first set of experiments, it was shown that the expression levels of bapB and bapC genes increased when Bp was cultivated in vitro under high salt concentrations. While the expression levels of all bap genes increased when Bp was cultured in vitro under low pH. To further evaluate the role of the bapA gene, an in-frame deletion mutant was constructed. The Bp ΔbapA#1 mutant strain derived from Bp K96243, wild type exhibited increased biofilm formation compared to wild type bacteria. Interestingly, this mutant was also able to replicate more efficiently inside macrophages and showed increased virulence in BALB/c mice. However, these phenotypes were not observed in the independently derived mutants Bp ΔbapA#2 from parental Bp K96243 and Bp ΔbapA#3  parental Bp 1026b since it was not possible to successfully complement the Bp ΔbapA#1 mutant strain. Thus, the bap genes seem to play a role for the adaptations to environmental stress, but at least the bapA gene is not directly involved in the pathogenic potential of Bp inexperimental murine infection.",
                            color=TextColor.PRIMARY.value,
                        ),
                    ),
                    # bg=Color.SECONDARY.value,
                    # padding=Size.BIG.value,
                    # border_radius="25px",
                    # style=MAX_WIDTH,
                    # margin_top="1em",  # Space from nav bar
                    # margin_bottom="1em",  # Space from nav bar
                    # margin_x="auto",  # Center horizontally
                ),
                rx.text(
                    "In 2009, I graduated Master of Science in Microbiology at Hanoi University of Science, Vietnam.",
                    color=TextColor.SECONDARY.value,
                    padding_left=Size.MEDIUM.value,
                    style={"list_style_type": "disc"},  # type: ignore
                    font_size=Size.ABIT_BIG.value,
                ),
                rx.text(
                    "In 2004, I graduated Bachelor of Science in Biology at Hanoi University of Science, Vietnam.",
                    color=TextColor.SECONDARY.value,
                    padding_left=Size.MEDIUM.value,
                    style={"list_style_type": "disc"},  # type: ignore
                    font_size=Size.ABIT_BIG.value,
                ),
            ),
            bg=Color.SECONDARY.value,
            padding=Size.BIG.value,
            border_radius="25px",
            style=MAX_WIDTH,  # type: ignore
            margin_top="2em",  # Space from nav bar
            margin_bottom="5em",  # Space from nav bar
            margin_x="auto",  # Center horizontally
            id="my-child",
        ),
    )
    return base_page(my_child)
