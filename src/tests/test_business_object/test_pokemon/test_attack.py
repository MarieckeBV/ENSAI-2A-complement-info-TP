from business_object.attack.fixed_damage_attack import FixedDamagedAttack
from business_object.pokemon.attacker_pokemon import AttackerPokemon
from business_object.statistic import Statistic


class TestFixedDamageAttack:
    def test_compute_damage(self):
        #GIVEN
        attack = FixedDamagedAttack(3, 'truc', 'desc')
        pok1 = AttackerPokemon(stat_current=Statistic(attack=100, speed=100))
        pok2 = AttackerPokemon(stat_current=Statistic(attack=100, speed=100))

        #WHEN
        damage = attack.compute_damage(pok1, pok2)

        #THEN
        assert damage==3

if __name__ == "__main__":
    import pytest

    pytest.main([__file__])


