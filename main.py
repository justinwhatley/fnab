""" Import Modules """

""" Loads data in the new format with new and old processing combined 
#https://blog.keras.io/building-powerful-image-classification-models-using-very-little-data.html

"Building powerful image classification models using very little data"

In our setup, we:
- created a data/ folder
- created train/ and validation/ subfolders inside data/
- created GR2/ and GR3/ subfolders inside train/ and validation/
"""

""" Path to data"""

import preprocessing
import utils

import os

# Machine learning modules
import numpy as np
import keras
import os.path as path
from keras.preprocessing.image import ImageDataGenerator

from keras import optimizers
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras import backend as K

""" Data-augmentation """

class cnn(object):
    def init(self):
        model = Sequential()
        model.add(Conv2D(32, (3, 3), input_shape=input_shape))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))

        model.add(Conv2D(32, (3, 3)))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))

        model.add(Conv2D(64, (3, 3)))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))

        model.add(Flatten())
        model.add(Dense(64))
        model.add(Activation('relu'))
        model.add(Dropout(0.5))
        model.add(Dense(1))
        model.add(Activation('sigmoid'))

        model.compile(loss='binary_crossentropy',
                    optimizer='rmsprop',
                    metrics=['accuracy'])

        model.summary()



from keras.preprocessing.image import ImageDataGenerator

datagen = ImageDataGenerator(
        rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest')


def get_path(computer_str, directory):
    """
    Returns the correct path based on where the program is run
    """

    mac_data_path = '/Users/justinwhatley/Dropbox/FevensLab'
    linux_data_path = '/Users/justinwhatley/Dropbox/FevensLab'
    
    if computer_str.lower() == 'mac':
        return os.path.join(mac_data_path, 'FNAB_raw')

    elif computer_str.lower() == 'linux': 
        return os.path.join(linux_data_path, 'FNAB_raw')

    elif computer_str.lower() == 'colab':
        # Google colab path
        print('Not yet implemented')
        exit(0)

    else: 
        print('Incorrect base path option')
        exit(0)


def train():
    """
    """
    pass

def validate():
    """
    Compute validation score
    """
    pass

def remove_training_validation_files(directory):
    """
    Remove the directory containing the validation and training set files that were assigned for k-fold validation 
    Note. Original files are still available 
    """
    pass



# def k_fold_validation(k):
#     # TODO modify this to append only
#     k = 5
#     l = int(len(X) / k)
#     mse_total, mae_total = 0, 0
#     for i in range(k):
#         test_x = X[i*l:(i+1)*l]
#         test_y = Y[i*l:(i+1)*l]

#         train_x = np.concatenate([X[:i*l], X[(i+1)*l:]])
#         train_y = np.concatenate([Y[:i*l], Y[(i+1)*l:]])

#         model.fit(train_x, train_y, epochs=15)

#         predictions = model.predict(test_x)
#         mse, mae = model.evaluate(test_x, test_y)
#         mse_total += mse
#         mae_total += mae

#     mse_avg = mse_total / k
#     mae_avg = mae_total / k
#     print(mse_avg, mae_avg)

def concat_channels():
    " TODO https://stackoverflow.com/questions/43196636/how-to-concatenate-two-layers-in-keras"
    from keras.models import Sequential, Model
    from keras.layers import Concatenate, Dense, LSTM, Input, concatenate
    from keras.optimizers import Adagrad

    first_input = Input(shape=(2, ))
    first_dense = Dense(1, )(first_input)

    second_input = Input(shape=(2, ))
    second_dense = Dense(1, )(second_input)

    merge_one = concatenate([first_dense, second_dense])

    third_input = Input(shape=(1, ))
    merge_two = concatenate([merge_one, third_input])

    model = Model(inputs=[first_input, second_input, third_input], outputs=merge_two)
    model.compile(optimizer=ada_grad, loss='binary_crossentropy',
                metrics=['accuracy'])



if __name__ == "__main__":

    raw_data_directory_name = 'FNAB_raw'
    raw_data_directory_path = get_path('mac', raw_data_directory_name)
    # raw_data_directory_path = get_path('linux', raw_data_directory_name)

    preprocessed_directory_path = os.path.join(os.path.dirname(raw_data_directory_path), 'FNAB_preprocessed')

    class_keyword_1 = 'MG2'
    class_keyword_2 = 'MG3'
    classes_list = [class_keyword_1, class_keyword_2]

    # Prepares data
    height, width = 224, 224
    file_lists_by_class = preprocessing.prepare_datasets(raw_data_directory_path, preprocessed_directory_path, height, width, classes_list)
    print(file_lists_by_class)
    exit(0)


    preprocessed_path = os.path.join(raw_data_directory_path, 'preprocessed')

    # Creates the training and validation directories if they do not exist
    preprocessing.create_training_and_validation_dir(preprocessed_path, 'MG2', 'MG3')



    # Iterates through folds
    # for _class in file_lists_by_class:
    #     for i, fold in enumerate(_class)
    #         validation_fold = i
    #         # Move the list of selected files to a training and validation folders
    #         preprocessing.assign_folds_to_training_and_validation(validation_fold, _class)
    #         # Run training, validation while keeping average
    #         model = train()
    #         model_score = validate()
            
    #         remove_test_files()
    #         # remove_files
