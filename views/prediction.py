def load_view():
    import streamlit as st

    st.markdown("## Predicting house prices in Amsterdam")
    with st.form(key="my_form"):

        c1, c2 = st.columns([1, 5])

        with c1:
            ModelType = st.radio(
                "Choose your model",
                ["DistilBERT (Default)", "Flair"],
                help="At present, you can choose between 2 models (Flair or DistilBERT) to embed your text. More to come!",
            )

            # if ModelType == "Default (DistilBERT)":
            #     # kw_model = KeyBERT(model=roberta)

            #     @st.cache(allow_output_mutation=True)
            #     def load_model():
            #         return KeyBERT(model=roberta)

            #     kw_model = load_model()

            # else:

            #     @st.cache(allow_output_mutation=True)
            #     def load_model():
            #         return KeyBERT("distilbert-base-nli-mean-tokens")

            #     kw_model = load_model()

            top_N = st.slider(
                "# of results",
                min_value=1,
                max_value=30,
                value=10,
                help="You can choose the number of keywords/keyphrases to display. Between 1 and 30, default number is 10.",
            )
            min_Ngrams = st.number_input(
                "Minimum Ngram",
                min_value=1,
                max_value=4,
                help="""The minimum value for the ngram range.
                *Keyphrase_ngram_range* sets the length of the resulting keywords/keyphrases.
                To extract keyphrases, simply set *keyphrase_ngram_range* to (1, 2) or higher depending on the number of words you would like in the resulting keyphrases.""",
                # help="Minimum value for the keyphrase_ngram_range. keyphrase_ngram_range sets the length of the resulting keywords/keyphrases. To extract keyphrases, simply set keyphrase_ngram_range to (1, # 2) or higher depending on the number of words you would like in the resulting keyphrases.",
            )

            max_Ngrams = st.number_input(
                "Maximum Ngram",
                value=2,
                min_value=1,
                max_value=4,
                help="""The maximum value for the keyphrase_ngram_range.
                        *Keyphrase_ngram_range* sets the length of the resulting keywords/keyphrases.
                        To extract keyphrases, simply set *keyphrase_ngram_range* to (1, 2) or higher depending on the number of words you would like in the resulting keyphrases.""",
            )

            StopWordsCheckbox = st.checkbox(
                "Remove stop words",
                help="Tick this box to remove stop words from the document (currently English only)",
            )

            use_MMR = st.checkbox(
                "Use MMR",
                value=True,
                help="You can use Maximal Margin Relevance (MMR) to diversify the results. It creates keywords/keyphrases based on cosine similarity. Try high/low 'Diversity' settings below for interesting variations.",
            )

            Diversity = st.slider(
                "Keyword diversity (MMR only)",
                value=0.5,
                min_value=0.0,
                max_value=1.0,
                step=0.1,
                help="""The higher the setting, the more diverse the keywords.
                
                        Note that the *Keyword diversity* slider only works if the *MMR* checkbox is ticked.
                     """,
            )

            submit_button = st.form_submit_button(label="✨ Predict data data!")

        with c2:

            st.markdown("### Check out the prices!")

            import pandas as pd
            from db import connection

            amsterdam_data = pd.read_sql("SELECT * FROM amsterdam INNER JOIN geo_info ON (amsterdam.wijkcode = geo_info.wijkcode)", con=connection)

            st.map(amsterdam_data)

    if not submit_button:
        st.stop()
