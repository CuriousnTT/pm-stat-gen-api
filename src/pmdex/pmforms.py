from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from pmalchemy.alchemy import Base, session, commit_and_close, get_or_create()
from pmdex.pmdex import PmDex

class PmForm(Base):
    __tablename__ = 'forms'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nat_dex_nr: Mapped[int] = mapped_column(Integer, ForeignKey('pmdex.nat_dex_nr'))
    form_name: Mapped[str] = mapped_column(String(20))
    pokemon: Mapped[PmDex] = relationship('PmDex', foreign_keys=[nat_dex_nr] backref='forms')
