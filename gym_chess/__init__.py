from gym.envs.registration import register

register(
    id='Chess-v0',
    entry_point='gym_minecraft.envs:ChessEnv',
    kwargs={'mission_file': 'default_world_1.xml'}
)
