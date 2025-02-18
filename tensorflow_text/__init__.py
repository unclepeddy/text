# coding=utf-8
# Copyright 2019 TF.Text Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Various tensorflow ops related to text-processing."""
from tensorflow.python.util.all_util import remove_undocumented

# pylint: disable=wildcard-import,g-import-not-at-top
from tensorflow_text.python.ops import *

_allowed_symbols = [
    "case_fold_utf8",
    "coerce_to_structurally_valid_utf8",
    "gather_with_default",
    "greedy_constrained_sequence",
    "ngrams",
    "normalize_utf8",
    "pad_along_dimension",
    "Reduction",
    "sentence_fragments",
    "sliding_window",
    "span_alignment",
    "span_overlaps",
    "Tokenizer",
    "TokenizerWithOffsets",
    "UnicodeScriptTokenizer",
    "viterbi_constrained_sequence",
    "WhitespaceTokenizer",
    "wordshape",
    "WordShape",
    "WordpieceTokenizer",
]

remove_undocumented(__name__, _allowed_symbols)
