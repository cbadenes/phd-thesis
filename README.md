# Semantically-enabled Browsing of Large Multilingual Document Collections

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
[![GitHub Issues](https://img.shields.io/github/issues/cbadenes/phd-thesis.svg)](https://github.com/cbadenes/phd-thesis/issues)
[![License](https://img.shields.io/badge/license-GPL3.0-blue.svg)](https://opensource.org/licenses/GPL-3.0)
[![DOI](https://img.shields.io/badge/DOI-10.20868/UPM.thesis.67594-yellow.svg)](https://doi.org/10.20868/UPM.thesis.67594)
[![SLIDES](https://img.shields.io/badge/slides-pdf-orange.svg)](https://www.slideshare.net/CarlosBadenes/semanticallyenabled-browsing-of-large-multilingual-document-collections)

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

**Contributions**:    
The following publications support the research work presented in this thesis:   
* **Carlos Badenes-Olmedo**, José Luis Redondo-Garcia, and Oscar Corcho. [Distributing Text Mining tasks with librAIry](http://cbadenes.github.io/papers/2017-librairy.pdf). Proceedings of the 17th ACM Symposium on Document Engineering (DocEng). Valletta, Malta. 2017.    
    [![DOI](https://img.shields.io/badge/DOI-10.1145/3103010.3121040-yellow.svg)](https://doi.org/10.1145/3103010.3121040) 
    [![SLIDES](https://img.shields.io/badge/slides-pdf-orange.svg)](https://www.slideshare.net/CarlosBadenes/distributing-text-mining-tasks-with-librairy)
* Victoria Kosa, Alyona Chugunenko, Eugene Yuschenko, **Carlos Badenes-Olmedo**, Vadim Ermolayev, and Aliaksandr Birukou. [Semantic saturation in retrospective text document collections](http://ceur-ws.org/Vol-1851/paper-1.pdf). Information and Communication Technologies in Education, Research, and Industrial Applications (ICTERI) PhD Symposium, vol. 1851, pages 1-8. CEUR-WS. 2017    
    [![PROCEEDINGS](https://img.shields.io/badge/Proceedings-ICTERI-purple.svg)](http://icteri.org/icteri-2017/phd-symposium/)
* Victoria Kosa, David Chaves-Fraga, Dmitriy Naumenko, Eugene Yuschenko, **Carlos Badenes-Olmedo**, Vadim Ermolayev, Aliaksandr Birukou, Nick Bassiliades, Hans-Georg Fill, Vitaliy Yakovyna, Heinrich C. Mayr, Mykola Nikitchenko, Grygoriy Zholtkevych, and Aleksander Spivakovsky. [Cross-Evaluation of Automated Term Extraction Tools by Measuring Terminological Saturation](http://ermolayev.com/TS-RTDS-TR-2017-1.pdf). Information and Communication Technologies in Education, Research, and Industrial Applications, pages 135-163. Springer International Publishing. 2018  
    [![DOI](https://img.shields.io/badge/DOI-10.1007/978_3_319_76168_8_7-yellow.svg)](https://link.springer.com/chapter/10.1007/978-3-319-76168-8_7)    
* **Carlos Badenes-Olmedo**, José Luis Redondo-García, and Oscar Corcho. [Efficient Clustering from Distributions over Topics](http://cbadenes.github.io/papers/2017-efficient-clustering-distributions.pdf). Proceedings of the 9th International Conference on Knowledge Capture (K-CAP), Article 17, 1–8. Association for Computing Machinery, Austin, TX, USA. 2017.    
    [![DOI](https://img.shields.io/badge/DOI-10.1145/3148011.3148019-yellow.svg)](https://doi.org/10.1145/3148011.3148019)
    [![SLIDES](https://img.shields.io/badge/slides-pdf-orange.svg)](https://www.slideshare.net/CarlosBadenes/efficient-clustering-from-distributions-over-topics-84159286)
* **Carlos Badenes-Olmedo**, José Luis Redondo-Garcia, and Oscar Corcho. [An initial Analysis of Topic-based Similarity among Scientific Documents based on their Rhetorical Discourse Parts](http://cbadenes.github.io/papers/2017-initial-analysis-topic.pdf). Proceedings of the 1st Workshop on Enabling Open Semantic Science (SemSci) co-located with 16th International Semantic Web Conference (ISWC 2017), 15-22. Vienna, Austria. 2017.    
    [![PROCEEDINGS](https://img.shields.io/badge/Proceedings-SemSci-purple.svg)](http://ceur-ws.org/Vol-1931/)
    [![SLIDES](https://img.shields.io/badge/slides-pdf-orange.svg)](https://www.slideshare.net/ocorcho/an-initial-analysis-of-topicbased-similarity-among-scientific-documents-based-on-their-rhetorical-discourse-parts)    
* **Carlos Badenes-Olmedo**, José Luis Redondo-García, and Oscar Corcho. [Large-scale Semantic Exploration of Scientific Literature Using Topic-based Hashing Algorithms](https://content.iospress.com/download/semantic-web/sw200373?id=semantic-web%2Fsw200373). Semantic Web journal, vol. 11, no. 5, pp. 735-750. 2020.   
    [![DOI](https://img.shields.io/badge/DOI-10.3233/SW_200373-yellow.svg)](https://content.iospress.com/articles/semantic-web/sw200373)
* **Carlos Badenes-Olmedo**, Borja Lozano and Oscar Corcho. [Impact of Text Length for Information Retrieval Tasks based on Probabilistic Topics](http://cbadenes.github.io/papers/2021-Impact-of-vocabulary.pdf). Spanish Society for Natural Language Processing journal (SEPLN). 2021    
    [![DOI](https://img.shields.io/badge/DOI-pending-yellow.svg)](http://www.hitz.eus/sepln2021/)
* **Carlos Badenes-Olmedo**, José Luis Redondo-García, and Oscar Corcho. [Scalable Cross-lingual Document Similarity through Language-specific Concept Hierarchies](http://cbadenes.github.io/papers/2019-cross-lingual-similarity.pdf). Proceedings of the 10th International Conference on Knowledge Capture (K-CAP). Association for Computing Machinery, 147–153. Marina Del Rey, CA, USA. 2019.    
    [![DOI](https://img.shields.io/badge/DOI-0.1145/3360901.3364444-yellow.svg)](https://doi.org/10.1145/3360901.3364444)
    [![SLIDES](https://img.shields.io/badge/slides-pdf-orange.svg)](https://www.slideshare.net/CarlosBadenes/scalable-crosslingual-document-similarity-through-languagespecific-concept-hierarchies)  
* **Carlos Badenes-Olmedo**, José Luis Redondo-García, and Oscar Corcho. [Legal document retrieval across languages: topic hierarchies based on synsets](http://cbadenes.github.io/papers/2019-Legal-Documents-Retrieval.pdf). Proceedings of the 1st Workshop on Iberlegal co-located with 32nd International Conference on Legal Knowledge and Information Systems organized by the Foundation for Legal Knowledge Based Systems (JURIX). Madrid, Spain. 2019.    
    [![PROCEEDINGS](https://img.shields.io/badge/Proceedings-IberLegal-purple.svg)](https://plantl.mineco.gob.es/tecnologias-lenguaje/comunicacion-formacion/eventos/Paginas/iberlegal-2019.aspx)
    [![SLIDES](https://img.shields.io/badge/slides-pdf-orange.svg)](https://plantl.mineco.gob.es/tecnologias-lenguaje/comunicacion-formacion/eventos/iberlegal2019/Sesi%C3%B3n%20t%C3%A9cnico-acad%C3%A9mica/topic-hierarchies-based%20on-synsets.pdf)  
* Beatriz López-Centeno, **Carlos Badenes-Olmedo**, Ángel Mataix-Sanjuan, Katie McAllister, José M Bellón, Sara Gibbons, Pascual Balsalobre, Leire Pérez-Latorre, Juana Benedí, Catia Marzolini, Ainhoa Aranguren-Oyarzábal, Saye Khoo, María J Calvo-Alcántara, Juan Berenguer. *Polypharmacy and Drug-Drug Interactions in People Living With Human Immunodeficiency Virus in the Region of Madrid, Spain: A Population-Based Study*. Clinical Infectious Diseases. vol. 71,2, 353-362. 2020.    
    [![DOI](https://img.shields.io/badge/DOI-10.1093/cid/ciz811-yellow.svg)](https://doi.org/10.1093/cid/ciz811)
* Ahmet Soylu, Oscar Corcho, Brian Elvesaeter, **Carlos Badenes-Olmedo**, Francisco Yedro, Matej Kovacic, Matej Posinkovic, Ian Makgill, Chris Taggart, Elena Simperl, Till C. Lech, and Dumitru Roman. *Enhancing Public Procurement in the European Union through Constructing and Exploiting an Integrated Knowledge Graph*. Proceedings of the 19th International Semantic Web Conference (ISWC). 2020.    
    [![DOI](https://img.shields.io/badge/DOI-10.1007/978_3_030_62466_8_27-yellow.svg)](https://doi.org/10.1007/978-3-030-62466-8_27)
* Ahmet Soylu, Oscar Corcho, Brian Elvesaeter, **Carlos Badenes-Olmedo**, Francisco Yedro, Matej Kovacic, Matej Posinkovic, Ian Makgill, Chris Taggart, Elena Simperl, Till C. Lech, and Dumitru Roman. [TheyBuyForYou Platform and Knowledge Graph: Expanding Horizons in Public Procurement with Open Linked Data](http://www.semantic-web-journal.net/system/files/swj2797.pdf). Semantic Web journal. 2021.    
    [![DOI](https://img.shields.io/badge/DOI-pending-yellow.svg)](http://www.semantic-web-journal.net/content/theybuyforyou-platform-and-knowledge-graph-expanding-horizons-public-procurement-open-0)
* **Carlos Badenes-Olmedo**, David Chaves-Fraga, Maria Poveda-Villalon, Ana Iglesias-Molina, Pablo Calleja, Socorro Bernardos, Patricia Martín-Chozas, Alba Fernández-Izquierdo, Elvira Amador-Dominguez, Paola Espinoza-Arias, Luis Pozo, Edna Ruckhaus, Esteban Gonzalez-Guardia, Raquel Cedazo, Beatriz Lopez-Centeno, and Oscar Corcho. [Drugs4Covid: Drug-driven Knowledge Exploitation based on Scientific Publications](https://arxiv.org/pdf/2012.01953.pdf). arXiv e-prints:2012.01953. 2020.    
    [![DOI](https://img.shields.io/badge/DOI-2012.01953-yellow.svg)](https://arxiv.org/abs/2012.01953)
    [![SITE](https://img.shields.io/badge/Site-drugs4covid-blue.svg)](https://drugs4covid.oeg.fi.upm.es)  
