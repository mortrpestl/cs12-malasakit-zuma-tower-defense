from model.entities.chameleon import Chameleon
from model.entities.enemy import Enemy
from model.entities.regenerator import Regenerator
from model.entities.normaltower import NormalTower
from model.entities.shooter import Shooter

from model.utils import BGColor, Color, SpriteSet

enemy_sprites: dict[tuple[type, Color], SpriteSet] = {
    (Enemy, Color.RED): SpriteSet(0, 8, 0, 48, 48, BGColor.PEACH, 0.833),
    (Enemy, Color.BLUE): SpriteSet(0, 8, 48, 48, 48, BGColor.PEACH, 0.833),
    (Enemy, Color.PURPLE): SpriteSet(0, 8, 96, 48, 48, BGColor.PEACH, 0.833),
    (Enemy, Color.ORANGE): SpriteSet(0, 8, 144, 48, 48, BGColor.PEACH, 0.833),
    (Enemy, Color.GREEN): SpriteSet(0, 8, 192, 48, 48, BGColor.PEACH, 0.833),
    (Enemy, Color.STEEL_BLUE): SpriteSet(0, 72, 0, 48, 48, BGColor.PEACH, 0.833),
    (Chameleon, Color.RED): SpriteSet(0, 136, 105, 48, 32, BGColor.PEACH, 0.833),
    (Chameleon, Color.BLUE): SpriteSet(0, 136, 153, 48, 32, BGColor.PEACH, 0.833),
    (Chameleon, Color.PURPLE): SpriteSet(0, 136, 201, 48, 32, BGColor.PEACH, 0.833),
    (Chameleon, Color.ORANGE): SpriteSet(0, 200, 9, 48, 32, BGColor.PEACH, 0.833),
    (Chameleon, Color.GREEN): SpriteSet(0, 200, 57, 48, 32, BGColor.PEACH, 0.833),
    (Chameleon, Color.STEEL_BLUE): SpriteSet(0, 200, 105, 48, 32, BGColor.PEACH, 0.833),
    (Regenerator, Color.RED): SpriteSet(0, 80, 49, 32, 48, BGColor.PEACH, 0.833),
    (Regenerator, Color.BLUE): SpriteSet(0, 80, 97, 32, 48, BGColor.PEACH, 0.833),
    (Regenerator, Color.PURPLE): SpriteSet(0, 80, 145, 32, 48, BGColor.PEACH, 0.833),
    (Regenerator, Color.ORANGE): SpriteSet(0, 80, 193, 32, 48, BGColor.PEACH, 0.833),
    (Regenerator, Color.GREEN): SpriteSet(0, 144, 1, 32, 48, BGColor.PEACH, 0.833),
    (Regenerator, Color.STEEL_BLUE): SpriteSet(0, 144, 49, 32, 48, BGColor.PEACH, 0.833),
}

tower_sprites: dict[tuple[type, int | None], SpriteSet] = {
    (NormalTower, 1): SpriteSet(1, 0, 64, 64, 64, BGColor.RED, 0.625),
    (NormalTower, 2): SpriteSet(1, 0, 128, 64, 64, BGColor.RED, 0.625),
    (Shooter, None): SpriteSet(1, 0, 0, 64, 64, BGColor.RED, 0.625)
}

menu_sprites: dict[str, SpriteSet] = {
    "misc": SpriteSet(2, 0, 0, 150, 30, BGColor.PEACH, 1),
    "pause": SpriteSet(2, 0, 32, 40, 40, BGColor.BLACK, 1)
}