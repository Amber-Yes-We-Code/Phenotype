### Install Required Packages
To set up the required dependencies, please ensure your environment is properly configured by
```python
conda env create -f environment.yml
```

###  Running Experiments
Choose the appropriate experiment based on your data type:
✅ If you have images and corresponding ground truth latent variables, refer to the MNIST experiment:
```python
python run_mnist.py --ground_truth
```

✅ If your dataset consists of multiple modalities without ground truth latent variables, refer to the Phenotype experiment. The provided dataset is just an example, and you are free to use your own dataset and modify your preferred encoder/decoder.
```python
python run_phenotype.py
```