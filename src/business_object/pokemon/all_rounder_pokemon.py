from business_object.pokemon.abstract_pokemon import AbstractPokemon

class AllRounderPokemon(AbstractPokemon):

    def get_pokemon_attack_coef(self)->float:
        multiplier = 1 + (self.sp_atk_current + self.sp_def_current) / 200
        return multiplier
