from typing import Union

from components.keyboard import DellKeyboardRechargeable, Keyboard
from components.memory import DDR3, RAM
from components.processing_unit import CPU, IntelCPU
from components.storage import SSD, Storage
from director.director import Director
from product.computer import Computer


def _get_builder_director(product: str, **kwargs) -> Union[Director | None]:
    from builders.builder_factory import GamingComputerBuilder
    from director.director_factory import GameBuilderDirector

    if product == "gaming_pc":
        builder = GamingComputerBuilder(manufacturer="dell", model="qwe", os="windows")
        builder_director = GameBuilderDirector(builder=builder, product="gaming_pc")

    else:
        raise KeyError('Product must be  "gaming_pc"')

    return builder_director


def main(product: str, **kwargs) -> Computer:
    director = _get_builder_director(product=product, **kwargs)
    computer = director.build_computer(**kwargs)
    return computer


if __name__ == "__main__":
    # I am a client,
    # I need a gameing computer
    # I need keyboard with recharageable feature and of Dell company
    # I need DDR3 memory
    # I need SSD as storage
    # Also I need Intel chip

    product = "gaming_pc"
    keyboard: Keyboard = DellKeyboardRechargeable(
        model="xxs3", type="qwerty", is_multilingual=True, battery_capacity=10
    )
    memory: RAM = DDR3(
        capacity_in_gb=10,
        manufacturer="DDR3_manufacturer",
        type="very_volaile",
        speed_range=22,
        latency=0.33,
    )

    storage: Storage = SSD(
        read_speed_mb=122.22,
        write_speed_mb=12.1,
        capacity=1024,
        interface="ssd_interface",
    )

    cpu: CPU = IntelCPU(model="pentium 22", core=13, cache_mb=1024)

    product = main(
        product,
        memory=memory,
        storage=storage,
        cpu=cpu,
        keyboard=keyboard,
        graphics_card_memory=1234,
    )

    print(product)

    print(dir(product))
