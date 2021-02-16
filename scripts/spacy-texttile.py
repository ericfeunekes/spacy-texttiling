'''The following code is a spacy implementation of NLTK's textTiling module
https://www.nltk.org/_modules/nltk/tokenize/texttiling.html
'''

from typing import List, Any
import re
from spacy.language import Language
from spacy.tokens import Doc, Span, Token
from typing import Any
import spacy


@Language.component('texttile')
class SpacyTextTile(object):
    '''SpaCy pipeline for textiling'''

    name = 'texttile'

    def __init__(
            self,
            text: str,
            w: int = 20,
            k: int = 10,
            similarity_method: str = 'BLOCK_COMPARISON',
            stopwords: List[str] = None,
            smoothing_method: str = 'DEFAULT_SMOOTHING',
            smoothing_width: int = 2,
            smoothing_rounds: int = 1,
            cutoff_policy: int = 1,
            demo_mode=False) -> None:

        Span.set_extension('Topic', getter=self.get_topics, force=True)
        Doc.set_extension('Topic', getter=self.get_topics, force=True)

        self.text = text
        self.w = w
        self.k = k
        self.similarity_method = similarity_method
        if stopwords is None:
            self.stopwords = spacy.blank('en').Defaults.stop_words
        else:
            self.stopwords = stopwords

    def __call__(
        self,
        doc: Doc
    ) -> Any:
        return doc

    def get_topics(
        self,
    ) -> List[str]:
        pass

    def mark_paragraphs(
        self,
        text: str,
        min_length: int = 100
    ) -> List[int]:
        '''Marks tabs and line breaks as the beginning of a paragraph'''

        # Look for two+ indents / breaks
        pattern = re.compile("[ \t\r\f\v\n]{2,}")
        matches = pattern.finditer(text)

        last_break = 0
        pbreaks = [0]
        for pb in matches:
            if pb.start() - last_break < min_length:
                continue
            pbreaks.append(pb.start())
            last_break = pb.start()

        return pbreaks
