from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.pmalchemy.alchemy import Base, session, commit_and_close, get_or_create
from src.pmdex.pmdex import PmDex, get_by_nat_dex_nr

class PmForm(Base):
    __tablename__ = 'form'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nat_dex_nr: Mapped[int] = mapped_column(Integer, ForeignKey('pmdex.nat_dex_nr'), primary_key=True)
    form_name: Mapped[str] = mapped_column(String(20), unique=True)

    pokemon: Mapped[PmDex] = relationship('PmDex', foreign_keys=[nat_dex_nr], backref='forms')

    def __init__(self, pokemon: PmDex, form_name: str):
        self.id = self.id
        self.nat_dex_nr = pokemon.nat_dex_nr
        self.form_name = form_name

    def __repr__(self):
        return self.form_name

### Functions used in table setup


def get_test_insert_dicts():
    rotom = get_by_nat_dex_nr(479)
    gallade = get_by_nat_dex_nr(475)
    skiploom = get_by_nat_dex_nr(188)
    munchlax = get_by_nat_dex_nr(446)
    test_inserts = [
        {
            "pokemon": rotom,
            "form_name": rotom.name,
        }, {
            "pokemon": rotom,
            "form_name": rotom.name + "-Frost",
        }, {
            "pokemon": rotom,
            "form_name": rotom.name + "-Fan",
        }, {
            "pokemon": rotom,
            "form_name": rotom.name + "-Heat",
        }, {
            "pokemon": rotom,
            "form_name": rotom.name + "-Mow",
        }, {
            "pokemon": rotom,
            "form_name": rotom.name + "-Wash",
        }, {
            "pokemon": gallade,
            "form_name": gallade.name,
        }, {
            "pokemon": skiploom,
            "form_name": skiploom.name,
        }, {
            "pokemon": munchlax,
            "form_name": munchlax.name,
        }
    ]
    return test_inserts

def add_form_to_table(dict):
    try:
        pokemon: PmDex = dict["pokemon"]
        form_name = dict["form_name"]
        nat_dex_nr = pokemon.nat_dex_nr
        form = session.query(PmForm).filter_by(nat_dex_nr=nat_dex_nr, form_name=form_name).first()
        if form is None:
            form = PmForm(pokemon, form_name)
            session.add(form)
    except Exception as error:
        print(f"An error occurred when adding form to table: {error}")
        session.rollback()

def four_test_pms():
    dicts = get_test_insert_dicts()
    pokemon = []
    for dict in dicts:
        pm: PmDex = dict["pokemon"]
        add_form_to_table(dict)
        print(dict["form_name"])
        pokemon.append(pm.name)
    commit_and_close()
    pm_set = {pokemon for pokemon in pokemon}
    print(f"test data inserted in pmforms for: {pm_set}")