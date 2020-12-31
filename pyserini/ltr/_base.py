from ..pyclass import autoclass, JString, JArrayList
import json

class Feature:
   def name(self):
        return self.extractor.getName()

class BM25(Feature):
    def __init__(self, k1=0.9, b=0.4, field='contents', qfield='analyzed'):
        Jclass = autoclass('io.anserini.ltr.feature.base.BM25')
        self.extractor = Jclass(k1, b, JString(field), JString(qfield))

class BM25Min(Feature):
    def __init__(self, pooler, k1=0.9, b=0.4, field='contents'):
        Jclass = autoclass('io.anserini.ltr.feature.base.BM25Min')
        self.extractor = Jclass(pooler.extractor, k1, b, JString(field))

class BM25Max(Feature):
    def __init__(self, pooler, k1=0.9, b=0.4, field='contents'):
        Jclass = autoclass('io.anserini.ltr.feature.base.BM25Max')
        self.extractor = Jclass(pooler.extractor, k1, b, JString(field))

class BM25Mean(Feature):
    def __init__(self, pooler, k1=0.9, b=0.4, field='contents'):
        Jclass = autoclass('io.anserini.ltr.feature.base.BM25Mean')
        self.extractor = Jclass(pooler.extractor, k1, b, JString(field))

class BM25HMean(Feature):
    def __init__(self, pooler, k1=0.9, b=0.4, field='contents'):
        Jclass = autoclass('io.anserini.ltr.feature.base.BM25HMean')
        self.extractor = Jclass(pooler.extractor, k1, b, JString(field))

class BM25Var(Feature):
    def __init__(self, pooler, k1=0.9, b=0.4, field='contents'):
        Jclass = autoclass('io.anserini.ltr.feature.base.BM25Var')
        self.extractor = Jclass(pooler.extractor, k1, b, JString(field))

class BM25Quartile(Feature):
    def __init__(self, pooler, k1=0.9, b=0.4, field='contents'):
        Jclass = autoclass('io.anserini.ltr.feature.base.BM25Quartile')
        self.extractor = Jclass(pooler.extractor, k1, b, JString(field))

class LMDir(Feature):
    def __init__(self,mu=1000, field='contents', qfield='analyzed'):
        Jclass = autoclass('io.anserini.ltr.feature.base.LMDir')
        self.extractor = Jclass(mu, JString(field), JString(qfield))

class LMJM(Feature):
    def __init__(self,lamda=0.5, field='contents', qfield='analyzed'):
        Jclass = autoclass('io.anserini.ltr.feature.base.LMJM')
        self.extractor = Jclass(lamda, JString(field), JString(qfield))

class NTFIDF(Feature):
    def __init__(self, field='contents', qfield='analyzed'):
        Jclass = autoclass('io.anserini.ltr.feature.base.NTFIDF')
        self.extractor = Jclass(JString(field), JString(qfield))

class ProbalitySum(Feature):
    def __init__(self , field='contents', qfield='analyzed'):
        Jclass = autoclass('io.anserini.ltr.feature.base.ProbalitySum')
        self.extractor = Jclass(JString(field), JString(qfield))

class DFR_GL2(Feature):
    def __init__(self, field='contents', qfield='analyzed'):
        Jclass = autoclass('io.anserini.ltr.feature.base.DFR_GL2')
        self.extractor = Jclass(JString(field), JString(qfield))

class IBMModel1(Feature):
    def __init__(self, path, field, tag, qfield):
        Jclass = autoclass('io.anserini.ltr.feature.base.IBMModel1')
        self.extractor = Jclass(JString(path), JString(field), JString(tag), JString(qfield))

class DFR_In_expB2(Feature):
    def __init__(self, field='contents', qfield='analyzed'):
        Jclass = autoclass('io.anserini.ltr.feature.base.DFR_In_expB2')
        self.extractor = Jclass(JString(field), JString(qfield))

class DPH(Feature):
    def __init__(self, field='contents', qfield='analyzed'):
        Jclass = autoclass('io.anserini.ltr.feature.base.DPH')
        self.extractor = Jclass(JString(field), JString(qfield))

class ContextDFR_GL2(Feature):
    def __init__(self, pooler, field='contents', qfield='analyzed'):
        Jclass = autoclass('io.anserini.ltr.feature.base.ContextDFR_GL2')
        self.extractor = Jclass(pooler.extractor, JString(field), JString(qfield))

class ContextDFR_In_expB2(Feature):
    def __init__(self, pooler, field='contents', qfield='analyzed'):
        Jclass = autoclass('io.anserini.ltr.feature.base.ContextDFR_In_expB2')
        self.extractor = Jclass(pooler.extractor, JString(field), JString(qfield))

class ContextDPH(Feature):
    def __init__(self, pooler, field='contents', qfield='analyzed'):
        Jclass = autoclass('io.anserini.ltr.feature.base.ContextDPH')
        self.extractor = Jclass(pooler.extractor, JString(field), JString(qfield))

