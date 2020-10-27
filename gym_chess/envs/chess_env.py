import gym
from gym import spaces

import chess
import chess.svg

import numpy as np

from io import BytesIO
import cairosvg
from PIL import Image

class MoveSpace:
    def __init__(self, board):
        self.board = board

    def sample(self):
        return np.random.choice(list(self.board.legal_moves))
    
class ChessEnv(gym.Env):
    """Chess Environment"""
    metadata = {'render.modes': ['rgb_array', 'human'], 'observation.modes': ['rgb_array', 'piece_map']}

    def __init__(self, render_size=512, observation_mode='rgb_array', claim_draw=True, **kwargs):
        super(ChessEnv, self).__init__()

        if observation_mode == 'rgb_array':
            self.observation_space = spaces.Box(low = 0, high = 255,
                                                shape = (render_size, render_size, 3),
                                                dtype = np.uint8)
        elif observation_mode == 'piece_map':
            self.observation_space = spaces.Box(low = -6, high = 6,
                                                shape = (8, 8),
                                                dtype = np.uint8)
        else:
            raise Exception("observation_mode must be either rgb_array or piece_map")

        self.observation_mode = observation_mode

        self.chess960 = kwargs['chess960']
        self.board = chess.Board(chess960 = self.chess960)

        if self.chess960:
            self.board.set_chess960_pos(np.random.randint(0, 960))

        self.render_size = render_size
        self.claim_draw = claim_draw

        self.viewer = None

        self.action_space = MoveSpace(self.board)

    def _get_image(self):
        out = BytesIO()
        bytestring = chess.svg.board(self.board, size = self.render_size).encode('utf-8')
        cairosvg.svg2png(bytestring = bytestring, write_to = out)
        image = Image.open(out)
        return np.asarray(image)

    def _get_piece_configuration(self):
        piece_map = np.zeros(64)

        for square, piece in zip(env.board.piece_map().keys(), env.board.piece_map().values()):
            piece_map[square] = piece.piece_type * (piece.color * 2 - 1)

        return piece_map.reshape((8, 8))

    def _observe(self):
        observation = (self._get_image() if self.observation_mode == 'rgb_array' else self._get_piece_configuration())
        return observation

    def _action_to_move(self, action):
        from_square = chess.Square(action[0])
        to_square = chess.Square(action[1])
        promotion = (None if action[2] == 0 else chess.Piece(chess.PieceType(action[2])), chess.Color(action[4]))
        drop = (None if action[3] == 0 else chess.Piece(chess.PieceType(action[3])), chess.Color(action[5]))
        move = chess.Move(from_square, to_square, promotion, drop)
        return move

    def _move_to_action(self, move):
        from_square = move.from_square
        to_square = move.to_square
        promotion = (0 if move.promotion is None else move.promotion)
        drop = (0 if move.drop is None else move.drop)
        return [from_square, to_square, promotion, drop]

    def step(self, action):
        self.board.push(action)

        observation = self._observe()
        result = self.board.result()
        reward = (1 if result == '1-0' else -1 if result == '0-1' else 0)
        terminal = self.board.is_game_over(claim_draw = self.claim_draw)
        info = {'turn': self.board.turn,
                'castling_rights': self.board.castling_rights,
                'fullmove_number': self.board.fullmove_number,
                'halfmove_clock': self.board.halfmove_clock,
                'promoted': self.board.promoted,
                'chess960': self.board.chess960,
                'ep_square': self.board.ep_square}

        return observation, reward, terminal, info

    def reset(self):
        self.board.reset()

        if self.chess960:
            self.board.set_chess960_pos(np.random.randint(0, 960))

        return self._observe()

    def render(self, mode='human'):
        img = self._get_image()
        if mode == 'rgb_array':
            return img
        elif mode == 'human':
            from gym.envs.classic_control import rendering

            if self.viewer is None:
                self.viewer = rendering.SimpleImageViewer()

            self.viewer.imshow(img)
            return self.viewer.isopen

    def close(self):
        if not self.viewer is None:
            self.viewer.close()
