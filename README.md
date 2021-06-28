# Semantically-enabled Browsing of Large Multilingual Document Collections

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
[![GitHub Issues](https://img.shields.io/github/issues/cbadenes/phd-thesis.svg)](https://github.com/cbadenes/phd-thesis/issues)
[![License](https://img.shields.io/badge/license-GPL3.0-blue.svg)](https://opensource.org/licenses/GPL-3.0)
[![DOI](https://img.shields.io/badge/doi-xxx-yellow.svg)](https://zenodo.org/badge/latestdoi/xxxx)


The PhD Thesis and slides are publicly available: 
* [PDF](https://github.com/cbadenes/phd-thesis/blob/master/Thesis.pdf)
* [slides](https://www.slideshare.net/CarlosBadenes/semanticallyenabled-browsing-of-large-multilingual-document-collections)

**Author**:  
  * [Carlos Badenes-Olmedo](https://scholar.google.com/citations?user=7U87QYEAAAAJ&hl=es)  
  
**Supervisors**:  
  * Dr. [Oscar Corcho García](https://scholar.google.com/citations?user=TzubuoF0OCwC&hl=es)  
  * Dr. [Jose Luís Redondo García](https://scholar.google.com/citations?user=YY37C-4AAAAJ&hl=es)

**Committee**:
 * Dr. [Horacio Saggion](https://scholar.google.com/citations?user=WMrCFCIAAAAJ&hl=en)
 * Dr. [Raphaël Troncy](https://scholar.google.com/citations?hl=en&user=1BxhcigAAAAJ)
 * Dr. [Jeronimo Arenas-Garcia](https://scholar.google.com/citations?hl=en&user=40AV6F0AAAAJ)
 * Dr. [Jose Manuel Gomez-Perez](https://scholar.google.com/citations?hl=en&user=P3B2MmwAAAAJ)
 * Dr. [Victor Rodriguez-Doncel](https://scholar.google.com/citations?hl=en&user=czpMk10AAAAJ)

**Abstract**:   
Searching for similar documents and exploring the major themes are common activities when browsing document collections. With the ongoing growth in the number of digital documents in multiple languages, we need better tools to browse large multilingual corpora. Manual document annotation has been traditionally used to facilitate such document browsing. However, manual annotation is knowledge-intensive and tedious task and can be alleviated by using automatic document annotation algorithms. Most  algorithms represent documents in a common feature space that abstracts them away from the specific sequence of words used in them. Probabilistic Topic Models reduce that feature space by annotating documents with thematic information. Over this low-dimensional latent space some algorithms have been proposed to perform document similarity search, including collections of texts in multiple languages. However, dictionaries or comparable corpora are required to create multilingual topics and thematic information is usually hidden behind specific representations that limits the explanatory capability of topics to justify content-based similarities. In this thesis we address the challenge of automatically relating documents from large multilingual corpora based on the knowledge offered by the topics covered in the collection, and without the need for theme-aligned data. In order to do so, we have created a framework where probabilistic topic models can be created and reused, a hierarchical model for describing documents with thematic annotations and an unsupervised algorithm that relates multilingual documents from their most relevant themes. Evaluations on classifying and sorting documents by similar content reveal good results on multiple domains.
