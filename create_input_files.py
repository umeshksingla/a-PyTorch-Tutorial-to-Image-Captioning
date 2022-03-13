from utils import create_input_files

if __name__ == '__main__':
    # Create input files (along with word map)
    home = '/datasets/home/94/194/usingla'
    create_input_files(dataset='flickr8k',
                       karpathy_json_path=home+'/projectdata/data/flickr8k/dataset.json',
                       image_folder=home+'/projectdata/data/flickr8k/imgs',
                       captions_per_image=5,
                       min_word_freq=5,
                       output_folder=home+'/projectdata/output/flickr8k',
                       max_len=50)