class Entropy(Feature):
    def __init__(self, field='contents'):
        Jclass = autoclass('io.anserini.ltr.feature.base.Entropy')
        self.extractor = Jclass(JString(field))

class SDM(Feature):
    def __init__(self, field='contents', qfield='analyzed'):
        Jclass = autoclass('io.anserini.ltr.feature.base.SDM')
        self.extractor = Jclass(JString(field), JString(qfield))

class Proximity(Feature):
    def __init__(self, field='contents', qfield='analyzed'):
        Jclass = autoclass('io.anserini.ltr.feature.base.Proximity')
        self.extractor = Jclass(JString(field), JString(qfield))

class TPscore(Feature):
    def __init__(self, field='contents', qfield='analyzed'):
        Jclass = autoclass('io.anserini.ltr.feature.base.TPscore')
        self.extractor = Jclass(JString(field), JString(qfield))

class tpDist(Feature):
    def __init__(self, field='contents', qfield='analyzed'):
        Jclass = autoclass('io.anserini.ltr.feature.base.tpDist')
        self.extractor = Jclass(JString(field), JString(qfield))

class DocSize(Feature):
    def __init__(self, field='contents'):
        Jclass = autoclass('io.anserini.ltr.feature.base.DocSize')
        self.extractor = Jclass(JString(field))

class MatchingTermCount(Feature):
    def __init__(self, field='contents', qfield='analyzed'):
        Jclass = autoclass('io.anserini.ltr.feature.base.MatchingTermCount')
        self.extractor = Jclass(JString(field), JString(qfield))

class QueryLength(Feature):
    def __init__(self, qfield='analyzed'):
        Jclass = autoclass('io.anserini.ltr.feature.base.QueryLength')
        self.extractor = Jclass(JString(qfield))


#class QueryLengthNonStopWords(Feature):
    #def __init__(self, qfield='analyzed'):
        #Jclass = autoclass('io.anserini.ltr.feature.base.QueryLengthNonStopWords')
        #self.extractor = Jclass(JString(qfield))

class SCS(Feature):
    def __init__(self, field='contents', qfield='analyzed'):
        Jclass = autoclass('io.anserini.ltr.feature.base.SCS')
        self.extractor = Jclass(JString(field), JString(qfield))

class SumMatchingTF(Feature):
    def __init__(self, field='contents', qfield='analyzed'):
        Jclass = autoclass('io.anserini.ltr.feature.base.SumMatchingTF')
        self.extractor = Jclass(JString(field), JString(qfield))

class QueryCoverageRatio(Feature):
    def __init__(self, field='contents', qfield='analyzed'):
        Jclass = autoclass('io.anserini.ltr.feature.base.QueryCoverageRatio')
        self.extractor = Jclass(JString(field), JString(qfield))

class RunList(Feature):
    def __init__(self,filename,tag):
        Jclass = autoclass('io.anserini.ltr.feature.base.RunList')
        self.extractor = Jclass(filename,tag)

class StopCover(Feature):
    def __init__(self, field='contents'):
        Jclass = autoclass('io.anserini.ltr.feature.base.StopCover')
        self.extractor = Jclass(JString(field))

class StopRatio(Feature):
    def __init__(self, field='contents'):
        Jclass = autoclass('io.anserini.ltr.feature.base.StopRatio')
        self.extractor = Jclass(JString(field))

class UniqueTermCount(Feature):
    def __init__(self, qfield='analyzed'):
        Jclass = autoclass('io.anserini.ltr.feature.base.UniqueTermCount')
        self.extractor = Jclass(JString(qfield))

class UnorderedSequentialPairs(Feature):
    def __init__(self, gap=8, field='contents', qfield='analyzed'):
        Jclass = autoclass('io.anserini.ltr.feature.base.UnorderedSequentialPairs')
        self.extractor = Jclass(gap, JString(field), JString(qfield))

class OrderedSequentialPairs(Feature):
    def __init__(self, gap=8, field='contents', qfield='analyzed'):
        Jclass = autoclass('io.anserini.ltr.feature.base.OrderedSequentialPairs')
        self.extractor = Jclass(gap, JString(field), JString(qfield))

class UnorderedQueryPairs(Feature):
    def __init__(self, gap=8, field='contents', qfield='analyzed'):
        Jclass = autoclass('io.anserini.ltr.feature.base.UnorderedQueryPairs')
        self.extractor = Jclass(gap, JString(field), JString(qfield))

class OrderedQueryPairs(Feature):
    def __init__(self, gap=8, field='contents', qfield='analyzed'):
        Jclass = autoclass('io.anserini.ltr.feature.base.OrderedQueryPairs')
        self.extractor = Jclass(gap, JString(field), JString(qfield))

