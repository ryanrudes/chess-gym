from gym.envs.registration import register

register(
    id='Chess-v0',
    entry_point='chess_gym.envs:ChessEnv',
    kwargs={'chess960': False}
)

register(
    id='Chess960-v0',
    entry_point='chess_gym.envs:ChessEnv',
    kwargs={'chess960': True}
)
