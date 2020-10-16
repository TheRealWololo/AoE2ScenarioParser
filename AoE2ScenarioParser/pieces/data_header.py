from AoE2ScenarioParser.pieces import aoe2_piece
from AoE2ScenarioParser.helper.datatype import DataType
from AoE2ScenarioParser.helper.retriever import Retriever
from AoE2ScenarioParser.pieces.structs.player_data_one import PlayerDataOneStruct


class DataHeaderPiece(aoe2_piece.AoE2Piece):
    def __init__(self, parser_obj=None, data=None):
        retrievers = [
            Retriever("next_unit_id_to_place", DataType("u32")),
            Retriever("version", DataType("f32")),
            Retriever("player_names", DataType("c256", repeat=16)),
            Retriever("string_table_player_names", DataType("u32", repeat=16)),
            Retriever("player_data_1", DataType(PlayerDataOneStruct, repeat=16)),
            Retriever("conquest_mode", DataType("u8")),
            Retriever("mission_items_counter", DataType("u16"), save_as="mic"),
            Retriever("mission_available", DataType("u16")),
            Retriever("mission_timeline", DataType("f32")),
            Retriever("mission_item", DataType("30"), set_repeat="{mic}"),
            Retriever("unknown", DataType("64")),
            Retriever("filename", DataType("str16")),
        ]

        super().__init__("Data Header", retrievers, parser_obj, data=data)

    @staticmethod
    def defaults():
        defaults = {
            'next_unit_id_to_place': 0,
            'version': 1.3600000143051147,
            'player_names': ['\x00' * 256] * 16,
            'string_table_player_names': [4294967294] * 16,
            'player_data_1': DataHeaderPiece.get_player_data_1_default(),
            'conquest_mode': 1_0_0_0_0_0_0_0_0,
            'mission_items_counter': 1_0_0_0_0_0_0_0_0,
            'mission_available': 1_0_0_0_0_0_0_0_0,
            'mission_timeline': 1_0_0_0_0_0_0_0_0,
            'mission_item': 1_0_0_0_0_0_0_0_0,
            'unknown': 1_0_0_0_0_0_0_0_0,
            'filename': 1_0_0_0_0_0_0_0_0,
        }
        return defaults

    @staticmethod
    def get_player_data_1_default():
        # active, human, civilization, cty_mode
        data = [
            [1, 1, 36, 4],
            [1, 0, 36, 4],
        ]
        data += [[0, 0, 36, 4] for _ in range(14)]
        return [PlayerDataOneStruct(data=x) for x in data]