class AvgPooler(Feature):
    def __init__(self):
        Jclass = autoclass('io.anserini.ltr.feature.AvgPooler')
        self.extractor = Jclass()

class SumPooler(Feature):
    def __init__(self):
        Jclass = autoclass('io.anserini.ltr.feature.SumPooler')
        self.extractor = Jclass()

class MedianPooler(Feature):
    def __init__(self):
        Jclass = autoclass('io.anserini.ltr.feature.MedianPooler')
        self.extractor = Jclass()

class MinPooler(Feature):
    def __init__(self):
        Jclass = autoclass('io.anserini.ltr.feature.MinPooler')
        self.extractor = Jclass()

class MaxPooler(Feature):
    def __init__(self):
        Jclass = autoclass('io.anserini.ltr.feature.MaxPooler')
        self.extractor = Jclass()

class VarPooler(Feature):
    def __init__(self):
        Jclass = autoclass('io.anserini.ltr.feature.VarPooler')
        self.extractor = Jclass()

class ConfidencePooler(Feature):
    def __init__(self):
        Jclass = autoclass('io.anserini.ltr.feature.ConfidencePooler')
        self.extractor = Jclass()

class MaxMinRatioPooler(Feature):
    def __init__(self):
        Jclass = autoclass('io.anserini.ltr.feature.MaxMinRatioPooler')
        self.extractor = Jclass()

class tfStat(Feature):
    def __init__(self, pooler, field='contents', qfield='analyzed'):
        Jclass = autoclass('io.anserini.ltr.feature.base.tfStat')
        self.extractor = Jclass(pooler.extractor, JString(field), JString(qfield))

class tfIdfStat(Feature):
    def __init__(self, pooler, field='contents', qfield='analyzed'):
        Jclass = autoclass('io.anserini.ltr.feature.base.tfIdfStat')
        self.extractor = Jclass(pooler.extractor, JString(field), JString(qfield))

class normalizedDocSizeStat(Feature):
    def __init__(self, pooler, field='contents', qfield='analyzed'):
        Jclass = autoclass('io.anserini.ltr.feature.base.normalizedDocSizeStat')
        self.extractor = Jclass(pooler.extractor, JString(field), JString(qfield))

class normalizedTfStat(Feature):
    def __init__(self, pooler, field='contents', qfield='analyzed'):
        Jclass = autoclass('io.anserini.ltr.feature.base.normalizedTfStat')
        self.extractor = Jclass(pooler.extractor, JString(field), JString(qfield))

class idfStat(Feature):
    def __init__(self, pooler, field='contents', qfield='analyzed'):
        Jclass = autoclass('io.anserini.ltr.feature.base.idfStat')
        self.extractor = Jclass(pooler.extractor, JString(field), JString(qfield))

class ictfStat(Feature):
    def __init__(self, pooler, field='contents', qfield='analyzed'):
        Jclass = autoclass('io.anserini.ltr.feature.base.ictfStat')
        self.extractor = Jclass(pooler.extractor, JString(field), JString(qfield))

class scqStat(Feature):
    def __init__(self, pooler, field='contents', qfield='analyzed'):
        Jclass = autoclass('io.anserini.ltr.feature.base.scqStat')
        self.extractor = Jclass(pooler.extractor, JString(field), JString(qfield))

class FeatureExtractor:
    def __init__(self, index_dir, worker_num=1):
        JFeatureExtractorUtils = autoclass('io.anserini.ltr.FeatureExtractorUtils')
        self.utils = JFeatureExtractorUtils(JString(index_dir), worker_num)
        self.feature_name = []

    def add(self, pyclass):
        """
        add feature extractor; cannot add feature extractors in the middle of extraction
        Parameters
        ----------
        pyclass: Feature
            an initialized feature extractor

        """
        self.utils.add(pyclass.extractor)
        self.feature_name.append(pyclass.name())

    def feature_names(self):
        """
        get all feature names
        Returns
        -------
        List[str]   all the feature names in order
        """
        return self.feature_name

    def lazy_extract(self, qid, doc_ids, query_dict):
        """
        sumbit tasks to workers
        Parameters
        ----------
        qid: str
            unique query id
        query_tokens: List[str]
            tokenized query
        doc_ids: List[str]
            doc id we need to extract on
        query_text_unlemma:  List[str]
            unlemma query text
        query_bert: List[str]
            query text tokenized by bert
        """
        input = {'qid': qid, 'docIds': doc_ids}
        assert 'qid' not in query_dict
        assert 'docIds' not in query_dict
        input.update(query_dict)
        self.utils.lazyExtract(JString(json.dumps(input)))

    def get_result(self, qid):
        """
        get task result by query id; this call will be blocked until the task is finished
        Parameters
        ----------
        qid: str
         unique query id; mush be the same id that is used to submit the task

        Returns
        -------
        dict: a parsed json

        """
        res = self.utils.getResult(JString(qid))
        return json.loads(res)


