from business_object.attack.abstract_attack import AbstractAttack

class FixedDamagedAttack(AbstractAttack):
    def compute_damage(self, APkm, DPkm)->int:
        return self.power
    
    
