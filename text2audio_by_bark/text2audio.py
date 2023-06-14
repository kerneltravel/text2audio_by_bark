from bark import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav
#from IPython.display import Audio


class Text2Audio:
     def __init__(self, bark_backend=None):
          # download and load all models
          preload_models()
     
     def do_convert_text_to_audio(self, text_prompt:str, output_audio_file_path:str):
          audio_array = generate_audio(text_prompt)
          write_wav(output_audio_file_path, SAMPLE_RATE, audio_array)


def test_main():
     text_prompt = """
               Hello, my name is Suno. And, uh — and I like pizza. [laughs] 
               But I also have other interests such as playing tic tac toe.
          """
     text_prompt = """
               你好我是刘老王，住在隔壁镇上，家里有100辆摩托车，因为我是卖摩托车的。欢迎来考察买车哦。
          """
     
     # generate audio from text
     t2a = Text2Audio()
     t2a.do_convert_text_to_audio(text_prompt, 'test.wav')
     
if __name__ == '__main__':
     test_main()