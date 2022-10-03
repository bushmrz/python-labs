from natasha import (Segmenter, NewsEmbedding,
                     NewsMorphTagger, NewsSyntaxParser, Doc)

segmenter = Segmenter()
emb = NewsEmbedding()
morph_tagger = NewsMorphTagger(emb)
syntax_parser = NewsSyntaxParser(emb)
text = 'Саша шла к себе домой с модной вечерушки. Завязался разговор про морских зверушек'
doc = Doc(text)
doc.segment(segmenter)
doc.tag_morph(morph_tagger)
doc.parse_syntax(syntax_parser)
print(doc.tokens[:10])
doc.sents[0].syntax.print()