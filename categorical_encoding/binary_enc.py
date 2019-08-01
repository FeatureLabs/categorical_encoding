from featuretools.primitives.base.transform_primitive_base import (
    TransformPrimitive
)
from featuretools.variable_types import Categorical, Numeric


class BinaryEnc(TransformPrimitive):
    name = "binary_enc"
    input_types = [Categorical]
    return_type = Numeric

    def __init__(self, mapping=None, mapping_ord=None):
        self.mapping = mapping
        self.mapping_ord = mapping_ord
        self.number_output_features = mapping.shape[1]

    def get_function(self):
        def transform(X):
            if self.mapping_ord is not None:
                X = X.map(self.mapping_ord)
            if self.mapping is not None:
                X = X.map(self.mapping)
            return X
        return transform

    def generate_name(self, base_feature_names):
        return u"%s_%s" % (base_feature_names[0].upper(), 'binary')
