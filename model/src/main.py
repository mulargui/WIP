import argparse
import sys

if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument('--epochs', type=int, default=10)
    parser.add_argument('--model-dir', type=str, default=os.environ['SM_MODEL_DIR'])
    parser.add_argument('--dataset-dir', type=str, default=os.environ['SM_DATASET_DIR'])
    
    args, _ = parser.parse_known_args()
    
    epochs     = args.epochs
    model_dir  = args.model_dir
    dataset_dir   = args.dataset_dir
    
    #create a data object and prepare it to train the model
    from data import Data
    d = Data(dataset_dir + '/train.csv')
    d.data_engineering()
    if d.validationError:
        print('error in validation')
        sys.exit(-1)
    d.split(0.2)

    #create the model object, train it and save it
    from model import Model
    m = Model()
    m.train(d.x_train, d.y_train, d.x_test, d.y_test, epochs)
    m.save(dataset_dir)
