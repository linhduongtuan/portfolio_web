from datetime import datetime
from database.database import init_db, get_session
from database.models import Post, CodeSnippet
from portfolio_web.data.contents import blog_posts  # Update the import path accordingly


def convert_date(date_str: str) -> datetime:
    """Convert date string to datetime object."""
    return datetime.strptime(date_str, "%B %d, %Y")


def seed_blog_posts():
    """Seed the database with existing blog posts."""
    session = next(get_session())

    try:
        for blog_post in blog_posts:
            # Check if the post already exists
            existing_post = (
                session.query(Post).filter(Post.slug == blog_post.id).first()
            )
            if existing_post:
                print(f"Post with slug '{blog_post.id}' already exists. Skipping...")
                continue

            # Create Post
            db_post = Post(
                slug=blog_post.id,  # Using the existing id as slug
                title=blog_post.title,
                date=convert_date(blog_post.date),
                preview=blog_post.preview,
                content=blog_post.content,
                tags=blog_post.tags,
                reading_time=blog_post.reading_time,
            )
            session.add(db_post)
            session.flush()  # Assigns an ID to db_post

            # Create CodeSnippets
            if blog_post.code_blocks:
                for code_block in blog_post.code_blocks:
                    db_code_snippet = CodeSnippet(
                        code=code_block.code,
                        language=code_block.language,
                        post_id=db_post.id,
                    )
                    session.add(db_code_snippet)

        session.commit()
        print("Successfully seeded blog posts!")

    except Exception as e:
        session.rollback()
        print(f"Error seeding blog posts: {e}")
    finally:
        session.close()


if __name__ == "__main__":
    init_db()
    seed_blog_posts()
