# from dotenv import load_dotenv
# from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import relationship

# load_dotenv()

# Base = declarative_base()

# """
# For Reference
# https://docs.sqlalchemy.org/en/14/orm/basic_relationships.html
# https://alembic.sqlalchemy.org/en/latest/tutorial.html
# https://pneuma.hashnode.dev/building-a-blog-with-fastapi-mysql-sqlalchemy-and-alembic#heading-database-crud-utility-functions
# """

# class Category(Base):
#     __tablename__ = "categories"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String(255))
#     icon = Column(String(255))

#     blockchain_categories = relationship(
#         "BlockchainCategories", back_populates="categories", cascade="all,delete"
#     )

#     def __repr__(self):
#         return f"{self.name}"


# class Blockchain(Base):
#     __tablename__ = "blockchain"
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String(50))
#     description = Column(String(50))
#     icon = Column(String(255))
#     status = Column(Boolean, default=False)
#     sustainability_score = Column(Integer)
#     decentralization_score = Column(Integer)
#     available = Column(Boolean, default=False)

#     blockchain_categories = relationship(
#         "BlockchainCategories", back_populates="blockchain", cascade="all,delete"
#     )

#     def __repr__(self):
#         return f"{self.name}"


# class BlockchainCategories(Base):
#     __tablename__ = "blockchain_categories"

#     id = Column(Integer, primary_key=True, index=True)
#     category_id = Column(Integer, ForeignKey("categories.id", ondelete="CASCADE"))
#     blockchain_id = Column(Integer, ForeignKey("blockchain.id", ondelete="CASCADE"))

#     category = relationship("Category", back_populates="blockchain_categories")
#     blockchain = relationship("Blockchain", back_populates="blockchain_categories")
