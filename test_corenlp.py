from nlplogic.corenlp import search_wiki, summary_wiki, get_text_blob, get_noun_phrases


def test_search_wiki():
    """Tests search_wiki function"""
    assert any(
        "Barack" in result or "Obama" in result
        for result in search_wiki("Barack Obama")
    )


def test_summary_wiki():
    """Tests summary_wiki function"""
    assert any(
        word
        in "Barack Hussein Obama II ( (listen); born August 4, 1961) is an American politician and attorney who served as the 44th president of the United States from 2009 to 2017. A member of the Democratic Party, Barack Obama was the first African-American president of the United States. He previously served as a U.S. senator from Illinois from 2005 to 2008 and an Illinois state senator from 1997 to 2004."
        for word in summary_wiki("Barack Obama").split()
    )


def test_get_text_blob():
    """Tests get_text_blob function"""
    assert get_text_blob("This is a test") == "This is a test"


def test_get_noun_phrases():
    """Tests get_noun_phrases function"""
    assert any(
        phrase in get_noun_phrases("Barack Obama")
        for phrase in [
            "barack hussein obama ii",
            "american",
            "politician",
            "attorney",
            "44th president",
            "united states",
            "member",
            "democratic party",
            "barack obama",
            "first african-american president",
            "united states",
            "u.s. senator",
            "illinois",
            "illinois state senator",
        ]
    )
