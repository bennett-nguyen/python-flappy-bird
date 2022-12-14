import pygame as pg
from dataclasses import dataclass

@dataclass(eq=False, unsafe_hash=False)
class __SharedData:
    """
    Defines the data that will be shared across all components

    dt and events are required data for any game;
    """
    dt: float
    events: pg.event

shared_data = __SharedData(None, None)
