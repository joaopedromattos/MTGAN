
<p align="center">
<img src="example.jpg" style="max-width:900px;"></img>
</p>


# Magic: The Gathering Card Generator

A generator of illustrations of the trade card game Magic: The Gathering based on StyleGANv2 created as final project for Data Mining and Machine Learning Applications.

## Dataset

Our dataset was collected using MTGJson API. We provide in this repository a script to collect data at [magic_card_generator/dataset/collection/card_collector.py](/magic_card_generator/dataset/collection/card_collector.py).

## Training Pipeline

Our StyleGANv2 training pipeline is available at [magic_card_generator/styleganv2/styleganv2.ipynb](magic_card_generator/styleganv2/styleganv2.ipynb). The final version of our model was trained for about 100 hours on the Nvidia P100 available at Google Colab.

## Baseline

We used a DCGAN as a qualitative baseline. Its results, along with the training pipeline, are also available at [magic_card_generator/baseline/dcgan/](magic_card_generator/baseline/dcgan/).

## Authors
- [Giovanni Paolo Meloni](https://github.com/GiovanniMeloni)
- Guilherme Soares Gama
- [Gustavo Sasaki Roncaglia](https://github.com/GustavoSasaki)
- [João Pedro Rodrigues Mattos](https://github.com/joaopedromattos)
- [Miguel Gardini](https://github.com/MiguelGardini)
