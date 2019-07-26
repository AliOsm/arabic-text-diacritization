# Arabic Text Diacritization

This repository contains the dataset, helpers, and systems comparison for our paper on Arabic Text Diacritization:

"[Arabic Text Diacritization Using Deep Neural Networks](https://arxiv.org/abs/1905.01965)", Ali Fadel, Ibraheem Tuffaha, Bara' Al-Jawarneh, and Mahmoud Al-Ayyoub, [ICCAIS 2019](http://www.iccais.tech).

## Files

### [dataset](/dataset)

- train.txt - Contains 50,000 lines of diacritized Arabic text which can be used as training dataset
- val.txt - Contains 2,500 lines of diacritized Arabic text which can be used as validation dataset
- test.txt - Contains 2,500 lines of diacritized Arabic text which can be used as testing dataset

### [helpers](/helpers)
- constants
  - ARABIC_LETTERS_LIST.pickle - Contains list of Arbaic letters
  - CLASSES_LIST.pickle - Contains list of all possible classes
  - DIACRITICS_LIST.pickle - Contains list of all diacritics
- count_characters.py - Counts the number of Arabic letters and diacritics in a file
- count_fathatan.py - Counts the number of fathatan occurrences before and after Alif in all files from a folder
- diacritization_stat.py - Calculates DER and WER using the gold data and the predicted output
- diacritics_rate_extractor.py - Keeps lines with p% diacritics to Arabic characters rate or more in all files from a folder
- file_lookup.py - Searches for a line in all files from a folder
- fix_fathatan.py - Changes after-Alif fathatan to before-Alit fathatan in a file
- remove_diacritics.py - Removes diacritics from a file
- transliteration.py - Converts a file from Arabic text to Buckwalter transliteration and vice-versa
- pre_process_tashkeela_corpus.ipynb - Pre-process Tashkeela Corpus data

### [existing_systems](/existing_systems)
- ali-soft - Contains some bugs that exist in [Ali-Soft](http://www.ali-soft.com) system
- farasa - Contains [Farasa](http://alt.qcri.org/farasa) system output, fixed output, and DER/WER statistics
- harakat - Contains [Harakat](https://harakat.ae) system testing script, output, fixed output, and DER/WER statistics
- madamira - Contains [MADAMIRA](https://camel.abudhabi.nyu.edu/madamira) system output, fixed output, and DER/WER statistics
- mishkal - Contains [Mishkal](https://tahadz.com/mishkal) system output, fixed output, and DER/WER statistics
- shakkala - Contains [Shakkala](https://ahmadai.com/shakkala) system data splitting script, output, fixed output, and DER/WER statistics
- tashkeela_model - Contains [Tashkeela-Model](https://github.com/Anwarvic/Tashkeela-Model) system output, fixed output, and DER/WER statistics for each n-gram model provided by them

#### Note: All codes in this repository tested on [Ubuntu 18.04](http://releases.ubuntu.com/18.04)

## Contributors
1. [Ali Hamdi Ali Fadel](https://github.com/AliOsm).<br/>
2. [Ibraheem Tuffaha](https://github.com/IbraheemTuffaha).<br/>
3. [Bara' Al-Jawarneh](https://github.com/baraajaw).<br/>
4. [Mahmoud Al-Ayyoub](https://github.com/malayyoub).<br/>

## License
The project is available as open source under the terms of the [MIT License](https://opensource.org/licenses/MIT).
