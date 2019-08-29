import json
import pandas as pd
from pathlib import Path

data_dir = Path(__file__).parent / 'data'
out_file = data_dir / 'geneExp.json'


def sample_data():
    sample_data = data_dir / 'sample.ini'
    sample_df = pd.read_csv(sample_data,
                            sep='\t',
                            header=None,
                            names=['tissue'],
                            index_col=1)
    for n, sample_i in enumerate(sample_df.index):
        tissue_i = sample_df.loc[sample_i].tissue
        sample_i_inf = {
            'model': 'geneExp.SampleInf',
            'pk': n,
            'fields': {
                "sample_id": sample_i,
                'tissue': tissue_i,
            },
        }
        yield sample_i_inf


def gene_data():
    pass


def main():
    data_list = []
    for inf_i in sample_data():
        data_list.append(inf_i)
    with open(out_file, 'w') as out_inf:
        json.dump(data_list, out_inf)


if __name__ == "__main__":
    main()
