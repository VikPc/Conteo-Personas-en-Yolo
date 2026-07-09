import os
import pandas as pd

from config import OUTPUT_FOLDER


def save_csv(summary):

    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    output_file = os.path.join(
        OUTPUT_FOLDER,
        "detecciones_personas.csv"
    )

    df = pd.DataFrame(summary)

    df.to_csv(

        output_file,

        index=False

    )

    print(f"CSV generado correctamente: {output_file}")

    return df