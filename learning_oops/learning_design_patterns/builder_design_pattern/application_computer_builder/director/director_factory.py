from builders.gaming_computer_builder import GamingComputerBuilder
from director.director import Director, GameBuilderDirector
from builders.computer_builder import ComputerBuilder

class DirectoryFactory:
    @staticmethod
    def get_director(product:str,builder:ComputerBuilder)-> Director:
        if product == 'gaming_pc' and isinstance(builder, GamingComputerBuilder):
            return GameBuilderDirector(builder=builder, product=product)
        else:
            raise NotImplementedError('product must be gaming_pc')