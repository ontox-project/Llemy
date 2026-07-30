# General system instructions

"You are a senior biomedical scientist specializing in systems biology.
Your task is to synthesize information from MINERVA Map data to answer the user's QUESTION.
**MINERVA Map Data** is a comprehensive dump of all reactions and elements from a specific metabolic map. It describes reactions, their participants (reactants, products, modifiers), and details about these elements (names, symbols, annotations). You will need to parse this information to find what's relevant to the QUESTION. Clearly label information derived from this source as "(Source: Minerva Map Data)". If the provided map data doesn't seem to contain information relevant to the QUESTION, state that. If there was an error retrieving this map data, that will be indicated.
Based on the user's QUESTION, analyze the detailed Minerva Map Data.
Create a comprehensive, scientifically rigorous answer.
Your answer should:
- Directly address the user's QUESTION.
- Be accurate and factual.
- Explain complex concepts clearly.
- Explicitly state the source of each piece of information or the status of the data retrieval.

Format the output with clearly delimited sections:
- Each section should start with a bold title (using ** around the title).
- Separate sections with two newlines.

Do not perform web search, restrict yourself to the context provided. 
Do not ask the user if they would like further steps in your answer, restrict yourself to providing information only.

After each statement, give a structured list of pertinent reaction references from the map"

# Example system prompt

"USER QUESTION:"What is the scope of this map? Give me a brief summary of the biology represented"

CONTEXT FROM MINERVA MAP DATA:
Status: "success"

Relevant Map Data (Reaction and Element Descriptions in text blob format):
"RID: 55849 (;Known transition omitted'):
  Reactants: NFE2L2 (annotations: UNIPROT:Q16236,,ENTREZ:4780,REFSEQ:NM_006164,HGNC:7782,HGNC_SYMBOL:NFE2L2)
  Products: NFE2L2 (annotations: UNIPROT:Q16236,,PUBMED:28416361,ENTREZ:4780,REFSEQ:NM_006164,HGNC:7782,HGNC_SYMBOL:NFE2L2)
  Modifiers: None
RID: 55129 (;Transport'):
  Reactants: Cholesterol ester (annotations: CHEBI:CHEBI:17002)
  Products: Cholesterol ester (annotations: CHEBI:CHEBI:17002)
  Modifiers: SCARB1 (formerSymbols: CD36L1) (annotations: UNIPROT:Q8WTV0,HGNC:1664,,HGNC_SYMBOL:SCARB1,ENTREZ:949,REFSEQ:NM_005505)
  (References: KEGG_PATHWAY:map04979)
RID: 56058 (;Negative influence'):
  Reactants: FOXO1 (formerSymbols: FKHR,FOXO1A) (annotations: HGNC:3819,,REFSEQ:NM_002015,ENTREZ:2308,PUBMED:28416361,HGNC_SYMBOL:FOXO1,UNIPROT:Q12778)
  Products: GCK (formerSymbols: MODY2) (annotations: ,ENTREZ:2645,HGNC_SYMBOL:GCK,PUBMED:28416361,REFSEQ:NM_000162,UNIPROT:P35557,HGNC:4195)
  Modifiers: None
RID: 55110 (;Transport'):
  Reactants: LDLR (annotations: HGNC_SYMBOL:LDLR,HGNC:6547,,ENTREZ:3949,REFSEQ:NM_000527,UNIPROT:P01130)
  Products: LDLR (annotations: HGNC_SYMBOL:LDLR,HGNC:6547,,ENTREZ:3949,REFSEQ:NM_000527,UNIPROT:P01130)
  Modifiers: PCSK9 (formerSymbols: HCHOLA3) (annotations: UNIPROT:Q8NBP7,ENTREZ:255738,HGNC:20001,HGNC_SYMBOL:PCSK9,REFSEQ:NM_174936,)
  (References: KEGG_PATHWAY:map04979)
RID: 55833 (;Positive influence'):
  Reactants: NR1H4 (annotations: ,ENTREZ:9971,HGNC:7967,UNIPROT:Q96RI1,REFSEQ:NM_005123,HGNC_SYMBOL:NR1H4)
  Products: NR1I2 (annotations: ,HGNC_SYMBOL:NR1I2,HGNC:7968,REFSEQ:NM_003889,ENTREZ:8856,UNIPROT:O75469)
  Modifiers: None
RID: 55483 (;Transport'):
  Reactants: AKT1 (annotations: ENTREZ:207,HGNC:391,PUBMED:28416361,HGNC_SYMBOL:AKT1,REFSEQ:NM_005163,UNIPROT:P31749,)
  Products: AKT1 (annotations: ENTREZ:207,HGNC:391,PUBMED:28416361,HGNC_SYMBOL:AKT1,REFSEQ:NM_005163,UNIPROT:P31749,)
  Modifiers: None
RID: 55453 (PDmap:re575.0;State transition'):
  Reactants: O2 (annotations: CHEBI:CHEBI:15379,KEGG_COMPOUND:C00007,HMDB:HMDB0001377,PUBCHEM:977,CHEMSPIDER:952,CAS:7782-44-7,WIKIPEDIA:Oxygen)
  Products: superoxide (annotations: HMDB:HMDB0002168,WIKIPEDIA:Superoxide,PUBCHEM:5359597,CHEMSPIDER:4514331,KEGG_COMPOUND:C00704,CHEBI:CHEBI:18421,CAS:11062-77-4)
  Modifiers: None
  (References: PUBMED:19427899)
RID: 55627 (;Positive influence'):
  Reactants: FA > C24
  Products: Very Long Fatty Acids-CoA
  Modifiers: None
RID: 55927 (;Positive influence'):
  Reactants: CYP7A1 (formerSymbols: CYP7) (annotations: HGNC:2651,,REFSEQ:NM_000780,ENTREZ:1581,HGNC_SYMBOL:CYP7A1,UNIPROT:P22680)
  Products: Cholesterol Metabolism (annotations: KEGG_PATHWAY:map04979)
  Modifiers: None
RID: 56108 (;State transition'):
  Reactants: (S)-Hydroxyhexanoyl-CoA (annotations: CHEBI:CHEBI:28276)
  Products: 3-Oxohexanoyl-CoA (annotations: CHEBI:CHEBI:62418,CHEBI:CHEBI:27648)
  Modifiers: HADH (formerSymbols: HADHSC) (annotations: HGNC_SYMBOL:HADH,REFSEQ:NM_005327,,HGNC:4799,ENTREZ:3033,UNIPROT:Q16836)
RID: 55083 (;State transition'):
  Reactants: Cholesterol ester (annotations: CHEBI:CHEBI:17002)
  Products: Cholesterol (annotations: CHEBI:CHEBI:16113,KEGG_COMPOUND:C00187)
  Modifiers: LIPA (annotations: HGNC_SYMBOL:LIPA,ENTREZ:3988,,HGNC:6617,REFSEQ:NM_000235,UNIPROT:P38571)
RID: 56159 (;State transition'):
  Reactants: UDP-Glucose (annotations: CHEBI:CHEBI:18066)
  Products: UDP-Glucuronate (annotations: CHEBI:CHEBI:17200)
  Modifiers: UGDH (annotations: HGNC:12525,ENTREZ:7358,UNIPROT:O60701,REFSEQ:NM_003359,HGNC_SYMBOL:UGDH,)
RID: 56057 (;Positive influence'):
  Reactants: GCG (annotations: HGNC_SYMBOL:GCG,,REFSEQ:NM_002054,HGNC:4191,UNIPROT:P01275,ENTREZ:2641)
  Products: GYS
  Modifiers: None
RID: 55300 (PDmap:re587.0;State transition'):
  Reactants: ACADL (annotations: REFSEQ:NM_001608,,HGNC_SYMBOL:ACADL,HGNC:88,ENTREZ:33,UNIPROT:P28330)
  Products: ACADL (annotations: REFSEQ:NM_001608,,HGNC_SYMBOL:ACADL,HGNC:88,ENTREZ:33,UNIPROT:P28330)
  Modifiers: SIRT3 (annotations: ENTREZ:23410,HGNC_SYMBOL:SIRT3,UNIPROT:Q9NTG7,HGNC:14931,REFSEQ:NM_001017524,)
  (References: PUBMED:20203611|PUBMED:21658599)
RID: 56088 (;State transition'):
  Reactants: RPS6KB1 (formerSymbols: STK14A) (annotations: HGNC:10436,UNIPROT:P23443,ENTREZ:6198,,HGNC_SYMBOL:RPS6KB1,REFSEQ:NM_003161)
  Products: RPS6KB1 (formerSymbols: STK14A) (annotations: HGNC:10436,UNIPROT:P23443,ENTREZ:6198,,HGNC_SYMBOL:RPS6KB1,REFSEQ:NM_003161)
  Modifiers: mTORC1 (annotations: GO:GO:0031931)
RID: 55954 (;State transition'):
  Reactants: Trans-enoyl-ACP
  Products: Acyl-ACP; Palmitate
  Modifiers: MECR (annotations: ENTREZ:51102,,HGNC:19691,HGNC_SYMBOL:MECR,REFSEQ:NM_016011,UNIPROT:Q9BV79)
RID: 56119 (;Known transition omitted'):
  Reactants: Acyl-ACP
  Products: Fatty acyl-ACP
  Modifiers: None
RID: 56032 (;Positive influence'):
  Reactants: GCG (annotations: HGNC_SYMBOL:GCG,,REFSEQ:NM_002054,HGNC:4191,UNIPROT:P01275,ENTREZ:2641)
  Products: Protein kinase A
  Modifiers: None
RID: 55893 (;State transition'):
  Reactants: TSC (annotations: PUBMED:28416361)
  Products: TSC (annotations: PUBMED:28416361)
  Modifiers: AKT1 (annotations: ENTREZ:207,HGNC:391,PUBMED:28416361,HGNC_SYMBOL:AKT1,REFSEQ:NM_005163,UNIPROT:P31749,)
RID: 55928 (;State transition'):
  Reactants: ACC
  Products: ACC
  Modifiers: None
RID: 55124 (;Transport'):
  Reactants: Cholesterol ester (annotations: CHEBI:CHEBI:17002)
  Products: Cholesterol ester (annotations: CHEBI:CHEBI:17002)
  Modifiers: None
  (References: KEGG_PATHWAY:map04979)
RID: 55912 (;State transition'):
  Reactants: 4-cis-decenoyl-CoA
  Products: 2-trans-4-cis-decadienoyl-CoA (annotations: CHEBI:CHEBI:29119)
  Modifiers: ACADM (annotations: UNIPROT:P11310,HGNC_SYMBOL:ACADM,,HGNC:89,REFSEQ:NM_000016,ENTREZ:34)
RID: 56170 (;Transport'):
  Reactants: Mitochondrial Metabolism
  Products: Malate (annotations: CHEBI:CHEBI:15595,CHEBI:CHEBI:30797)
  Modifiers: None
RID: 56210 (;State transition'):
  Reactants: Galactose (annotations: CHEBI:CHEBI:28260)
  Products: Galactose-1-Phosphate (annotations: CHEBI:CHEBI:17973)
  Modifiers: GALK1 (formerSymbols: GALK) (annotations: REFSEQ:NM_000154,,HGNC_SYMBOL:GALK1,HGNC:4118,ENTREZ:2584,UNIPROT:P51570); GALK2 (annotations: REFSEQ:NM_001001556,HGNC_SYMBOL:GALK2,HGNC:4119,ENTREZ:2585,,UNIPROT:Q01415)
RID: 55274 (;Known transition omitted'):
  Reactants: CCS:Zn2+:Cu1+; SOD1:Zn2+
  Products: CCS:Zn2+:Cu1+:SOD1:Zn2+
  Modifiers: None
  (References: REACTOME:REACT_264249)
RID: 55433 (;State transition'):
  Reactants: NADPH (annotations: KEGG_COMPOUND:C00005,HMDB:HMDB0000221,CHEMSPIDER:17215925,CHEMBL_COMPOUND:CHEMBL213053,CHEBI:CHEBI:16474,CAS:53-57-6,WIKIPEDIA:NADPH,PUBCHEM:22833512); NAD(+) (annotations: KEGG_COMPOUND:C00003,CAS:53-84-9,PUBCHEM:5893,CHEMSPIDER:5682,REACTOME:REACT_4970.1,CHEBI:CHEBI:15846,HMDB:HMDB0000902,WIKIPEDIA:NAD); H+ (annotations: CHEBI:CHEBI:15378)
  Products: NADP(+) (annotations: CHEBI:CHEBI:18009,WIKIPEDIA:NADP,KEGG_COMPOUND:C00006,CAS:53-59-8,PUBCHEM:5886,CHEMBL_COMPOUND:CHEMBL213053,HMDB:HMDB0000217,CHEMSPIDER:5675); NADH (annotations: REACTOME:REACT_2390.1,KEGG_COMPOUND:C00004,HMDB:HMDB0001487,CHEMSPIDER:903,WIKIPEDIA:NADH,CAS:58-68-4,CHEBI:CHEBI:16908,PUBCHEM:928,CHEMBL_COMPOUND:CHEMBL1628272,MESH_2012:D009243); H+ (annotations: CHEBI:CHEBI:15378)
  Modifiers: NNT (annotations: HGNC:7863,ENTREZ:23530,,HGNC_SYMBOL:NNT,REFSEQ:NM_182977,UNIPROT:Q13423)
  (References: PUBMED:19427899|PUBMED:23216354)
RID: 55126 (;Positive influence'):
  Reactants: LRPAP1 (formerSymbols: A2MRAP,RAP) (annotations: HGNC:6701,ENTREZ:4043,UNIPROT:P30533,,REFSEQ:NM_002337,HGNC_SYMBOL:LRPAP1)
  Products: LRP1 (formerSymbols: A2MR,APR) (annotations: REFSEQ:NM_002332,UNIPROT:Q07954,,ENTREZ:4035,HGNC_SYMBOL:LRP1,HGNC:6692)
  Modifiers: None
  (References: WIKIPATHWAYS:WP5304)
RID: 56017 (;Positive influence'):
  Reactants: MDM2 (annotations: HGNC:6973,ENTREZ:4193,REFSEQ:NM_002392,,HGNC_SYMBOL:MDM2,UNIPROT:Q00987)
  Products: Apoptosis (annotations: GO:GO:1900117,GO:GO:0097194)
  Modifiers: None
RID: 55216 (;State transition'):
  Reactants: 7alpha-hydroxycholesterol (annotations: CHEBI:CHEBI:17500)
  Products: 7-oxocholesterol (annotations: CHEBI:CHEBI:64294)
  Modifiers: None
  (References: WIKIPATHWAYS:WP4718)
RID: 55389 (PDmap:re516.0;State transition'):
  Reactants: (S)-3-hydroxytetradecanoyl-CoA (annotations: CHEBI:CHEBI:27466,REACTOME:REACT_5705.1,KEGG_COMPOUND:C05260,CHEMSPIDER:389500,HMDB:HMDB0003934,PUBCHEM:440602)
  Products: 3-oxotetradecanoyl-CoA (annotations: CAS:122364-86-7,KEGG_COMPOUND:C05261,REACTOME:REACT_5544.1,HMDB:HMDB0003935,CHEBI:CHEBI:28726,CHEMSPIDER:10140190,PUBCHEM:11966197)
  Modifiers: trifunctional Protein
  (References: PUBMED:1550553|REACTOME:REACT_343.2)
RID: 55332 (PDmap:re579.0;State transition'):
  Reactants: TXN (annotations: ENTREZ:7295,UNIPROT:P10599,HGNC:12435,,REFSEQ:NM_001244938,HGNC_SYMBOL:TXN); NADPH (annotations: KEGG_COMPOUND:C00005,HMDB:HMDB0000221,CHEMSPIDER:17215925,CHEMBL_COMPOUND:CHEMBL213053,CHEBI:CHEBI:16474,CAS:53-57-6,WIKIPEDIA:NADPH,PUBCHEM:22833512); H+ (annotations: CHEBI:CHEBI:15378)
  Products: TXN (annotations: ENTREZ:7295,UNIPROT:P10599,HGNC:12435,,REFSEQ:NM_001244938,HGNC_SYMBOL:TXN); NADP(+) (annotations: CHEBI:CHEBI:18009,WIKIPEDIA:NADP,KEGG_COMPOUND:C00006,CAS:53-59-8,PUBCHEM:5886,CHEMBL_COMPOUND:CHEMBL213053,HMDB:HMDB0000217,CHEMSPIDER:5675)
  Modifiers: TXNRD2 (annotations: ,HGNC_SYMBOL:TXNRD2,REFSEQ:NM_006440,HGNC:18155,ENTREZ:10587,UNIPROT:Q9NNW7); TXNRD1 (annotations: HGNC:12437,UNIPROT:Q16881,ENTREZ:7296,REFSEQ:NM_003330,HGNC_SYMBOL:TXNRD1,)
  (References: PUBMED:19427899|REACTOME:REACT_264249)
RID: 55388 (;Translation'):
  Reactants: mt mRNA (annotations: CHEBI:CHEBI:33699)
  Products: mtDNA encoded OXPHOS units (annotations: PUBMED:23149385,PUBMED:30030361)
  Modifiers: Mt translation (annotations: DOI:10.1155/2010/737385); Mt ribosomal proteins (annotations: PUBMED:23149385)
  (References: PUBMED:23149385|TAXONOMY:10090|TAXONOMY:4891|DOI:10.1101/gad.316547.118)
RID: 55731 (;State transition'):
  Reactants: Gutamate (annotations: CHEBI:CHEBI:18237)
  Products: α-Ketogluatarate (annotations: CHEBI:CHEBI:30915); NADH (annotations: CHEBI:CHEBI:16908); ammonium (annotations: CHEBI:CHEBI:28938)
  Modifiers: None
RID: 55612 (;Positive influence'):
  Reactants: NR1I2 (annotations: ,HGNC_SYMBOL:NR1I2,HGNC:7968,REFSEQ:NM_003889,ENTREZ:8856,UNIPROT:O75469)
  Products: PPARG (annotations: HGNC:9236,REFSEQ:NM_005037,HGNC_SYMBOL:PPARG,UNIPROT:P37231,ENTREZ:5468,)
  Modifiers: None
RID: 56105 (;Positive influence'):
  Reactants: mTORC1 (annotations: GO:GO:0031931)
  Products: SREBP-1c (annotations: PUBMED:26451809)
  Modifiers: None
RID: 55262 (PDmap:re585.0;State transition'):
  Reactants: superoxide (annotations: HMDB:HMDB0002168,WIKIPEDIA:Superoxide,PUBCHEM:5359597,CHEMSPIDER:4514331,KEGG_COMPOUND:C00704,CHEBI:CHEBI:18421,CAS:11062-77-4); Fe3+ (annotations: CHEBI:CHEBI:29034)
  Products: O2 (annotations: CHEBI:CHEBI:15379,KEGG_COMPOUND:C00007,HMDB:HMDB0001377,PUBCHEM:977,CHEMSPIDER:952,CAS:7782-44-7,WIKIPEDIA:Oxygen); Fe2+ (annotations: CHEBI:CHEBI:29033); H+ (annotations: CHEBI:CHEBI:15378)
  Modifiers: None
  (References: PUBMED:2172697)
RID: 55591 (;Known transition omitted'):
  Reactants: Dihydroxyacetone-Phosphate (annotations: CHEBI:CHEBI:16108)
  Products: Acyl Dihydroxyacetone Phosphate
  Modifiers: None
RID: 56187 (;Known transition omitted'):
  Reactants: 3-Phospho-Hydroxy-Pyruvate (annotations: CHEBI:CHEBI:18110); Glutamate (annotations: CHEBI:CHEBI:29987,CHEBI:CHEBI:14321,CHEBI:CHEBI:16015,CHEBI:CHEBI:18237)
  Products: 3-Phosphoserine (annotations: CHEBI:CHEBI:15811); α-Ketogluatarate (annotations: CHEBI:CHEBI:30915)
  Modifiers: PSAT1 (annotations: REFSEQ:NM_021154,HGNC:19129,UNIPROT:Q9Y617,,ENTREZ:29968,HGNC_SYMBOL:PSAT1)
RID: 56194 (;State transition'):
  Reactants: Malate (annotations: CHEBI:CHEBI:15595,CHEBI:CHEBI:30797)
  Products: Pyruvate (annotations: CHEBI:CHEBI:15361)
  Modifiers: ME
RID: 55720 (;Positive influence'):
  Reactants: PPARA (formerSymbols: PPAR) (annotations: HGNC_SYMBOL:PPARA,ENTREZ:5465,REFSEQ:NM_001001928,,PUBMED:26451809,UNIPROT:Q07869,HGNC:9232)
  Products: APOA1 (annotations: HGNC:600,,UNIPROT:P02647,ENTREZ:335,REFSEQ:NM_000039,HGNC_SYMBOL:APOA1)
  Modifiers: None
RID: 56136 (;State transition'):
  Reactants: Mannose-6-Phosphate (annotations: CHEBI:CHEBI:17369)
  Products: Fructose-6-Phosphate (annotations: CHEBI:CHEBI:15946,CHEBI:CHEBI:16084)
  Modifiers: MPI (annotations: ENTREZ:4351,HGNC:7216,,REFSEQ:NM_001289155,HGNC_SYMBOL:MPI,UNIPROT:P34949)
RID: 55725 (;Negative influence'):
  Reactants: AMPK (annotations: GO:GO:0031588)
  Products: mTORC1 (annotations: GO:GO:0031931)
  Modifiers: None
RID: 55193 (;State transition'):
  Reactants: Dihydro-FF-MAS (annotations: CHEBI:CHEBI:78904)
  Products: Dihydro-T-MAS (annotations: CHEBI:CHEBI:87044)
  Modifiers: TM7SF2 (annotations: ,HGNC:11863,REFSEQ:NM_003273,UNIPROT:O76062,ENTREZ:7108,HGNC_SYMBOL:TM7SF2); LBR (annotations: HGNC_SYMBOL:LBR,UNIPROT:Q14739,REFSEQ:NM_002296,HGNC:6518,ENTREZ:3930,)
  (References: WIKIPATHWAYS:WP4718|DOI:10.1016/B978-0-12-824048-9.00005-5)
RID: 55404 (PDmap:re388.0;State transition'):
  Reactants: (S)-2-hydroxyglutaric acid (annotations: REACTOME:REACT_25542.1,CHEBI:CHEBI:32797); FAD (annotations: KEGG_COMPOUND:C00016,CHEMBL_COMPOUND:CHEMBL1232653,WIKIPEDIA:FAD,CHEMSPIDER:559059,HMDB:HMDB0001248,PUBCHEM:643975,CHEBI:CHEBI:16238,CAS:146-14-5)
  Products: 2-oxoglutaric acid (annotations: KEGG_COMPOUND:C00026,REACTOME:REACT_3871.1,CHEBI:CHEBI:30915,CAS:328-50-7,MESH_2012:C029743,PUBCHEM:51,CHEMSPIDER:50,HMDB:HMDB0000208,WIKIPEDIA:Alpha-Ketoglutaric_acid); FADH2 (annotations: CHEBI:CHEBI:17877,HMDB:HMDB0001197,CHEMBL_COMPOUND:CHEMBL1232653,WIKIPEDIA:FADH,PUBCHEM:446013,CHEMSPIDER:393487,KEGG_COMPOUND:C01352,CAS:146-14-5)
  Modifiers: D2HGDH (annotations: UNIPROT:Q8N465,HGNC:28358,ENTREZ:728294,REFSEQ:NM_152783,HGNC_SYMBOL:D2HGDH,); Zn2+ (annotations: CHEBI:CHEBI:29105); Co2+ (annotations: CHEBI:CHEBI:48828,REACTOME:REACT_26586.1); Mn2+ (annotations: CHEBI:CHEBI:29035)
  (References: PUBMED:7564244|PUBMED:15070399|PUBMED:16435184|REACTOME:REACT_25270.2)
RID: 56013 (;State transition'):
  Reactants: Monoacylglycerol (annotations: CHEBI:CHEBI:17408)
  Products: Glycerol (annotations: CHEBI:CHEBI:17754); Fatty Acid (annotations: CHEBI:CHEBI:35366)
  Modifiers: MGLL (annotations: ,HGNC:17038,ENTREZ:11343,REFSEQ:NM_007283,HGNC_SYMBOL:MGLL,UNIPROT:Q99685)
RID: 55775 (;Positive influence'):
  Reactants: Cholesterol (annotations: CHEBI:CHEBI:16113,KEGG_COMPOUND:C00187)
  Products: Lipoproteins (annotations: GO:GO:0140306,GO:GO:0008203)
  Modifiers: None
RID: 55213 (;Transcription'):
  Reactants: MYLIP (annotations: REFSEQ:NM_013262,ENTREZ:29116,UNIPROT:Q8WY64,HGNC:21155,HGNC_SYMBOL:MYLIP,)
  Products: MYLIP (annotations: REFSEQ:NM_013262,ENTREZ:29116,UNIPROT:Q8WY64,HGNC:21155,HGNC_SYMBOL:MYLIP,)
  Modifiers: SREBF1 (annotations: UNIPROT:P36956,REFSEQ:NM_004176,ENTREZ:6720,HGNC:11289,HGNC_SYMBOL:SREBF1,)
  (References: WIKIPATHWAYS:WP4718)
RID: 55934 (;Positive influence'):
  Reactants: Cytochrome c (annotations: CHEBI:CHEBI:18070)
  Products: Complex IV
  Modifiers: None
RID: 55707 (;Positive influence'):
  Reactants: FOXO1 (formerSymbols: FKHR,FOXO1A) (annotations: HGNC:3819,,REFSEQ:NM_002015,ENTREZ:2308,PUBMED:28416361,HGNC_SYMBOL:FOXO1,UNIPROT:Q12778)
  Products: PCK1 (annotations: ,PUBMED:28416361,HGNC:8724,UNIPROT:P35558,HGNC_SYMBOL:PCK1,REFSEQ:NM_002591,ENTREZ:5105)
  Modifiers: None
RID: 55396 (PDmap:re509.0;State transition'):
  Reactants: 3-oxopalmitoyl-CoA (annotations: HMDB:HMDB0006402,CAS:34619-89-1,CHEBI:CHEBI:15491,REACTOME:REACT_3202.1,CHEMSPIDER:389499,KEGG_COMPOUND:C05259,PUBCHEM:440601)
  Products: myristoyl-CoA (annotations: CHEBI:CHEBI:15532,REACTOME:REACT_2294.1,HMDB:HMDB0001521,KEGG_COMPOUND:C02593,CHEMSPIDER:58623,CAS:3130-72-1,PUBCHEM:65113)
  Modifiers: trifunctional Protein
  (References: PUBMED:1550553|REACTOME:REACT_582.2)
RID: 55200 (;Known transition omitted'):
  Reactants: ABCG1 (annotations: HGNC_SYMBOL:ABCG1,ENTREZ:9619,,UNIPROT:P45844,REFSEQ:NM_207174,HGNC:73)
  Products: Sterol Eflux (annotations: GO:GO:0035382)
  Modifiers: None
  (References: WIKIPATHWAYS:WP4718)
RID: 55512 (;State transition'):
  Reactants: PIP2
  Products: PIP3
  Modifiers: PI3K
RID: 56138 (;Transport'):
  Reactants: Glucose (annotations: CHEBI:CHEBI:17234)
  Products: Glucose (annotations: CHEBI:CHEBI:17234)
  Modifiers: Glucose transporters (GLUT)
  (References: WIKIPATHWAYS:WP534)
RID: 55500 (;Positive influence'):
  Reactants: AKT1 (annotations: ENTREZ:207,HGNC:391,PUBMED:28416361,HGNC_SYMBOL:AKT1,REFSEQ:NM_005163,UNIPROT:P31749,)
  Products: CREB1 (annotations: REFSEQ:NM_134442,HGNC:2345,ENTREZ:1385,HGNC_SYMBOL:CREB1,UNIPROT:P16220,)
  Modifiers: None
RID: 55613 (;State transition'):
  Reactants: Isocitrate (annotations: CHEBI:CHEBI:16087)
  Products: α-Ketogluatarate (annotations: CHEBI:CHEBI:30915); NADH (annotations: CHEBI:CHEBI:16908)
  Modifiers: isocitrate dehydrogenase 2
RID: 55594 (;State transition'):
  Reactants: Acetaldehyde (annotations: CHEBI:CHEBI:15343)
  Products: Acetate (annotations: CHEBI:CHEBI:30089,CHEBI:CHEBI:47622)
  Modifiers: ALDH
RID: 55325 (PDmap:re382.0;State transition'):
  Reactants: oxaloacetate(2-) (annotations: PUBCHEM:970,CHEBI:CHEBI:30744,KEGG_COMPOUND:C00036,CAS:328-42-7,HMDB:HMDB0000223,CHEMSPIDER:945,REACTOME:REACT_5376.1,CHEBI:CHEBI:16452,WIKIPEDIA:Oxalacetic acid); H+ (annotations: CHEBI:CHEBI:15378); NADH (annotations: REACTOME:REACT_2390.1,KEGG_COMPOUND:C00004,HMDB:HMDB0001487,CHEMSPIDER:903,WIKIPEDIA:NADH,CAS:58-68-4,CHEBI:CHEBI:16908,PUBCHEM:928,CHEMBL_COMPOUND:CHEMBL1628272,MESH_2012:D009243)
  Products: (S)-malate(2-) (annotations: KEGG_COMPOUND:C00149,HMDB:HMDB0000156,PUBCHEM:222656,REACTOME:REACT_4778.1,CHEMSPIDER:193317,WIKIPEDIA:Apple acid,CHEBI:CHEBI:30797,CHEBI:CHEBI:15589,CAS:97-67-6); NAD(+) (annotations: KEGG_COMPOUND:C00003,CAS:53-84-9,PUBCHEM:5893,CHEMSPIDER:5682,REACTOME:REACT_4970.1,CHEBI:CHEBI:15846,HMDB:HMDB0000902,WIKIPEDIA:NAD)
  Modifiers: malate dehydrogenase 2 (annotations: REACTOME:REACT_11471.1)
  (References: PUBMED:16740313|REACTOME:REACT_11169.3)
RID: 55944 (;State transition'):
  Reactants: Beta-hydroxyacyl-ACP
  Products: Trans-enoyl-ACP
  Modifiers: HTD2 (annotations: REFSEQ:NM_001348712,,ENTREZ:109703458,UNIPROT:P86397,HGNC_SYMBOL:HTD2,HGNC:53111)
RID: 56004 (;State transition'):
  Reactants: Glyceraldehyde (annotations: CHEBI:CHEBI:5445,CHEBI:CHEBI:17378)
  Products: Glycerol (annotations: CHEBI:CHEBI:17754)
  Modifiers: None
RID: 56114 (;State transition'):
  Reactants: Long-chain Fatty Acids
  Products: Fatty acyl-CoA
  Modifiers: ACSL
RID: 55974 (;State transition'):
  Reactants: PYGL (annotations: ENTREZ:5836,REFSEQ:NM_002863,HGNC_SYMBOL:PYGL,HGNC:9725,,UNIPROT:P06737)
  Products: PYGL (annotations: ENTREZ:5836,REFSEQ:NM_002863,HGNC_SYMBOL:PYGL,HGNC:9725,,UNIPROT:P06737)
  Modifiers: None
RID: 55316 (;State transition'):
  Reactants: carnitine (annotations: CHEBI:CHEBI:17126,REACTOME:REACT_11423.1)
  Products: carnitine (annotations: CHEBI:CHEBI:17126,REACTOME:REACT_11423.1)
  Modifiers: L-palmitoylcarnitine (annotations: PUBCHEM:11953816,CHEBI:CHEBI:17490,HMDB:HMDB0000222,CAS:2364-67-2,REACTOME:REACT_11789.2,KEGG_COMPOUND:C02990,CHEMSPIDER:10128117); SLC25A20 (formerSymbols: CACT) (annotations: REFSEQ:NM_000387,HGNC:1421,ENTREZ:788,,UNIPROT:O43772,HGNC_SYMBOL:SLC25A20)
  (References: REACTOME:REACT_11180.3)
RID: 55102 (;State transition'):
  Reactants: Long-chain Fatty Acids (annotations: CHEBI:CHEBI:15904); CoA (annotations: CHEBI:CHEBI:15346)
  Products: Fatty acyl-CoA (annotations: CHEBI:CHEBI:37554)
  Modifiers: LACS
  (References: PUBMED:12856180|PUBMED:18477307)
RID: 55670 (;State transition'):
  Reactants: Zymosterol (annotations: CHEBI:CHEBI:18252)
  Products: Zymostenol (annotations: CHEBI:CHEBI:16608)
  Modifiers: DHCR24 (formerSymbols: DCE) (annotations: REFSEQ:NM_014762,HGNC_SYMBOL:DHCR24,,ENTREZ:1718,UNIPROT:Q15392,HGNC:2859)
  (References: DOI:10.1016/B978-0-12-824048-9.00005-5)
RID: 55112 (;Transport'):
  Reactants: Cholesterol ester (annotations: CHEBI:CHEBI:17002)
  Products: Cholesterol ester (annotations: CHEBI:CHEBI:17002)
  Modifiers: None
  (References: KEGG_PATHWAY:map04979)
RID: 55695 (;State transition'):
  Reactants: Trans-dec-2-enoyl-CoA (annotations: CHEBI:CHEBI:10723)
  Products: Decanoyl-CoA (annotations: CHEBI:CHEBI:28493)
  Modifiers: MECR (annotations: ENTREZ:51102,,HGNC:19691,HGNC_SYMBOL:MECR,REFSEQ:NM_016011,UNIPROT:Q9BV79)
RID: 55444 (PDmap:re511.0;State transition'):
  Reactants: (E)-hexadec-2-enoyl-CoA (annotations: REACTOME:REACT_4177.1,CHEBI:CHEBI:28935)
  Products: (S)-3-hydroxypalmitoyl-CoA (annotations: REACTOME:REACT_2413.1,CHEBI:CHEBI:27402)
  Modifiers: trifunctional Protein
  (References: REACTOME:REACT_1513.2|PUBMED:1550553)
RID: 55125 (;Known transition omitted'):
  Reactants: Chylomicron (annotations: GO:GO:0042627)
  Products: Nascent HDL (annotations: GO:GO:0034364)
  Modifiers: None
  (References: WIKIPATHWAYS:WP5304)
RID: 55811 (;Positive influence'):
  Reactants: PPARA (formerSymbols: PPAR) (annotations: HGNC_SYMBOL:PPARA,ENTREZ:5465,REFSEQ:NM_001001928,,PUBMED:26451809,UNIPROT:Q07869,HGNC:9232)
  Products: ACADM  (annotations: UNIPROT:P11310,HGNC_SYMBOL:ACADM,,HGNC:89,REFSEQ:NM_000016,ENTREZ:34)
  Modifiers: None
RID: 55360 (PDmap:re572.0;State transition'):
  Reactants: arachidonoyl-CoA (annotations: REACTOME:REACT_22603.1,CHEBI:CHEBI:15514)
  Products: 3ODCT-CoA (annotations: REACTOME:REACT_22500.1,CHEBI:CHEBI:63821)
  Modifiers: ELOVL5 (formerSymbols: SCA38) (annotations: REFSEQ:NM_021814,UNIPROT:Q9NYP7,HGNC_SYMBOL:ELOVL5,,ENTREZ:60481,HGNC:21308)
  (References: REACTOME:REACT_22350.1|PUBMED:10970790)
RID: 55932 (;State transition'):
  Reactants: Glycin (annotations: CHEBI:CHEBI:55443,CHEBI:CHEBI:15428); Methylene-FH4 (annotations: CHEBI:CHEBI:20502)
  Products: Serine (annotations: CHEBI:CHEBI:17822,CHEBI:CHEBI:17115); FH4 (annotations: CHEBI:CHEBI:20506)
  Modifiers: Serine Hydroxymethyltransferase
RID: 55643 (;State transition'):
  Reactants: MDM2 (annotations: HGNC:6973,ENTREZ:4193,REFSEQ:NM_002392,,HGNC_SYMBOL:MDM2,UNIPROT:Q00987)
  Products: MDM2 (annotations: HGNC:6973,ENTREZ:4193,REFSEQ:NM_002392,,HGNC_SYMBOL:MDM2,UNIPROT:Q00987)
  Modifiers: AKT1 (annotations: ENTREZ:207,HGNC:391,PUBMED:28416361,HGNC_SYMBOL:AKT1,REFSEQ:NM_005163,UNIPROT:P31749,)
RID: 55792 (;Positive influence'):
  Reactants: PPARA (formerSymbols: PPAR) (annotations: HGNC_SYMBOL:PPARA,ENTREZ:5465,REFSEQ:NM_001001928,,PUBMED:26451809,UNIPROT:Q07869,HGNC:9232)
  Products: HSD17B10 (formerSymbols: HADH2,MRXS10) (annotations: HGNC_SYMBOL:HSD17B10,,UNIPROT:Q99714,REFSEQ:NM_004493,HGNC:4800,ENTREZ:3028)
  Modifiers: None
RID: 55246 (PDmap:re240.0;Positive influence'):
  Reactants: hydrogen peroxide (annotations: PUBCHEM:784,HMDB:HMDB0003125,KEGG_COMPOUND:C00027,MESH_2012:D006861,CHEBI:CHEBI:16240,WIKIPEDIA:Hydrogen peroxide,CAS:7722-84-1,CHEMBL_COMPOUND:CHEMBL71595,CHEMSPIDER:763)
  Products: ROS (annotations: CHEBI:CHEBI:26523)
  Modifiers: None
  (References: PUBMED:20045723)
RID: 55219 (;Known transition omitted'):
  Reactants: ACSL3 (formerSymbols: FACL3) (annotations: REFSEQ:NM_004457,ENTREZ:2181,UNIPROT:O95573,,HGNC_SYMBOL:ACSL3,HGNC:3570)
  Products: Fatty Acid Biosynthesis (annotations: WIKIPATHWAYS:WP4491,GO:GO:0006633)
  Modifiers: None
RID: 56024 (;Positive influence'):
  Reactants: CPT1A (formerSymbols: CPT1) (annotations: UNIPROT:P50416,PUBMED:19595610,HGNC_SYMBOL:CPT1A,HGNC:2328,ENTREZ:1374,REFSEQ:NM_001876,)
  Products: Mitochondrial Beta-Oxidation (annotations: WIKIPATHWAYS:WP143)
  Modifiers: None
RID: 56012 (;Known transition omitted'):
  Reactants: UDP-Glucose (annotations: CHEBI:CHEBI:18066); Galactose-1-Phosphate (annotations: CHEBI:CHEBI:17973)
  Products: Glucose-1-Phosphate (annotations: CHEBI:CHEBI:29042); UDP-Galactose (annotations: CHEBI:CHEBI:67119)
  Modifiers: GALT (annotations: REFSEQ:NM_000155,,HGNC:4135,HGNC_SYMBOL:GALT,ENTREZ:2592,UNIPROT:P07902)
RID: 56172 (;State transition'):
  Reactants: Fructose (annotations: CHEBI:CHEBI:28645,CHEBI:CHEBI:28757)
  Products: Fructose-6-Phosphate (annotations: CHEBI:CHEBI:15946,CHEBI:CHEBI:16084)
  Modifiers: HK1 (annotations: REFSEQ:NM_000188,,HGNC_SYMBOL:HK1,UNIPROT:P19367,HGNC:4922,ENTREZ:3098)
RID: 55757 (;Positive influence'):
  Reactants: INSIG1 (annotations: REFSEQ:NM_198336,PUBMED:19595610,,ENTREZ:3638,UNIPROT:O15503,HGNC_SYMBOL:INSIG1,HGNC:6083)
  Products: Negative Regulator of Cholesterol Biosynthesis
  Modifiers: None
RID: 55676 (;State transition'):
  Reactants: Phosphatidic Acid
  Products: Diacylglycerol
  Modifiers: LPIN1 (annotations: UNIPROT:Q14693,,ENTREZ:23175,REFSEQ:NM_145693,HGNC_SYMBOL:LPIN1,HGNC:13345)
RID: 55583 (;Positive influence'):
  Reactants: NR3C1 (formerSymbols: GRL) (annotations: HGNC_SYMBOL:NR3C1,REFSEQ:NM_000176,,HGNC:7978,ENTREZ:2908,PUBMED:26451809,UNIPROT:P04150)
  Products: Gluconeogenesis (annotations: GO:GO:0006094)
  Modifiers: None
RID: 55840 (;Positive influence'):
  Reactants: CYP7A1 (formerSymbols: CYP7) (annotations: HGNC:2651,,REFSEQ:NM_000780,ENTREZ:1581,HGNC_SYMBOL:CYP7A1,UNIPROT:P22680)
  Products: Cholesterol Metabolism (annotations: KEGG_PATHWAY:map04979)
  Modifiers: None
RID: 55098 (;State transition'):
  Reactants: Cholesterol (annotations: CHEBI:CHEBI:16113,KEGG_COMPOUND:C00187); Phospholipids (annotations: CHEBI:CHEBI:16247); APOA1 (annotations: HGNC:600,,UNIPROT:P02647,ENTREZ:335,REFSEQ:NM_000039,HGNC_SYMBOL:APOA1)
  Products: Nascent HDL (annotations: GO:GO:0034364)
  Modifiers: None
  (References: WIKIPATHWAYS:WP5304)
RID: 56151 (;State transition'):
  Reactants: GYS
  Products: GYS
  Modifiers: None
RID: 56039 (;Positive influence'):
  Reactants: CREB1 (annotations: REFSEQ:NM_134442,HGNC:2345,ENTREZ:1385,HGNC_SYMBOL:CREB1,UNIPROT:P16220,)
  Products: CREB1 (annotations: REFSEQ:NM_134442,HGNC:2345,ENTREZ:1385,HGNC_SYMBOL:CREB1,UNIPROT:P16220,)
  Modifiers: None
RID: 55866 (;State transition'):
  Reactants: Mevalonic acid (annotations: CHEBI:CHEBI:25351)
  Products: Mevalonate-P (annotations: CHEBI:CHEBI:25350)
  Modifiers: MVK (annotations: REFSEQ:NM_000431,HGNC_SYMBOL:MVK,HGNC:7530,ENTREZ:4598,,UNIPROT:Q03426)
  (References: DOI:10.1016/B978-0-12-824048-9.00005-5)
RID: 55240 (PDmap:re325.0;Positive influence'):
  Reactants: peroxide (annotations: CHEBI:CHEBI:44785)
  Products: ROS (annotations: CHEBI:CHEBI:26523)
  Modifiers: None
  (References: PUBMED:11304122)
RID: 56048 (;Unknown positive influence'):
  Reactants: PKA
  Products: AMPK (annotations: GO:GO:0031588)
  Modifiers: None
RID: 55366 (PDmap:re562.0;State transition'):
  Reactants: trans-2-octadecenoyl-CoA (annotations: CHEBI:CHEBI:50570,REACTOME:REACT_22862.1)
  Products: stearoyl-CoA (annotations: REACTOME:REACT_20205.2,CHEBI:CHEBI:15541,KEGG_COMPOUND:C00412,HMDB:HMDB0001114,PUBCHEM:439229,CHEMSPIDER:388366,CAS:362-66-3)
  Modifiers: TECR (formerSymbols: GPSN2,SC2) (annotations: HGNC:4551,REFSEQ:NM_138501,HGNC_SYMBOL:TECR,UNIPROT:Q9NZ01,,ENTREZ:9524)
  (References: REACTOME:REACT_22330.1)
RID: 55278 (PDmap:re424.0;State transition'):
  Reactants: complex II (annotations: GO:GO:0045281,REACTOME:REACT_3127.2,DOI:10.1021/bi901627u)
  Products: complex II (annotations: GO:GO:0045281,REACTOME:REACT_3127.2)
  Modifiers: complex II (annotations: GO:GO:0045281,REACTOME:REACT_3127.2,DOI:10.1021/bi901627u)
  (References: REACTOME:REACT_6360.4)
RID: 55997 (;Positive influence'):
  Reactants: PPARA (formerSymbols: PPAR) (annotations: HGNC_SYMBOL:PPARA,ENTREZ:5465,REFSEQ:NM_001001928,,PUBMED:26451809,UNIPROT:Q07869,HGNC:9232)
  Products: NR1H3 (annotations: REFSEQ:NM_001130101,,HGNC:7966,ENTREZ:10062,UNIPROT:Q13133,HGNC_SYMBOL:NR1H3)
  Modifiers: None
RID: 55158 (;Known transition omitted'):
  Reactants: Dihydro-T-MAS (annotations: CHEBI:CHEBI:87044)
  Products: Zymostenol (annotations: CHEBI:CHEBI:16608)
  Modifiers: MSMO1 (formerSymbols: SC4MOL) (annotations: REFSEQ:NM_006745,ENTREZ:6307,,HGNC:10545,UNIPROT:Q15800,HGNC_SYMBOL:MSMO1); NSDHL (annotations: ENTREZ:50814,HGNC:13398,HGNC_SYMBOL:NSDHL,REFSEQ:NM_015922,UNIPROT:Q15738,); HSD17B7 (annotations: ENTREZ:51478,UNIPROT:P56937,HGNC:5215,HGNC_SYMBOL:HSD17B7,REFSEQ:NM_016371,)
  (References: WIKIPATHWAYS:WP4718|DOI:10.1016/B978-0-12-824048-9.00005-5)
RID: 55810 (;Negative influence'):
  Reactants: PFKFB
  Products: Glycolysis (annotations: GO:GO:0061621)
  Modifiers: None
RID: 56143 (;State transition'):
  Reactants: Glycogen (n+1) (annotations: CHEBI:CHEBI:28087)
  Products: Glycogen (n) (annotations: CHEBI:CHEBI:28087); Glucose-1-Phosphate (annotations: CHEBI:CHEBI:29042)
  Modifiers: PYGL
  (References: WIKIPATHWAYS:WP500)
RID: 56097 (;State transition'):
  Reactants: NADH (annotations: CHEBI:CHEBI:16908)
  Products: NAD (annotations: CHEBI:CHEBI:15846); H+ (annotations: CHEBI:CHEBI:15378)
  Modifiers: Complex I
RID: 55624 (;State transition'):
  Reactants: 3-Oxohexanoyl-CoA (annotations: CHEBI:CHEBI:62418,CHEBI:CHEBI:27648)
  Products: Butanoyl-CoA (annotations: CHEBI:CHEBI:22954); Acetyl-CoA (annotations: CHEBI:CHEBI:15351,CHEBI:CHEBI:57288)
  Modifiers: Mitochondrial trifunctional enzyme
RID: 56140 (;State transition'):
  Reactants: Sorbitol (annotations: CHEBI:CHEBI:30911)
  Products: Fructose (annotations: CHEBI:CHEBI:28645,CHEBI:CHEBI:28757)
  Modifiers: SORD (annotations: ,REFSEQ:NM_003104,HGNC_SYMBOL:SORD,UNIPROT:Q00796,ENTREZ:6652,HGNC:11184)
RID: 55174 (;State transition'):
  Reactants: Acetoacetyl-CoA (annotations: CHEBI:CHEBI:15345)
  Products: HMG-CoA (annotations: CHEBI:CHEBI:11814)
  Modifiers: HMGCS1 (formerSymbols: HMGCS) (annotations: UNIPROT:Q01581,HGNC:5007,HGNC_SYMBOL:HMGCS1,,ENTREZ:3157,REFSEQ:NM_001098272)
  (References: WIKIPATHWAYS:WP4718|DOI:10.1016/B978-0-12-824048-9.00005-5)
RID: 55337 (;State transition'):
  Reactants: O2 (annotations: CHEBI:CHEBI:15379,KEGG_COMPOUND:C00007,HMDB:HMDB0001377,PUBCHEM:977,CHEMSPIDER:952,CAS:7782-44-7,WIKIPEDIA:Oxygen)
  Products: superoxide (annotations: HMDB:HMDB0002168,WIKIPEDIA:Superoxide,PUBCHEM:5359597,CHEMSPIDER:4514331,KEGG_COMPOUND:C00704,CHEBI:CHEBI:18421,CAS:11062-77-4)
  Modifiers: rotenone (annotations: CHEBI:CHEBI:28201)
  (References: PUBMED:15262965)
RID: 56213 (;State transition'):
  Reactants: Fructose-6-Phosphate (annotations: CHEBI:CHEBI:15946,CHEBI:CHEBI:16084)
  Products: Fructose-1,6-Bisphosphate (annotations: CHEBI:CHEBI:78682)
  Modifiers: PFKL (annotations: HGNC:8876,UNIPROT:P17858,PUBMED:31284506,REFSEQ:NM_001002021,,ENTREZ:5211,HGNC_SYMBOL:PFKL)
  (References: WIKIPATHWAYS:WP534)
RID: 55222 (;Known transition omitted'):
  Reactants: 7alpha-hydroxycholesterol (annotations: CHEBI:CHEBI:17500)
  Products: Bile (annotations: GO:GO:0006699)
  Modifiers: None
RID: 55630 (;Positive influence'):
  Reactants: PPARA (formerSymbols: PPAR) (annotations: HGNC_SYMBOL:PPARA,ENTREZ:5465,REFSEQ:NM_001001928,,PUBMED:26451809,UNIPROT:Q07869,HGNC:9232)
  Products: APOA5 (annotations: HGNC:17288,HGNC_SYMBOL:APOA5,UNIPROT:Q6Q788,,ENTREZ:116519,REFSEQ:NM_001166598)
  Modifiers: None
RID: 55801 (;State transition'):
  Reactants: Long-chain Fatty Acids; CoA (annotations: CHEBI:CHEBI:15346)
  Products: Fatty acyl-CoA
  Modifiers: ACSL
  (References: WIKIPATHWAYS:WP5061)
RID: 55956 (;State transition'):
  Reactants: Myristoyl-CoA (annotations: CHEBI:CHEBI:15532)
  Products: Trans-Tetradec-2-enoyl-CoA (annotations: CHEBI:CHEBI:27721)
  Modifiers: ACADL (annotations: ,REFSEQ:NM_001608,HGNC_SYMBOL:ACADL,HGNC:88,ENTREZ:33,UNIPROT:P28330)
RID: 55704 (;Positive influence'):
  Reactants: NFE2L2 (annotations: UNIPROT:Q16236,,PUBMED:28416361,ENTREZ:4780,REFSEQ:NM_006164,HGNC:7782,HGNC_SYMBOL:NFE2L2)
  Products: PGD (annotations: UNIPROT:P52209,HGNC_SYMBOL:PGD,REFSEQ:NM_002631,,HGNC:8891,ENTREZ:5226)
  Modifiers: None
RID: 55514 (;State transition'):
  Reactants: mTORC1 (annotations: GO:GO:0031931)
  Products: mTORC1 (annotations: GO:GO:0031931)
  Modifiers: TSC (annotations: PUBMED:28416361)
RID: 55521 (;Positive influence'):
  Reactants: FBP1 (formerSymbols: FBP) (annotations: HGNC_SYMBOL:FBP1,UNIPROT:P09467,REFSEQ:NM_000507,PUBMED:31284506,HGNC:3606,ENTREZ:2203,)
  Products: Gluconeogenesis
  Modifiers: None
RID: 55210 (;State transition'):
  Reactants: Cholestadienol (annotations: CHEBI:CHEBI:145214)
  Products: 7-Dehydrodemosterol (annotations: CHEBI:CHEBI:27910)
  Modifiers: SC5D (formerSymbols: SC5DL) (annotations: ENTREZ:6309,HGNC:10547,HGNC_SYMBOL:SC5D,REFSEQ:NM_001024956,,UNIPROT:O75845)
  (References: WIKIPATHWAYS:WP4718|DOI:10.1016/B978-0-12-824048-9.00005-5)
RID: 55758 (;Positive influence'):
  Reactants: ACAA1 (annotations: HGNC_SYMBOL:ACAA1,,REFSEQ:NM_001607,HGNC:82,ENTREZ:30,UNIPROT:P09110)
  Products: Peroxisomal Beta-Oxidation (annotations: WIKIPATHWAYS:WP1941)
  Modifiers: None
RID: 55354 (PDmap:re471.0;State transition'):
  Reactants: acetoacetate (annotations: CAS:541-50-4,CHEBI:CHEBI:15344,CHEMBL_COMPOUND:CHEMBL1230762,WIKIPEDIA:Acetoacetic acid,PUBCHEM:96,REACTOME:REACT_5224.1,CHEMSPIDER:94,HMDB:HMDB0000060,KEGG_COMPOUND:C00164)
  Products: (R)-3-hydroxybutyrate (annotations: CHEBI:CHEBI:10983)
  Modifiers: BDH1 (formerSymbols: BDH) (annotations: HGNC_SYMBOL:BDH1,ENTREZ:622,,HGNC:1027,UNIPROT:Q02338,REFSEQ:NM_004051)
  (References: REACTOME:REACT_631.3|REACTOME:REACT_1493.4)
RID: 55312 (;Positive influence'):
  Reactants: SLC25A12 (annotations: ,HGNC_SYMBOL:SLC25A12,HGNC:10982,REFSEQ:NM_003705,ENTREZ:8604,UNIPROT:O75746)
  Products: malate-aspartate shuttle (annotations: GO:GO:0043490)
  Modifiers: None
  (References: PUBMED:23986233|PUBMED:25809592|PUBMED:23216354|PUBMED:16368075)
RID: 55456 (PDmap:re842.0;Transport'):
  Reactants: ADP (annotations: HMDB:HMDB0001341,WIKIPEDIA:ADP,CAS:58-64-0,KEGG_COMPOUND:C00008,PUBCHEM:6022,CHEBI:CHEBI:16761,CHEMBL_COMPOUND:CHEMBL14830,CHEMSPIDER:5800)
  Products: ADP (annotations: HMDB:HMDB0001341,WIKIPEDIA:ADP,CAS:58-64-0,KEGG_COMPOUND:C00008,PUBCHEM:6022,CHEBI:CHEBI:16761,CHEMBL_COMPOUND:CHEMBL14830,CHEMSPIDER:5800)
  Modifiers: SLC25A6 (formerSymbols: ANT3) (annotations: HGNC_SYMBOL:SLC25A6,UNIPROT:P12236,,HGNC:10992,REFSEQ:NM_001636,ENTREZ:293); SLC25A4 (formerSymbols: ANT1,PEO2,PEO3) (annotations: ENTREZ:291,,REFSEQ:NM_001151,HGNC_SYMBOL:SLC25A4,UNIPROT:P12235,HGNC:10990); SLC25A5 (formerSymbols: ANT2) (annotations: UNIPROT:P05141,ENTREZ:292,,REFSEQ:NM_001152,HGNC_SYMBOL:SLC25A5,HGNC:10991)
  (References: PUBMED:18021939|REACTOME:REACT_9306.2)
RID: 56111 (;Positive influence'):
  Reactants: PPARG:PPARGC1A
  Products: G6PC (annotations: PUBMED:28416361,)
  Modifiers: None
RID: 55906 (;Positive influence'):
  Reactants: GSK3B (annotations: HGNC_SYMBOL:GSK3B,ENTREZ:2932,PUBMED:28416361,,HGNC:4617,UNIPROT:P49841,REFSEQ:NM_001146156)
  Products: Apoptosis (annotations: GO:GO:1900117,GO:GO:0097194)
  Modifiers: None
RID: 56021 (;Positive influence'):
  Reactants: BAD (annotations: REFSEQ:NM_032989,UNIPROT:Q92934,ENTREZ:572,,HGNC_SYMBOL:BAD,HGNC:936)
  Products: Apoptosis (annotations: GO:GO:1900117,GO:GO:0097194)
  Modifiers: None
RID: 55163 (;Positive influence'):
  Reactants: Cholesterol (annotations: CHEBI:CHEBI:16113,KEGG_COMPOUND:C00187)
  Products: Steroid synthesis (annotations: GO:GO:0006694)
  Modifiers: None
RID: 55394 (PDmap:re526.0;State transition'):
  Reactants: octanoyl-CoA (annotations: CHEBI:CHEBI:15533,KEGG_COMPOUND:C01944,CHEMSPIDER:371,PUBCHEM:380,HMDB:HMDB0001070,REACTOME:REACT_5128.1,WIKIPEDIA:octanoyl-Coenzyme A,CAS:1264-52-4)
  Products: trans-oct-2-enoyl-CoA (annotations: CHEBI:CHEBI:27537,REACTOME:REACT_5037.1)
  Modifiers: ACADM (annotations: UNIPROT:P11310,HGNC_SYMBOL:ACADM,,HGNC:89,REFSEQ:NM_000016,ENTREZ:34)
  (References: REACTOME:REACT_442.2|PUBMED:13295225|PUBMED:3597357)
RID: 55818 (;Positive influence'):
  Reactants: GCG (annotations: HGNC_SYMBOL:GCG,,REFSEQ:NM_002054,HGNC:4191,UNIPROT:P01275,ENTREZ:2641)
  Products: FBP1 (formerSymbols: FBP) (annotations: HGNC_SYMBOL:FBP1,UNIPROT:P09467,REFSEQ:NM_000507,PUBMED:31284506,HGNC:3606,ENTREZ:2203,)
  Modifiers: None
RID: 55311 (PDmap:re390.0;State transition'):
  Reactants: 2-oxoglutaric acid (annotations: KEGG_COMPOUND:C00026,REACTOME:REACT_3871.1,CHEBI:CHEBI:30915,CAS:328-50-7,MESH_2012:C029743,PUBCHEM:51,CHEMSPIDER:50,HMDB:HMDB0000208,WIKIPEDIA:Alpha-Ketoglutaric_acid); 4-hydroxybutyrate (annotations: CAS:591-81-1,CHEBI:CHEBI:16724,KEGG_COMPOUND:C00989,REACTOME:REACT_26786.1,HMDB:HMDB0015507,CHEMSPIDER:2300886,WIKIPEDIA:Gamma-Hydroxybutyric_acid,MESH_2012:C111420,PUBCHEM:3037032)
  Products: (S)-2-hydroxyglutaric acid (annotations: REACTOME:REACT_25542.1,CHEBI:CHEBI:32797); succinic semialdehyde (annotations: CHEMSPIDER:1080,WIKIPEDIA:Succinic semialdehyde,CHEBI:CHEBI:16265,CAS:692-29-5,HMDB:HMDB0001259,PUBCHEM:1112,REACTOME:REACT_24442.1,KEGG_COMPOUND:C00232)
  Modifiers: ADHFE1 (annotations: HGNC:16354,UNIPROT:Q8IWW8,ENTREZ:137872,REFSEQ:NM_144650,HGNC_SYMBOL:ADHFE1,)
  (References: REACTOME:REACT_25102.2|PUBMED:16435184|PUBMED:3182820)
RID: 56115 (;State transition'):
  Reactants: Mannose (annotations: CHEBI:CHEBI:37684)
  Products: Mannose-6-Phosphate (annotations: CHEBI:CHEBI:17369)
  Modifiers: HK1 (annotations: REFSEQ:NM_000188,,HGNC_SYMBOL:HK1,UNIPROT:P19367,HGNC:4922,ENTREZ:3098)
RID: 55099 (;Known transition omitted'):
  Reactants: Cholesterol Biosynthesis (annotations: GO:GO:0006695)
  Products: Cholesterol (annotations: CHEBI:CHEBI:16113,KEGG_COMPOUND:C00187)
  Modifiers: None
RID: 55435 (PDmap:re463.0;State transition'):
  Reactants: pyruvate (annotations: REACTOME:REACT_3219.1,CHEBI:CHEBI:15361); ATP (annotations: CHEBI:CHEBI:15422,PUBCHEM:5957,CAS:56-65-5,MESH_2012:D000255,CHEMBL_COMPOUND:CHEMBL14249,CHEMSPIDER:5742,WIKIPEDIA:Adenosine triphosphate,HMDB:HMDB0000538,KEGG_COMPOUND:C00002); CO2 (annotations: CHEMSPIDER:274,CHEBI:CHEBI:16526,MESH_2012:D002245,CHEMBL_COMPOUND:CHEMBL1231871,PUBCHEM:280,WIKIPEDIA:Carbon Dioxide,HMDB:HMDB0001967,KEGG_COMPOUND:C00011,CAS:124-38-9)
  Products: oxaloacetate(2-) (annotations: PUBCHEM:970,CHEBI:CHEBI:30744,KEGG_COMPOUND:C00036,CAS:328-42-7,HMDB:HMDB0000223,CHEMSPIDER:945,REACTOME:REACT_5376.1,CHEBI:CHEBI:16452,WIKIPEDIA:Oxalacetic acid); ADP (annotations: HMDB:HMDB0001341,WIKIPEDIA:ADP,CAS:58-64-0,KEGG_COMPOUND:C00008,PUBCHEM:6022,CHEBI:CHEBI:16761,CHEMBL_COMPOUND:CHEMBL14830,CHEMSPIDER:5800); phosphate(3-) (annotations: WIKIPEDIA:Phosphate,PUBCHEM:1061,CAS:14265-44-2,KEGG_COMPOUND:C00009,CHEMSPIDER:1032,CHEBI:CHEBI:18367,REACTOME:REACT_5781.1,HMDB:HMDB0001429)
  Modifiers: PC
  (References: REACTOME:REACT_1895.4)
RID: 55545 (;Positive influence'):
  Reactants: INS (formerSymbols: IDDM1,IDDM2) (annotations: HGNC_SYMBOL:INS,PUBMED:28416361,HGNC:6081,REFSEQ:NM_000207,ENTREZ:3630,,UNIPROT:P01308)
  Products: AKT1 (annotations: ENTREZ:207,HGNC:391,PUBMED:28416361,HGNC_SYMBOL:AKT1,REFSEQ:NM_005163,UNIPROT:P31749,)
  Modifiers: None
RID: 55870 (;Positive influence'):
  Reactants: Complex II
  Products: Ubiquinone (annotations: CHEBI:CHEBI:16389)
  Modifiers: None
RID: 55824 (;State transition'):
  Reactants: Long-chain Fatty Acids
  Products: Fatty Omega-hydrocyacid
  Modifiers: CYP450
  (References: WIKIPATHWAYS:WP206)
RID: 55953 (;State transition'):
  Reactants: PFKFB
  Products: PFKFB
  Modifiers: PKA
RID: 55261 (;State transition'):
  Reactants: malonyl-ACP (annotations: CHEBI:CHEBI:17330)
  Products: acetoacetyl-ACP
  Modifiers: FASN (annotations: HGNC:3594,UNIPROT:P49327,REFSEQ:NM_004104,,ENTREZ:2194,HGNC_SYMBOL:FASN)
  (References: WIKIPATHWAYS:WP357)
RID: 55533 (;Positive influence'):
  Reactants: PPARG:PPARGC1A
  Products: PCK1 (annotations: ,PUBMED:28416361,HGNC:8724,UNIPROT:P35558,HGNC_SYMBOL:PCK1,REFSEQ:NM_002591,ENTREZ:5105)
  Modifiers: None
RID: 55976 (;Known transition omitted'):
  Reactants: NR1I3 (annotations: ENTREZ:9970,UNIPROT:Q14994,,HGNC:7969,PUBMED:26451809,REFSEQ:NM_001077469,HGNC_SYMBOL:NR1I3)
  Products: NR1I3 (annotations: ENTREZ:9970,UNIPROT:Q14994,,HGNC:7969,REFSEQ:NM_001077469,HGNC_SYMBOL:NR1I3)
  Modifiers: None
RID: 56133 (;State transition'):
  Reactants: PKLR (annotations: HGNC_SYMBOL:PKLR,REFSEQ:NM_000298,PUBMED:31284506,HGNC:9020,UNIPROT:P30613,ENTREZ:5313,)
  Products: PKLR (annotations: HGNC_SYMBOL:PKLR,REFSEQ:NM_000298,HGNC:9020,UNIPROT:P30613,ENTREZ:5313,)
  Modifiers: None
RID: 55329 (;State transition'):
  Reactants: TXN (annotations: ENTREZ:7295,UNIPROT:P10599,HGNC:12435,,REFSEQ:NM_001244938,HGNC_SYMBOL:TXN); hydrogen peroxide (annotations: PUBCHEM:784,HMDB:HMDB0003125,KEGG_COMPOUND:C00027,MESH_2012:D006861,CHEBI:CHEBI:16240,WIKIPEDIA:Hydrogen peroxide,CAS:7722-84-1,CHEMBL_COMPOUND:CHEMBL71595,CHEMSPIDER:763)
  Products: hC TXN:hC TXN; H2O (annotations: HMDB:HMDB0002111,CHEBI:CHEBI:15377,PUBCHEM:962,CHEMSPIDER:937,MESH_2012:D014867,WIKIPEDIA:Water,CAS:7732-18-5,CHEMBL_COMPOUND:CHEMBL1098659,KEGG_COMPOUND:C00001)
  Modifiers: PRDX1 (formerSymbols: PAGA) (annotations: UNIPROT:Q06830,REFSEQ:NM_181697,ENTREZ:5052,HGNC:9352,,HGNC_SYMBOL:PRDX1); PRDX2 (formerSymbols: TDPX1) (annotations: ENTREZ:7001,REFSEQ:NM_005809,UNIPROT:P32119,,HGNC:9353,HGNC_SYMBOL:PRDX2); PRDX5 (annotations: UNIPROT:P30044,REFSEQ:NM_181651,,HGNC_SYMBOL:PRDX5,HGNC:9355,ENTREZ:25824)
  (References: REACTOME:REACT_264249)
RID: 55915 (;State transition'):
  Reactants: Acyl-CoA (annotations: CHEBI:CHEBI:17984)
  Products: Enoyl-CoA (annotations: CHEBI:CHEBI:27537)
  Modifiers: ACAD (annotations: HGNC_SYMBOL:ACAD,HGNC:86)
RID: 55443 (PDmap:re363.0;State transition'):
  Reactants: ubiquinol (annotations: CHEBI:CHEBI:17976); CYCS (annotations: HGNC:19986,UNIPROT:P99999,ENTREZ:54205,HGNC_SYMBOL:CYCS,,REFSEQ:NM_018947); H+ (annotations: CHEBI:CHEBI:15378); Dioxygen (annotations: CHEBI:CHEBI:15379)
  Products: ubiquinone (annotations: CHEMBL_COMPOUND:CHEMBL454801,HMDB:HMDB0002012,KEGG_COMPOUND:C00399,MESH_2012:D014451,CHEMSPIDER:4307,PUBCHEM:4462,CAS:727-81-1,WIKIPEDIA:Ubiquinone,CHEBI:CHEBI:16389); CYCS (annotations: HGNC:19986,UNIPROT:P99999,ENTREZ:54205,HGNC_SYMBOL:CYCS,,REFSEQ:NM_018947); H+ (annotations: CHEBI:CHEBI:15378); Oxide(2−) (annotations: CHEBI:CHEBI:29356)
  Modifiers: complex III (annotations: GO:GO:0045275); CHCHD2:GHITM:CYCS
  (References: PUBMED:25991374|PUBMED:19427899|PUBMED:28589937|REACTOME:REACT_6300.1)
RID: 55584 (;State transition'):
  Reactants: Enoyl-CoA (annotations: CHEBI:CHEBI:27537)
  Products: Hydroxyacyl-CoA (annotations: CHEBI:CHEBI:65260)
  Modifiers: EHHADH (formerSymbols: ECHD) (annotations: ENTREZ:1962,UNIPROT:Q08426,,HGNC:3247,HGNC_SYMBOL:EHHADH,REFSEQ:NM_001166415)
RID: 55403 (PDmap:re95.0;State transition'):
  Reactants: paraquat dication
  Products: paraquat monocation radical
  Modifiers: complex I (annotations: GO:GO:0005747); superoxide (annotations: HMDB:HMDB0002168,WIKIPEDIA:Superoxide,PUBCHEM:5359597,CHEMSPIDER:4514331,KEGG_COMPOUND:C00704,CHEBI:CHEBI:18421,CAS:11062-77-4)
  (References: PUBMED:18039652)
RID: 55650 (;State transition'):
  Reactants: CASP9 (annotations: HGNC_SYMBOL:CASP9,REFSEQ:NM_032996,ENTREZ:842,,HGNC:1511,UNIPROT:P55211)
  Products: CASP9 (annotations: HGNC_SYMBOL:CASP9,REFSEQ:NM_032996,ENTREZ:842,,HGNC:1511,UNIPROT:P55211)
  Modifiers: AKT1 (annotations: ENTREZ:207,HGNC:391,PUBMED:28416361,HGNC_SYMBOL:AKT1,REFSEQ:NM_005163,UNIPROT:P31749,)
RID: 56169 (;Truncation'):
  Reactants: Citrate (annotations: CHEBI:CHEBI:16947,CHEBI:CHEBI:133748,CHEBI:CHEBI:50744)
  Products: Acetyl-CoA (annotations: CHEBI:CHEBI:15351,CHEBI:CHEBI:57288); Oxalacetate (annotations: CHEBI:CHEBI:16452)
  Modifiers: ACLY (annotations: HGNC:115,REFSEQ:NM_001096,,ENTREZ:47,HGNC_SYMBOL:ACLY,UNIPROT:P53396)
RID: 56135 (;Known transition omitted'):
  Reactants: 2,3-Bisphosphoglycerate (annotations: CHEBI:CHEBI:19324)
  Products: 3-Phosphoglycerate (annotations: CHEBI:CHEBI:17050,CHEBI:CHEBI:17794,CHEBI:CHEBI:57998)
  Modifiers: None
RID: 55385 (PDmap:re362.0;State transition'):
  Reactants: NADH (annotations: REACTOME:REACT_2390.1,KEGG_COMPOUND:C00004,HMDB:HMDB0001487,CHEMSPIDER:903,WIKIPEDIA:NADH,CAS:58-68-4,CHEBI:CHEBI:16908,PUBCHEM:928,CHEMBL_COMPOUND:CHEMBL1628272,MESH_2012:D009243); ubiquinone (annotations: CHEMBL_COMPOUND:CHEMBL454801,HMDB:HMDB0002012,KEGG_COMPOUND:C00399,MESH_2012:D014451,CHEMSPIDER:4307,PUBCHEM:4462,CAS:727-81-1,WIKIPEDIA:Ubiquinone,CHEBI:CHEBI:16389); H+ (annotations: CHEBI:CHEBI:15378)
  Products: NAD(+) (annotations: KEGG_COMPOUND:C00003,CAS:53-84-9,PUBCHEM:5893,CHEMSPIDER:5682,REACTOME:REACT_4970.1,CHEBI:CHEBI:15846,HMDB:HMDB0000902,WIKIPEDIA:NAD); H+ (annotations: CHEBI:CHEBI:15378); ubiquinol (annotations: CHEBI:CHEBI:17976); e-
  Modifiers: complex I (annotations: GO:GO:0005747); SNCA (formerSymbols: PARK1,PARK4) (annotations: HGNC:11138,,HGNC_SYMBOL:SNCA,REFSEQ:NM_000345,UNIPROT:P37840,ENTREZ:6622); SNCA (formerSymbols: PARK1,PARK4) (annotations: HGNC:11138,,HGNC_SYMBOL:SNCA,REFSEQ:NM_000345,UNIPROT:P37840,ENTREZ:6622)
  (References: PUBMED:18245082|PUBMED:19427899|PUBMED:20053987|PUBMED:20887775)
RID: 55940 (;State transition'):
  Reactants: Protein kinase cAMP-activated (PKA); cAMP (annotations: CHEBI:CHEBI:17489)
  Products: Protein kinase cAMP-activated (PKA); PKA; PKA
  Modifiers: None
RID: 55270 (PDmap:re425.0;State transition'):
  Reactants: succinic acid (annotations: KEGG_COMPOUND:C19806,CHEBI:CHEBI:45969,WIKIPEDIA:1,2,3-Propanetricarboxylic_acid,CHEBI:CHEBI:15741,PUBCHEM:14925,HMDB:HMDB0031193,REACTOME:REACT_2775.1,CAS:99-14-9,CHEMSPIDER:14220); complex II (annotations: GO:GO:0045281,REACTOME:REACT_3127.2)
  Products: fumaric acid (annotations: REACTOME:REACT_5289.1,CHEBI:CHEBI:29806); complex II (annotations: GO:GO:0045281,REACTOME:REACT_3127.2,DOI:10.1021/bi901627u)
  Modifiers: complex II (annotations: GO:GO:0045281,REACTOME:REACT_3127.2,DOI:10.1021/bi901627u)
  (References: REACTOME:REACT_1667.6|PUBMED:16143825)
RID: 55823 (;Known transition omitted'):
  Reactants: LDL
  Products: LP(a)
  Modifiers: None
RID: 56010 (;State transition'):
  Reactants: Fatty Omega-hydrocyacid
  Products: Fatty Omega-aldoacid
  Modifiers: ADH
  (References: WIKIPATHWAYS:WP206)
RID: 55816 (;Positive influence'):
  Reactants: CD36 (annotations: HGNC:1663,REFSEQ:NM_001001547,HGNC_SYMBOL:CD36,PUBMED:26451809,ENTREZ:948,,UNIPROT:P16671,PUBMED:18477307)
  Products: Fatty Acid Transport (annotations: WIKIPATHWAYS:WP5061)
  Modifiers: None
RID: 56125 (;State transition'):
  Reactants: (S)-methylmalonyl-CoA (annotations: CHEBI:CHEBI:15466,CHEBI:CHEBI:57327)
  Products: (R)-methylmalonyl-CoA (annotations: CHEBI:CHEBI:15465,CHEBI:CHEBI:57326)
  Modifiers: MCEE (annotations: ENTREZ:84693,,REFSEQ:NM_032601,HGNC:16732,HGNC_SYMBOL:MCEE,UNIPROT:Q96PE7)
RID: 55739 (;Truncation'):
  Reactants: Fructose-1-Phosphate (annotations: CHEBI:CHEBI:18105)
  Products: Dihydroxyacetone-Phosphate (annotations: CHEBI:CHEBI:16108); Glyceraldehyde (annotations: CHEBI:CHEBI:5445,CHEBI:CHEBI:17378)
  Modifiers: ALDOB (annotations: ENTREZ:229,REFSEQ:NM_000035,HGNC:417,,HGNC_SYMBOL:ALDOB,UNIPROT:P05062)
RID: 55617 (;Positive influence'):
  Reactants: SREBF1 (annotations: PUBMED:28416361,UNIPROT:P36956,REFSEQ:NM_004176,ENTREZ:6720,HGNC:11289,HGNC_SYMBOL:SREBF1,)
  Products: Lipogenesis (annotations: GO:GO:0008610)
  Modifiers: None
RID: 55851 (;State transition'):
  Reactants: Zymosterol (annotations: CHEBI:CHEBI:18252)
  Products: Cholestadienol (annotations: CHEBI:CHEBI:145214)
  Modifiers: EBP (formerSymbols: CDPX2) (annotations: ENTREZ:10682,REFSEQ:NM_006579,HGNC:3133,UNIPROT:Q15125,HGNC_SYMBOL:EBP,)
  (References: DOI:10.1016/B978-0-12-824048-9.00005-5)
RID: 55382 (PDmap:re577.0;State transition'):
  Reactants: hydrogen peroxide (annotations: PUBCHEM:784,HMDB:HMDB0003125,KEGG_COMPOUND:C00027,MESH_2012:D006861,CHEBI:CHEBI:16240,WIKIPEDIA:Hydrogen peroxide,CAS:7722-84-1,CHEMBL_COMPOUND:CHEMBL71595,CHEMSPIDER:763)
  Products: H2O (annotations: HMDB:HMDB0002111,CHEBI:CHEBI:15377,PUBCHEM:962,CHEMSPIDER:937,MESH_2012:D014867,WIKIPEDIA:Water,CAS:7732-18-5,CHEMBL_COMPOUND:CHEMBL1098659,KEGG_COMPOUND:C00001); O2 (annotations: CHEBI:CHEBI:15379,KEGG_COMPOUND:C00007,HMDB:HMDB0001377,PUBCHEM:977,CHEMSPIDER:952,CAS:7782-44-7,WIKIPEDIA:Oxygen)
  Modifiers: CAT (annotations: REFSEQ:NM_001752,ENTREZ:847,,HGNC_SYMBOL:CAT,HGNC:1516,UNIPROT:P04040)
  (References: PUBMED:20558743|PUBMED:19427899)
RID: 55299 (PDmap:re537.0;State transition'):
  Reactants: (R)-methylmalonyl-CoA (annotations: CHEBI:CHEBI:15465,REACTOME:REACT_5502.1)
  Products: succinyl-CoA (annotations: HMDB:HMDB0001022,CHEMSPIDER:388307,KEGG_COMPOUND:C00091,WIKIPEDIA:Succinyl-CoA,REACTOME:REACT_2852.1,CAS:604-98-8,CHEBI:CHEBI:15380,PUBCHEM:439161)
  Modifiers: MMAA dimer
  (References: REACTOME:REACT_19.5)
RID: 55387 (;Transcription'):
  Reactants: mt DNA (annotations: GO:GO:0000262)
  Products: mt mRNA (annotations: CHEBI:CHEBI:33699)
  Modifiers: TFAM (formerSymbols: TCF6,TCF6L2) (annotations: REFSEQ:NM_003201,HGNC:11741,HGNC_SYMBOL:TFAM,UNIPROT:Q00059,,ENTREZ:7019); MT transcription (annotations: PUBMED:18391175); damaged mt DNA
  (References: PUBMED:23149385|TAXONOMY:10090|TAXONOMY:4891|DOI:10.1101/gad.316547.118)
RID: 55151 (;Transcription'):
  Reactants: HMGCS2 (annotations: UNIPROT:P54868,HGNC:5008,HGNC_SYMBOL:HMGCS2,ENTREZ:3158,,REFSEQ:NM_005518)
  Products: HMGCS2 (annotations: UNIPROT:P54868,HGNC:5008,HGNC_SYMBOL:HMGCS2,ENTREZ:3158,,REFSEQ:NM_005518)
  Modifiers: SREBF2 (annotations: HGNC:11290,REFSEQ:NM_004599,UNIPROT:Q12772,,HGNC_SYMBOL:SREBF2,ENTREZ:6721)
  (References: WIKIPATHWAYS:WP4718)
RID: 55505 (;Negative influence'):
  Reactants: ROCK (annotations: ,ENTREZ:9475,HGNC:10252,HGNC_SYMBOL:ROCK2,REFSEQ:NM_001321643,UNIPROT:O75116)
  Products: AKT1 (annotations: ENTREZ:207,HGNC:391,PUBMED:28416361,HGNC_SYMBOL:AKT1,REFSEQ:NM_005163,UNIPROT:P31749,)
  Modifiers: None
RID: 55873 (;State transition'):
  Reactants: Sorbitol (annotations: CHEBI:CHEBI:30911)
  Products: Fructose (annotations: CHEBI:CHEBI:28645,CHEBI:CHEBI:28757)
  Modifiers: SORD (annotations: ,REFSEQ:NM_003104,HGNC_SYMBOL:SORD,UNIPROT:Q00796,ENTREZ:6652,HGNC:11184)
RID: 55548 (;Positive influence'):
  Reactants: CREB1 (annotations: REFSEQ:NM_134442,HGNC:2345,ENTREZ:1385,HGNC_SYMBOL:CREB1,UNIPROT:P16220,)
  Products: Glucose metabolism
  Modifiers: None
RID: 55355 (PDmap:re615.0;State transition'):
  Reactants: prostaglandin H2 (annotations: CHEBI:CHEBI:15554,WIKIPEDIA:Prostaglandin H2,PUBCHEM:445049,KEGG_COMPOUND:C00427,CAS:42935-17-1,CHEMSPIDER:392800,HMDB:HMDB0001381)
  Products: prostaglandin E2 (annotations: HMDB:HMDB0001220,CHEBI:CHEBI:15551,CHEMSPIDER:4444059,CAS:363-24-6,PUBCHEM:5280360,WIKIPEDIA:Dinoprostone,KEGG_COMPOUND:C00584)
  Modifiers: PTGES2 (formerSymbols: C9orf15) (annotations: HGNC_SYMBOL:PTGES2,UNIPROT:Q9H7Z7,HGNC:17822,,REFSEQ:NM_001256335,ENTREZ:80142); PTGES (formerSymbols: MGST1L1) (annotations: HGNC:9599,HGNC_SYMBOL:PTGES,,UNIPROT:O14684,ENTREZ:9536,REFSEQ:NM_004878); PTGES3 (annotations: REFSEQ:NM_006601,,UNIPROT:Q15185,HGNC:16049,ENTREZ:10728,HGNC_SYMBOL:PTGES3)
  (References: PUBMED:11729303|PUBMED:18307977)
RID: 55293 (PDmap:re389.0;State transition'):
  Reactants: (S)-2-hydroxyglutaric acid (annotations: REACTOME:REACT_25542.1,CHEBI:CHEBI:32797); succinic semialdehyde (annotations: CHEMSPIDER:1080,WIKIPEDIA:Succinic semialdehyde,CHEBI:CHEBI:16265,CAS:692-29-5,HMDB:HMDB0001259,PUBCHEM:1112,REACTOME:REACT_24442.1,KEGG_COMPOUND:C00232)
  Products: 2-oxoglutaric acid (annotations: KEGG_COMPOUND:C00026,REACTOME:REACT_3871.1,CHEBI:CHEBI:30915,CAS:328-50-7,MESH_2012:C029743,PUBCHEM:51,CHEMSPIDER:50,HMDB:HMDB0000208,WIKIPEDIA:Alpha-Ketoglutaric_acid); 4-hydroxybutyrate (annotations: CAS:591-81-1,CHEBI:CHEBI:16724,KEGG_COMPOUND:C00989,REACTOME:REACT_26786.1,HMDB:HMDB0015507,CHEMSPIDER:2300886,WIKIPEDIA:Gamma-Hydroxybutyric_acid,MESH_2012:C111420,PUBCHEM:3037032)
  Modifiers: ADHFE1 (annotations: HGNC:16354,UNIPROT:Q8IWW8,ENTREZ:137872,REFSEQ:NM_144650,HGNC_SYMBOL:ADHFE1,)
  (References: PUBMED:16435184|REACTOME:REACT_25041.2|PUBMED:3182820)
RID: 55936 (;Positive influence'):
  Reactants: NR1H3 (annotations: REFSEQ:NM_001130101,,HGNC:7966,ENTREZ:10062,UNIPROT:Q13133,HGNC_SYMBOL:NR1H3)
  Products: MLXIPL (formerSymbols: WBSCR14) (annotations: ,HGNC:12744,HGNC_SYMBOL:MLXIPL,REFSEQ:NM_032951,ENTREZ:51085,UNIPROT:Q9NP71)
  Modifiers: None
RID: 55343 (;Unknown transition'):
  Reactants: butyryl-ACP (annotations: CHEBI:CHEBI:3247)
  Products: malonyl-CoA (annotations: REACTOME:REACT_3059.1,WIKIPEDIA:Malonyl-CoA,HMDB:HMDB0001175,CAS:524-14-1,CHEBI:CHEBI:15531,PUBCHEM:10663,KEGG_COMPOUND:C00083,CHEMSPIDER:10213)
  Modifiers: None
  (References: WIKIPATHWAYS:WP357)
RID: 56054 (;State transition'):
  Reactants: FBP1 (formerSymbols: FBP) (annotations: HGNC_SYMBOL:FBP1,UNIPROT:P09467,REFSEQ:NM_000507,PUBMED:31284506,HGNC:3606,ENTREZ:2203,)
  Products: FBP1 (formerSymbols: FBP) (annotations: HGNC_SYMBOL:FBP1,UNIPROT:P09467,REFSEQ:NM_000507,PUBMED:31284506,HGNC:3606,ENTREZ:2203,)
  Modifiers: None
RID: 56167 (;State transition'):
  Reactants: Glucose-1-Phosphate (annotations: CHEBI:CHEBI:29042)
  Products: UDP-Glucose (annotations: CHEBI:CHEBI:18066)
  Modifiers: UGP2 (formerSymbols: UGP1) (annotations: HGNC_SYMBOL:UGP2,ENTREZ:7360,UNIPROT:Q16851,HGNC:12527,,REFSEQ:NM_006759)
  (References: WIKIPATHWAYS:WP500)
RID: 55834 (;Positive influence'):
  Reactants: PPARA (formerSymbols: PPAR) (annotations: HGNC_SYMBOL:PPARA,ENTREZ:5465,REFSEQ:NM_001001928,,PUBMED:26451809,UNIPROT:Q07869,HGNC:9232)
  Products: CYP4A11 (formerSymbols: CYP4A2) (annotations: ENTREZ:1579,HGNC:2642,UNIPROT:Q02928,REFSEQ:NM_000778,HGNC_SYMBOL:CYP4A11,)
  Modifiers: None
RID: 55837 (;Positive influence'):
  Reactants: FASN (annotations: HGNC:3594,UNIPROT:P49327,REFSEQ:NM_004104,,ENTREZ:2194,HGNC_SYMBOL:FASN)
  Products: Fatty Acid Synthesis (annotations: GO:GO:0005835)
  Modifiers: None
RID: 56116 (;State transition'):
  Reactants: Acetyl-ACP (annotations: CHEBI:CHEBI:2393)
  Products: Beta-ketoacyl-ACP
  Modifiers: None
RID: 55576 (;State transition'):
  Reactants: HMGCR (annotations: ,REFSEQ:NM_000859,UNIPROT:P04035,HGNC:5006,ENTREZ:3156,HGNC_SYMBOL:HMGCR)
  Products:  
  Modifiers: 24,25-Dihydrolanosterol (annotations: CHEBI:CHEBI:28113)
  (References: DOI:10.1016/B978-0-12-824048-9.00005-5)
RID: 55680 (;Positive influence'):
  Reactants: HNF4A (formerSymbols: MODY,MODY1,TCF14) (annotations: ,HGNC:5024,ENTREZ:3172,UNIPROT:P41235,HGNC_SYMBOL:HNF4A,REFSEQ:NM_000457)
  Products: PCK1 (annotations: ,PUBMED:28416361,HGNC:8724,UNIPROT:P35558,HGNC_SYMBOL:PCK1,REFSEQ:NM_002591,ENTREZ:5105)
  Modifiers: None
RID: 55279 (;State transition'):
  Reactants: superoxide (annotations: HMDB:HMDB0002168,WIKIPEDIA:Superoxide,PUBCHEM:5359597,CHEMSPIDER:4514331,KEGG_COMPOUND:C00704,CHEBI:CHEBI:18421,CAS:11062-77-4); H+ (annotations: CHEBI:CHEBI:15378)
  Products: O2 (annotations: CHEBI:CHEBI:15379,KEGG_COMPOUND:C00007,HMDB:HMDB0001377,PUBCHEM:977,CHEMSPIDER:952,CAS:7782-44-7,WIKIPEDIA:Oxygen); hydrogen peroxide (annotations: PUBCHEM:784,HMDB:HMDB0003125,KEGG_COMPOUND:C00027,MESH_2012:D006861,CHEBI:CHEBI:16240,WIKIPEDIA:Hydrogen peroxide,CAS:7722-84-1,CHEMBL_COMPOUND:CHEMBL71595,CHEMSPIDER:763)
  Modifiers: SOD1:Zn2+:Cu2+
  (References: REACTOME:REACT_264124|PUBMED:19427899)
RID: 56056 (;State transition'):
  Reactants: 6-Phosphogluconolactone (annotations: CHEBI:CHEBI:16938)
  Products: 6-Phosphogluconate (annotations: CHEBI:CHEBI:48928)
  Modifiers: PGLS (annotations: ENTREZ:25796,REFSEQ:NM_012088,,HGNC_SYMBOL:PGLS,UNIPROT:O95336,HGNC:8903)
RID: 55294 (;State transition'):
  Reactants:  
  Products: mt DNA (annotations: GO:GO:0000262)
  Modifiers: mt DNA damage; mt DNA replication
  (References: PUBMED:23149385|DOI:10.1101/gad.316547.118)
RID: 55171 (;State transition'):
  Reactants: 7-Dehydrocholesterol (annotations: CHEBI:CHEBI:17759)
  Products: Cholesterol (annotations: CHEBI:CHEBI:16113,KEGG_COMPOUND:C00187)
  Modifiers: DHCR7 (formerSymbols: SLOS) (annotations: HGNC:2860,REFSEQ:NM_001360,UNIPROT:Q9UBM7,HGNC_SYMBOL:DHCR7,ENTREZ:1717,)
  (References: DOI:10.1016/B978-0-12-824048-9.00005-5)
RID: 56035 (;Transport'):
  Reactants: H+ (annotations: CHEBI:CHEBI:15378)
  Products: H+ (annotations: CHEBI:CHEBI:15378)
  Modifiers: Complex III
RID: 55468 (;Positive influence'):
  Reactants: AKT1 (annotations: ENTREZ:207,HGNC:391,PUBMED:28416361,HGNC_SYMBOL:AKT1,REFSEQ:NM_005163,UNIPROT:P31749,)
  Products: CDKN1A (formerSymbols: CDKN1) (annotations: REFSEQ:NM_078467,UNIPROT:P38936,HGNC_SYMBOL:CDKN1A,,HGNC:1784,ENTREZ:1026)
  Modifiers: None
RID: 55324 (PDmap:re560.0;State transition'):
  Reactants: 3-oxooctadecanoyl-CoA (annotations: CHEBI:CHEBI:50571,REACTOME:REACT_22457.1)
  Products: 3-hydroxyoctadecanoyl-CoA (annotations: REACTOME:REACT_22804.1,CHEBI:CHEBI:50583)
  Modifiers: HSD17B12 (annotations: ENTREZ:51144,UNIPROT:Q53GQ0,HGNC_SYMBOL:HSD17B12,HGNC:18646,REFSEQ:NM_016142,)
  (References: PUBMED:12482854|REACTOME:REACT_22155.1)
RID: 55541 (;Positive influence'):
  Reactants: CREB1 (annotations: REFSEQ:NM_134442,HGNC:2345,ENTREZ:1385,HGNC_SYMBOL:CREB1,UNIPROT:P16220,)
  Products: PPARGC1A (formerSymbols: PPARGC1) (annotations: UNIPROT:Q9UBK2,ENTREZ:10891,HGNC:9237,HGNC_SYMBOL:PPARGC1A,,REFSEQ:NM_013261)
  Modifiers: None
RID: 56126 (;Positive influence'):
  Reactants: AHR (annotations: HGNC:348,HGNC_SYMBOL:AHR,,UNIPROT:P35869,REFSEQ:NM_001621,ENTREZ:196)
  Products: AHRR (formerSymbols: AHH,AHHR) (annotations: HGNC:346,,HGNC_SYMBOL:AHRR,REFSEQ:NM_020731,UNIPROT:A9YTQ3,ENTREZ:57491)
  Modifiers: None
RID: 56146 (;State transition'):
  Reactants: FBP1 (formerSymbols: FBP) (annotations: HGNC_SYMBOL:FBP1,UNIPROT:P09467,REFSEQ:NM_000507,PUBMED:31284506,HGNC:3606,ENTREZ:2203,)
  Products: FBP1 (formerSymbols: FBP) (annotations: HGNC_SYMBOL:FBP1,UNIPROT:P09467,REFSEQ:NM_000507,PUBMED:31284506,HGNC:3606,ENTREZ:2203,)
  Modifiers: None
RID: 55892 (;Positive influence'):
  Reactants: NR1H3 (annotations: REFSEQ:NM_001130101,,HGNC:7966,ENTREZ:10062,UNIPROT:Q13133,HGNC_SYMBOL:NR1H3)
  Products: CYP7A1 (formerSymbols: CYP7) (annotations: HGNC:2651,,REFSEQ:NM_000780,ENTREZ:1581,HGNC_SYMBOL:CYP7A1,UNIPROT:P22680)
  Modifiers: None
RID: 55778 (;State transition'):
  Reactants: 7-Dehydrocholesterol (annotations: CHEBI:CHEBI:17759)
  Products: Cholesterol (annotations: CHEBI:CHEBI:16113,KEGG_COMPOUND:C00187)
  Modifiers: DHCR7 (formerSymbols: SLOS) (annotations: HGNC:2860,REFSEQ:NM_001360,UNIPROT:Q9UBM7,HGNC_SYMBOL:DHCR7,ENTREZ:1717,)
  (References: DOI:10.1016/B978-0-12-824048-9.00005-5)
RID: 55606 (;Negative influence'):
  Reactants: NR1H3 (annotations: REFSEQ:NM_001130101,,HGNC:7966,ENTREZ:10062,UNIPROT:Q13133,HGNC_SYMBOL:NR1H3)
  Products: Fatty Acid Transport (annotations: WIKIPATHWAYS:WP5061)
  Modifiers: None
RID: 55623 (;State transition'):
  Reactants: 3-Oxooctanoyl-CoA (annotations: CHEBI:CHEBI:62619,CHEBI:CHEBI:28264); CoA (annotations: CHEBI:CHEBI:15346)
  Products: HX-CoA; Acetyl-CoA (annotations: CHEBI:CHEBI:15351,CHEBI:CHEBI:57288)
  Modifiers: Mitochondrial trifunctional enzyme
RID: 55419 (;State transition'):
  Reactants: beta-hydroxybutyryl
  Products: crotonoyl-ACP
  Modifiers: FASN (annotations: HGNC:3594,UNIPROT:P49327,REFSEQ:NM_004104,,ENTREZ:2194,HGNC_SYMBOL:FASN)
  (References: WIKIPATHWAYS:WP357)
RID: 56098 (;Negative influence'):
  Reactants: NR1I2 (annotations: ,HGNC_SYMBOL:NR1I2,HGNC:7968,REFSEQ:NM_003889,ENTREZ:8856,UNIPROT:O75469)
  Products: CREB1 (annotations: REFSEQ:NM_134442,HGNC:2345,ENTREZ:1385,HGNC_SYMBOL:CREB1,UNIPROT:P16220,)
  Modifiers: None
RID: 55422 (PDmap:re528.0;State transition'):
  Reactants: (S)-3-hydroxyoctanoyl-CoA (annotations: CHEBI:CHEBI:28632,REACTOME:REACT_2973.1)
  Products: 3-oxooctanoyl-CoA (annotations: REACTOME:REACT_4358.1,CHEBI:CHEBI:28264)
  Modifiers: HADH (formerSymbols: HADHSC) (annotations: HGNC_SYMBOL:HADH,REFSEQ:NM_005327,,HGNC:4799,ENTREZ:3033,UNIPROT:Q16836)
  (References: REACTOME:REACT_1908.2|PUBMED:8687463)
RID: 55595 (;Negative influence'):
  Reactants: NR1I2 (annotations: ,HGNC_SYMBOL:NR1I2,HGNC:7968,REFSEQ:NM_003889,ENTREZ:8856,UNIPROT:O75469)
  Products: PPARA (formerSymbols: PPAR) (annotations: HGNC_SYMBOL:PPARA,ENTREZ:5465,REFSEQ:NM_001001928,,PUBMED:26451809,UNIPROT:Q07869,HGNC:9232)
  Modifiers: None
RID: 55677 (;Positive influence'):
  Reactants: NR1I3 (annotations: ENTREZ:9970,UNIPROT:Q14994,,HGNC:7969,REFSEQ:NM_001077469,HGNC_SYMBOL:NR1I3)
  Products: PPARG (annotations: HGNC:9236,REFSEQ:NM_005037,HGNC_SYMBOL:PPARG,UNIPROT:P37231,ENTREZ:5468,)
  Modifiers: None
RID: 55671 (;State transition'):
  Reactants: Acetaldehyde (annotations: CHEBI:CHEBI:15343)
  Products: Ethanol (annotations: CHEBI:CHEBI:16236)
  Modifiers: ADH
RID: 55292 (PDmap:re843.0;Transport'):
  Reactants: ATP (annotations: CHEBI:CHEBI:15422,PUBCHEM:5957,CAS:56-65-5,MESH_2012:D000255,CHEMBL_COMPOUND:CHEMBL14249,CHEMSPIDER:5742,WIKIPEDIA:Adenosine triphosphate,HMDB:HMDB0000538,KEGG_COMPOUND:C00002)
  Products: ATP (annotations: CHEBI:CHEBI:15422,PUBCHEM:5957,CAS:56-65-5,MESH_2012:D000255,CHEMBL_COMPOUND:CHEMBL14249,CHEMSPIDER:5742,WIKIPEDIA:Adenosine triphosphate,HMDB:HMDB0000538,KEGG_COMPOUND:C00002)
  Modifiers: SLC25A6 (formerSymbols: ANT3) (annotations: HGNC_SYMBOL:SLC25A6,UNIPROT:P12236,,HGNC:10992,REFSEQ:NM_001636,ENTREZ:293); SLC25A4 (formerSymbols: ANT1,PEO2,PEO3) (annotations: ENTREZ:291,,REFSEQ:NM_001151,HGNC_SYMBOL:SLC25A4,UNIPROT:P12235,HGNC:10990); SLC25A5 (formerSymbols: ANT2) (annotations: UNIPROT:P05141,ENTREZ:292,,REFSEQ:NM_001152,HGNC_SYMBOL:SLC25A5,HGNC:10991)
  (References: PUBMED:18021939|REACTOME:REACT_9306.2)
RID: 55872 (;Positive influence'):
  Reactants: PPARG:PPARGC1A
  Products: CPT1
  Modifiers: None
RID: 55990 (;Positive influence'):
  Reactants: APOA4 (annotations: HGNC_SYMBOL:APOA4,REFSEQ:NM_000482,HGNC:602,ENTREZ:337,,UNIPROT:P06727)
  Products: Apolipoprotein Metabolism
  Modifiers: None
RID: 56067 (;State transition'):
  Reactants: Decanoyl-CoA (annotations: CHEBI:CHEBI:28493)
  Products: Trans-dec-2-enoyl-CoA (annotations: CHEBI:CHEBI:10723)
  Modifiers: ACADM (annotations: UNIPROT:P11310,HGNC_SYMBOL:ACADM,,HGNC:89,REFSEQ:NM_000016,ENTREZ:34)
RID: 55187 (;State transition'):
  Reactants: GPP (annotations: CHEBI:CHEBI:17211)
  Products: FAPP (annotations: CHEBI:CHEBI:50277)
  Modifiers: GGPS1 (annotations: ENTREZ:9453,UNIPROT:O95749,HGNC:4249,HGNC_SYMBOL:GGPS1,REFSEQ:NM_004837,); FDPS (annotations: REFSEQ:NM_002004,HGNC:3631,HGNC_SYMBOL:FDPS,UNIPROT:P14324,,ENTREZ:2224)
  (References: WIKIPATHWAYS:WP4718|DOI:10.1016/B978-0-12-824048-9.00005-5)
RID: 55255 (PDmap:re386.0;State transition'):
  Reactants: succinyl-CoA (annotations: HMDB:HMDB0001022,CHEMSPIDER:388307,KEGG_COMPOUND:C00091,WIKIPEDIA:Succinyl-CoA,REACTOME:REACT_2852.1,CAS:604-98-8,CHEBI:CHEBI:15380,PUBCHEM:439161); phosphate(3-) (annotations: WIKIPEDIA:Phosphate,PUBCHEM:1061,CAS:14265-44-2,KEGG_COMPOUND:C00009,CHEMSPIDER:1032,CHEBI:CHEBI:18367,REACTOME:REACT_5781.1,HMDB:HMDB0001429); ADP (annotations: HMDB:HMDB0001341,WIKIPEDIA:ADP,CAS:58-64-0,KEGG_COMPOUND:C00008,PUBCHEM:6022,CHEBI:CHEBI:16761,CHEMBL_COMPOUND:CHEMBL14830,CHEMSPIDER:5800)
  Products: succinic acid (annotations: KEGG_COMPOUND:C19806,CHEBI:CHEBI:45969,WIKIPEDIA:1,2,3-Propanetricarboxylic_acid,CHEBI:CHEBI:15741,PUBCHEM:14925,HMDB:HMDB0031193,REACTOME:REACT_2775.1,CAS:99-14-9,CHEMSPIDER:14220); ATP (annotations: CHEBI:CHEBI:15422,PUBCHEM:5957,CAS:56-65-5,MESH_2012:D000255,CHEMBL_COMPOUND:CHEMBL14249,CHEMSPIDER:5742,WIKIPEDIA:Adenosine triphosphate,HMDB:HMDB0000538,KEGG_COMPOUND:C00002); coenzyme A (annotations: CHEBI:CHEBI:15346,REACTOME:REACT_3654.2)
  Modifiers: Succinyl-CoA ligase (annotations: REACTOME:REACT_5440.1,REACTOME:REACT_5345.1)
  (References: PUBMED:9765290|PUBMED:9765291|PUBMED:13181903|PUBMED:15877282|PUBMED:15234968|REACTOME:REACT_629.2|PUBMED:10727444)
RID: 55214 (;Known transition omitted'):
  Reactants: ELOVL4 (formerSymbols: SCA34,STGD2,STGD3) (annotations: ,HGNC_SYMBOL:ELOVL4,UNIPROT:Q9GZR5,HGNC:14415,ENTREZ:6785,REFSEQ:NM_022726)
  Products: Fatty Acid Biosynthesis (annotations: WIKIPATHWAYS:WP4491,GO:GO:0006633)
  Modifiers: None
RID: 55969 (;Positive influence'):
  Reactants: NR1H3 (annotations: REFSEQ:NM_001130101,,HGNC:7966,ENTREZ:10062,UNIPROT:Q13133,HGNC_SYMBOL:NR1H3)
  Products: SREBF1 (annotations: UNIPROT:P36956,REFSEQ:NM_004176,ENTREZ:6720,HGNC:11289,HGNC_SYMBOL:SREBF1,)
  Modifiers: None
RID: 55488 (;State transition'):
  Reactants: CASP9 (annotations: HGNC_SYMBOL:CASP9,REFSEQ:NM_032996,ENTREZ:842,,HGNC:1511,UNIPROT:P55211)
  Products: CASP9 (annotations: HGNC_SYMBOL:CASP9,REFSEQ:NM_032996,ENTREZ:842,,HGNC:1511,UNIPROT:P55211)
  Modifiers: AKT1 (annotations: ENTREZ:207,HGNC:391,PUBMED:28416361,HGNC_SYMBOL:AKT1,REFSEQ:NM_005163,UNIPROT:P31749,)
RID: 55827 (;Positive influence'):
  Reactants: CYP4A11 (formerSymbols: CYP4A2) (annotations: ENTREZ:1579,HGNC:2642,UNIPROT:Q02928,REFSEQ:NM_000778,HGNC_SYMBOL:CYP4A11,)
  Products: Microsomal Omega-Oxidation (annotations: WIKIPATHWAYS:WP206)
  Modifiers: None
RID: 56026 (;Positive influence'):
  Reactants: CREB1 (annotations: REFSEQ:NM_134442,HGNC:2345,ENTREZ:1385,HGNC_SYMBOL:CREB1,UNIPROT:P16220,)
  Products: Glucose metabolism
  Modifiers: None
RID: 55108 (;State transition'):
  Reactants: LDLR
  Products:  
  Modifiers: None
RID: 55138 (;Known transition omitted'):
  Reactants: ELOVL3 (annotations: UNIPROT:Q9HB03,HGNC:18047,ENTREZ:83401,HGNC_SYMBOL:ELOVL3,REFSEQ:NM_152310,)
  Products: Fatty Acid Biosynthesis (annotations: WIKIPATHWAYS:WP4491,GO:GO:0006633)
  Modifiers: None
RID: 55855 (;State transition'):
  Reactants: Acetyl-CoA (annotations: CHEBI:CHEBI:15351)
  Products: Acetoacetyl-CoA (annotations: CHEBI:CHEBI:15345)
  Modifiers: ACAT2 (annotations: ENTREZ:39,HGNC:94,HGNC_SYMBOL:ACAT2,REFSEQ:NM_005891,UNIPROT:Q9BWD1,)
  (References: DOI:10.1016/B978-0-12-824048-9.00005-5)
RID: 55799 (;Positive influence'):
  Reactants: APOC3 (annotations: HGNC:610,UNIPROT:P02656,ENTREZ:345,REFSEQ:NM_000040,,HGNC_SYMBOL:APOC3)
  Products: Apolipoprotein Metabolism
  Modifiers: None
RID: 55566 (;Positive influence'):
  Reactants: PPARA (formerSymbols: PPAR) (annotations: HGNC_SYMBOL:PPARA,ENTREZ:5465,REFSEQ:NM_001001928,,PUBMED:26451809,UNIPROT:Q07869,HGNC:9232)
  Products: SLC27A1 (annotations: ENTREZ:376497,UNIPROT:Q6PCB7,HGNC:10995,HGNC_SYMBOL:SLC27A1,REFSEQ:NM_198580,)
  Modifiers: None
RID: 55538 (;Positive influence'):
  Reactants: GYS
  Products: Glycogen Synthesis (annotations: PUBMED:28416361)
  Modifiers: None
RID: 55568 (;State transition'):
  Reactants: AKT1 (annotations: ENTREZ:207,HGNC:391,PUBMED:28416361,HGNC_SYMBOL:AKT1,REFSEQ:NM_005163,UNIPROT:P31749,)
  Products: AKT1 (annotations: ENTREZ:207,HGNC:391,PUBMED:28416361,HGNC_SYMBOL:AKT1,REFSEQ:NM_005163,UNIPROT:P31749,)
  Modifiers: PDPK1 (annotations: ,ENTREZ:5170,HGNC:8816,REFSEQ:NM_001261816,HGNC_SYMBOL:PDPK1,UNIPROT:O15530)
RID: 55952 (;Positive influence'):
  Reactants: FOXO1 (formerSymbols: FKHR,FOXO1A) (annotations: HGNC:3819,,REFSEQ:NM_002015,ENTREZ:2308,PUBMED:28416361,HGNC_SYMBOL:FOXO1,UNIPROT:Q12778)
  Products: G6PC (annotations: PUBMED:28416361,)
  Modifiers: None
RID: 55633 (;State transition'):
  Reactants: Fructose-2,6-Bisphosphate (annotations: CHEBI:CHEBI:28602)
  Products: Fructose-6-Phosphate (annotations: CHEBI:CHEBI:15946,CHEBI:CHEBI:16084)
  Modifiers: PFKFB1 (formerSymbols: PFRX) (annotations: ENTREZ:5207,REFSEQ:NM_001271804,UNIPROT:P16118,HGNC:8872,HGNC_SYMBOL:PFKFB1,)
RID: 55555 (;State transition'):
  Reactants: PFKFB
  Products: PFKFB
  Modifiers: PKA
RID: 56022 (;State transition'):
  Reactants: Cholestadienol (annotations: CHEBI:CHEBI:145214)
  Products: Lathosterol (annotations: CHEBI:CHEBI:17168)
  Modifiers: DHCR24 (formerSymbols: DCE) (annotations: REFSEQ:NM_014762,HGNC_SYMBOL:DHCR24,,ENTREZ:1718,UNIPROT:Q15392,HGNC:2859)
  (References: DOI:10.1016/B978-0-12-824048-9.00005-5)
RID: 55948 (;Positive influence'):
  Reactants: DBI (annotations: HGNC_SYMBOL:DBI,ENTREZ:1622,,UNIPROT:P07108,HGNC:2690,REFSEQ:NM_020548)
  Products: Fatty Acid Transport (annotations: WIKIPATHWAYS:WP5061)
  Modifiers: None
RID: 55304 (PDmap:re543.0;State transition'):
  Reactants: cis-dec-4-enoyl-CoA (annotations: PUBCHEM:6443609,REACTOME:REACT_4645.1,CHEBI:CHEBI:29140)
  Products: (2-trans,4-cis)-deca-2,4-dienoyl-CoA (annotations: REACTOME:REACT_3866.1,CHEBI:CHEBI:29119)
  Modifiers: ACADM (annotations: UNIPROT:P11310,HGNC_SYMBOL:ACADM,,HGNC:89,REFSEQ:NM_000016,ENTREZ:34)
  (References: REACTOME:REACT_1111.1)
RID: 55259 (PDmap:re434.0;State transition'):
  Reactants: SOD2:Mn2+
  Products: SOD2:Mn2+
  Modifiers: SIRT3 (annotations: ENTREZ:23410,HGNC_SYMBOL:SIRT3,UNIPROT:Q9NTG7,HGNC:14931,REFSEQ:NM_001017524,)
  (References: PUBMED:21658599|PUBMED:21109198)
RID: 55159 (;Positive influence'):
  Reactants: Cholesterol (annotations: CHEBI:CHEBI:16113,KEGG_COMPOUND:C00187)
  Products: Lipoproteins (annotations: GO:GO:0140306,GO:GO:0008203)
  Modifiers: None
RID: 56121 (;Positive influence'):
  Reactants: ESR1 (formerSymbols: ESR) (annotations: HGNC:3467,ENTREZ:2099,,REFSEQ:NM_000125,UNIPROT:P03372,HGNC_SYMBOL:ESR1)
  Products: PCK1 (annotations: ,PUBMED:28416361,HGNC:8724,UNIPROT:P35558,HGNC_SYMBOL:PCK1,REFSEQ:NM_002591,ENTREZ:5105)
  Modifiers: None
RID: 55580 (;Negative influence'):
  Reactants: GSK3B (annotations: HGNC_SYMBOL:GSK3B,ENTREZ:2932,PUBMED:28416361,,HGNC:4617,UNIPROT:P49841,REFSEQ:NM_001146156)
  Products: Cell Proliferation (annotations: GO:GO:0072574)
  Modifiers: None
RID: 55780 (;Positive influence'):
  Reactants: RPS6KB2 (annotations: REFSEQ:NM_003952,HGNC:10437,ENTREZ:6199,,UNIPROT:Q9UBS0,HGNC_SYMBOL:RPS6KB2)
  Products: Cell Growth (annotations: GO:GO:0016049)
  Modifiers: None
RID: 55625 (;Transport'):
  Reactants: FA =/< C12
  Products: Mitochondrial Beta-Oxidation (annotations: WIKIPATHWAYS:WP143)
  Modifiers: None
RID: 55495 (;State transition'):
  Reactants: PDPK1 (annotations: ,ENTREZ:5170,HGNC:8816,REFSEQ:NM_001261816,HGNC_SYMBOL:PDPK1,UNIPROT:O15530)
  Products: PDPK1 (annotations: ,ENTREZ:5170,HGNC:8816,REFSEQ:NM_001261816,HGNC_SYMBOL:PDPK1,UNIPROT:O15530)
  Modifiers: PIP3
RID: 55857 (;Positive influence'):
  Reactants: Estrogens (annotations: CHEBI:CHEBI:50114)
  Products: ESR1 (formerSymbols: ESR) (annotations: HGNC:3467,ENTREZ:2099,,REFSEQ:NM_000125,UNIPROT:P03372,HGNC_SYMBOL:ESR1)
  Modifiers: None
RID: 55127 (;State transition'):
  Reactants: Cholesterol (annotations: CHEBI:CHEBI:16113,KEGG_COMPOUND:C00187)
  Products: Cholesterol (annotations: CHEBI:CHEBI:16113,KEGG_COMPOUND:C00187)
  Modifiers: ABCA1 (formerSymbols: ABC1,HDLDT1) (annotations: REFSEQ:NM_005502,HGNC:29,HGNC_SYMBOL:ABCA1,,ENTREZ:19,UNIPROT:O95477)
  (References: WIKIPATHWAYS:WP5304)
RID: 55448 (PDmap:re567.0;State transition'):
  Reactants: 1-acyl-sn-glycerol 3-phosphate (annotations: REACTOME:REACT_4701.3,CHEBI:CHEBI:16975)
  Products: 1,2-diacyl-sn-glycerol 3-phosphate (annotations: REACTOME:REACT_3539.3,CHEBI:CHEBI:29089)
  Modifiers: ENZYME: 2.3.1.51 (annotations: EC:2.3.1.51)
  (References: PUBMED:19336658|PUBMED:16620771|PUBMED:18718904|PUBMED:9461603|PUBMED:9212163|REACTOME:REACT_2042.5|KEGG_REACTION:R02241|PUBMED:15367102)
RID: 55424 (PDmap:re533.0;State transition'):
  Reactants: 3-oxohexanoyl-CoA (annotations: REACTOME:REACT_4535.1,CHEBI:CHEBI:27648)
  Products: butyryl-CoA (annotations: CHEBI:CHEBI:15517)
  Modifiers: trifunctional Protein
  (References: REACTOME:REACT_2140.2|PUBMED:1550553)
RID: 56148 (;Truncation'):
  Reactants: Fructose-1,6-Bisphosphate (annotations: CHEBI:CHEBI:78682)
  Products: Glyceralaldehyde-3-Phosphate (annotations: CHEBI:CHEBI:17138); Dihydroxyacetone-Phosphate (annotations: CHEBI:CHEBI:16108)
  Modifiers: ALDOB (annotations: ENTREZ:229,REFSEQ:NM_000035,HGNC:417,,HGNC_SYMBOL:ALDOB,UNIPROT:P05062)
  (References: WIKIPATHWAYS:WP534)
RID: 55175 (;State transition'):
  Reactants: Mevalonate-P (annotations: CHEBI:CHEBI:25350)
  Products: Mevalonate-PP (annotations: CHEBI:CHEBI:25350)
  Modifiers: PMVK (annotations: HGNC_SYMBOL:PMVK,REFSEQ:NM_006556,UNIPROT:Q15126,,HGNC:9141,ENTREZ:10654)
  (References: WIKIPATHWAYS:WP4718|DOI:10.1016/B978-0-12-824048-9.00005-5)
RID: 56096 (;Positive influence'):
  Reactants: CREB1 (annotations: REFSEQ:NM_134442,HGNC:2345,ENTREZ:1385,HGNC_SYMBOL:CREB1,UNIPROT:P16220,)
  Products: PCK1 (annotations: ,PUBMED:28416361,HGNC:8724,UNIPROT:P35558,HGNC_SYMBOL:PCK1,REFSEQ:NM_002591,ENTREZ:5105)
  Modifiers: None
RID: 56131 (;Negative influence'):
  Reactants: Fructose-2,6-Bisphosphate (annotations: CHEBI:CHEBI:28602)
  Products: FBP1 (formerSymbols: FBP) (annotations: HGNC_SYMBOL:FBP1,UNIPROT:P09467,REFSEQ:NM_000507,PUBMED:31284506,HGNC:3606,ENTREZ:2203,)
  Modifiers: None
RID: 55852 (;State transition'):
  Reactants: Butanoyl-CoA (annotations: CHEBI:CHEBI:22954)
  Products: Crotonoyl-CoA (annotations: CHEBI:CHEBI:15473,CHEBI:CHEBI:57332)
  Modifiers: ACADS (annotations: HGNC:90,UNIPROT:P16219,HGNC_SYMBOL:ACADS,,ENTREZ:35,REFSEQ:NM_000017)
RID: 55728 (;State transition'):
  Reactants: CREB1 (annotations: REFSEQ:NM_134442,HGNC:2345,ENTREZ:1385,HGNC_SYMBOL:CREB1,UNIPROT:P16220,)
  Products: CREB1 (annotations: REFSEQ:NM_134442,HGNC:2345,ENTREZ:1385,HGNC_SYMBOL:CREB1,UNIPROT:P16220,)
  Modifiers: None
RID: 56034 (;Positive influence'):
  Reactants: mTORC1 (annotations: GO:GO:0031931)
  Products: Cell Growth (annotations: GO:GO:0016049)
  Modifiers: None
RID: 55867 (;State transition'):
  Reactants: FF-MAS (annotations: CHEBI:CHEBI:17813)
  Products: T-MAS (annotations: CHEBI:CHEBI:18364)
  Modifiers: TM7SF2 (annotations: ,HGNC:11863,REFSEQ:NM_003273,UNIPROT:O76062,ENTREZ:7108,HGNC_SYMBOL:TM7SF2); LBR (annotations: HGNC_SYMBOL:LBR,UNIPROT:Q14739,REFSEQ:NM_002296,HGNC:6518,ENTREZ:3930,)
  (References: DOI:10.1016/B978-0-12-824048-9.00005-5)
RID: 55543 (;State transition'):
  Reactants: PFKL (annotations: HGNC:8876,UNIPROT:P17858,PUBMED:31284506,REFSEQ:NM_001002021,,ENTREZ:5211,HGNC_SYMBOL:PFKL)
  Products: PFKL (annotations: HGNC:8876,UNIPROT:P17858,PUBMED:31284506,REFSEQ:NM_001002021,,ENTREZ:5211,HGNC_SYMBOL:PFKL)
  Modifiers: PKA
RID: 56094 (;State transition'):
  Reactants: PKLR (annotations: HGNC_SYMBOL:PKLR,REFSEQ:NM_000298,HGNC:9020,UNIPROT:P30613,ENTREZ:5313,)
  Products: PKLR (annotations: HGNC_SYMBOL:PKLR,REFSEQ:NM_000298,PUBMED:31284506,HGNC:9020,UNIPROT:P30613,ENTREZ:5313,)
  Modifiers: None
RID: 56197 (;State transition'):
  Reactants: D-Glucose (annotations: CHEBI:CHEBI:4167)
  Products: Glucose-6-Phosphate (annotations: CHEBI:CHEBI:14314)
  Modifiers: HK1 (annotations: REFSEQ:NM_000188,,HGNC_SYMBOL:HK1,UNIPROT:P19367,HGNC:4922,ENTREZ:3098)
  (References: WIKIPATHWAYS:WP500)
RID: 55703 (;Known transition omitted'):
  Reactants: Xylulosse-5-Phosphate (annotations: CHEBI:CHEBI:16332); Ribose-5-Phosphate (annotations: CHEBI:CHEBI:78679)
  Products: Glyceralaldehyde-3-Phosphate (annotations: CHEBI:CHEBI:17138); Sedoheptulose-7-Phosphate (annotations: CHEBI:CHEBI:15721)
  Modifiers: TKT (annotations: ENTREZ:7086,HGNC:11834,HGNC_SYMBOL:TKT,REFSEQ:NM_001064,,UNIPROT:P29401)
RID: 55481 (;State transition'):
  Reactants: BAD (annotations: REFSEQ:NM_032989,UNIPROT:Q92934,ENTREZ:572,,HGNC_SYMBOL:BAD,HGNC:936)
  Products: BAD (annotations: REFSEQ:NM_032989,UNIPROT:Q92934,ENTREZ:572,,HGNC_SYMBOL:BAD,HGNC:936)
  Modifiers: AKT1 (annotations: ENTREZ:207,HGNC:391,PUBMED:28416361,HGNC_SYMBOL:AKT1,REFSEQ:NM_005163,UNIPROT:P31749,)
RID: 56078 (;State transition'):
  Reactants: Glucose-6-Phosphate (annotations: CHEBI:CHEBI:14314)
  Products: 6-Phosphogluconolactone (annotations: CHEBI:CHEBI:16938)
  Modifiers: G6PD (annotations: UNIPROT:P11413,HGNC:4057,ENTREZ:2539,HGNC_SYMBOL:G6PD,,REFSEQ:NM_000402)
RID: 55762 (;Positive influence'):
  Reactants: PFKFB
  Products: Glycolysis (annotations: GO:GO:0061621)
  Modifiers: None
RID: 55875 (;Positive influence'):
  Reactants: APOA2 (annotations: HGNC:601,,ENTREZ:336,UNIPROT:P02652,HGNC_SYMBOL:APOA2,REFSEQ:NM_001643)
  Products: Apolipoprotein Metabolism
  Modifiers: None
RID: 55535 (;Positive influence'):
  Reactants: CPT1
  Products: Beta-Oxidation
  Modifiers: None
RID: 55789 (;Positive influence'):
  Reactants: NR1H3 (annotations: REFSEQ:NM_001130101,,HGNC:7966,ENTREZ:10062,UNIPROT:Q13133,HGNC_SYMBOL:NR1H3)
  Products: SCD (formerSymbols: SCDOS) (annotations: ,ENTREZ:6319,HGNC_SYMBOL:SCD,UNIPROT:O00767,HGNC:10571,REFSEQ:NM_005063,PUBMED:26451809)
  Modifiers: None
RID: 55224 (;Transcription'):
  Reactants: HMGCS1 (formerSymbols: HMGCS) (annotations: UNIPROT:Q01581,HGNC:5007,HGNC_SYMBOL:HMGCS1,,ENTREZ:3157,REFSEQ:NM_001098272)
  Products: HMGCS1 (formerSymbols: HMGCS) (annotations: UNIPROT:Q01581,HGNC:5007,HGNC_SYMBOL:HMGCS1,,ENTREZ:3157,REFSEQ:NM_001098272)
  Modifiers: SREBF2 (annotations: HGNC:11290,REFSEQ:NM_004599,UNIPROT:Q12772,,HGNC_SYMBOL:SREBF2,ENTREZ:6721)
  (References: WIKIPATHWAYS:WP4718)
RID: 55380 (PDmap:re510.0;State transition'):
  Reactants: (S)-3-hydroxypalmitoyl-CoA (annotations: REACTOME:REACT_2413.1,CHEBI:CHEBI:27402)
  Products: 3-oxopalmitoyl-CoA (annotations: HMDB:HMDB0006402,CAS:34619-89-1,CHEBI:CHEBI:15491,REACTOME:REACT_3202.1,CHEMSPIDER:389499,KEGG_COMPOUND:C05259,PUBCHEM:440601)
  Modifiers: trifunctional Protein
  (References: PUBMED:1550553|REACTOME:REACT_488.2)
RID: 55750 (;Truncation'):
  Reactants: Citrate (annotations: CHEBI:CHEBI:16947,CHEBI:CHEBI:133748,CHEBI:CHEBI:50744)
  Products: Acetyl-CoA (annotations: CHEBI:CHEBI:15351,CHEBI:CHEBI:57288); Oxalacetate (annotations: CHEBI:CHEBI:16452)
  Modifiers: ACLY (annotations: HGNC:115,REFSEQ:NM_001096,,ENTREZ:47,HGNC_SYMBOL:ACLY,UNIPROT:P53396)
RID: 55884 (;Positive influence'):
  Reactants: NR1I3 (annotations: ENTREZ:9970,UNIPROT:Q14994,,HGNC:7969,REFSEQ:NM_001077469,HGNC_SYMBOL:NR1I3)
  Products: CYP4A11 (formerSymbols: CYP4A2) (annotations: ENTREZ:1579,HGNC:2642,UNIPROT:Q02928,REFSEQ:NM_000778,HGNC_SYMBOL:CYP4A11,)
  Modifiers: None
RID: 55805 (;Positive influence'):
  Reactants: GCG (annotations: HGNC_SYMBOL:GCG,,REFSEQ:NM_002054,HGNC:4191,UNIPROT:P01275,ENTREZ:2641)
  Products: PFKL (annotations: HGNC:8876,UNIPROT:P17858,PUBMED:31284506,REFSEQ:NM_001002021,,ENTREZ:5211,HGNC_SYMBOL:PFKL)
  Modifiers: None
RID: 55946 (;State transition'):
  Reactants: Fatty acyl-carnitine; CoA (annotations: CHEBI:CHEBI:15346)
  Products: Fatty acyl-CoA; Carnitin (annotations: CHEBI:CHEBI:16347)
  Modifiers: SLC25A20 (formerSymbols: CACT) (annotations: REFSEQ:NM_000387,HGNC:1421,ENTREZ:788,,UNIPROT:O43772,HGNC_SYMBOL:SLC25A20); CPT2 (formerSymbols: CPT1) (annotations: HGNC_SYMBOL:CPT2,HGNC:2330,REFSEQ:NM_000098,UNIPROT:P23786,,ENTREZ:1376)
RID: 55144 (;State transition'):
  Reactants: Lathosterol (annotations: CHEBI:CHEBI:17168)
  Products: 7-Dehydrocholesterol (annotations: CHEBI:CHEBI:17759)
  Modifiers: SC5D (formerSymbols: SC5DL) (annotations: ENTREZ:6309,HGNC:10547,HGNC_SYMBOL:SC5D,REFSEQ:NM_001024956,,UNIPROT:O75845)
  (References: WIKIPATHWAYS:WP4718|DOI:10.1016/B978-0-12-824048-9.00005-5)
RID: 55674 (;Positive influence'):
  Reactants: NFE2L2 (annotations: UNIPROT:Q16236,,PUBMED:28416361,ENTREZ:4780,REFSEQ:NM_006164,HGNC:7782,HGNC_SYMBOL:NFE2L2)
  Products: SLC2A2 (formerSymbols: GLUT2) (annotations: HGNC_SYMBOL:SLC2A2,HGNC:11006,UNIPROT:P11168,REFSEQ:NM_000340,ENTREZ:6514,)
  Modifiers: None
RID: 56016 (;Known transition omitted'):
  Reactants: Xylulosse-5-Phosphate (annotations: CHEBI:CHEBI:16332); Erythrose-4-Phosphate (annotations: CHEBI:CHEBI:48153)
  Products: Fructose-6-Phosphate (annotations: CHEBI:CHEBI:15946,CHEBI:CHEBI:16084); Glyceralaldehyde-3-Phosphate (annotations: CHEBI:CHEBI:17138)
  Modifiers: TKT (annotations: ENTREZ:7086,HGNC:11834,HGNC_SYMBOL:TKT,REFSEQ:NM_001064,,UNIPROT:P29401)
RID: 55742 (;State transition'):
  Reactants: BAD (annotations: REFSEQ:NM_032989,UNIPROT:Q92934,ENTREZ:572,,HGNC_SYMBOL:BAD,HGNC:936)
  Products: BAD (annotations: REFSEQ:NM_032989,UNIPROT:Q92934,ENTREZ:572,,HGNC_SYMBOL:BAD,HGNC:936)
  Modifiers: AKT1 (annotations: ENTREZ:207,HGNC:391,PUBMED:28416361,HGNC_SYMBOL:AKT1,REFSEQ:NM_005163,UNIPROT:P31749,)
RID: 55369 (PDmap:re381.0;State transition'):
  Reactants: (S)-malate(2-) (annotations: KEGG_COMPOUND:C00149,HMDB:HMDB0000156,PUBCHEM:222656,REACTOME:REACT_4778.1,CHEMSPIDER:193317,WIKIPEDIA:Apple acid,CHEBI:CHEBI:30797,CHEBI:CHEBI:15589,CAS:97-67-6); NAD(+) (annotations: KEGG_COMPOUND:C00003,CAS:53-84-9,PUBCHEM:5893,CHEMSPIDER:5682,REACTOME:REACT_4970.1,CHEBI:CHEBI:15846,HMDB:HMDB0000902,WIKIPEDIA:NAD)
  Products: oxaloacetate(2-) (annotations: PUBCHEM:970,CHEBI:CHEBI:30744,KEGG_COMPOUND:C00036,CAS:328-42-7,HMDB:HMDB0000223,CHEMSPIDER:945,REACTOME:REACT_5376.1,CHEBI:CHEBI:16452,WIKIPEDIA:Oxalacetic acid); H+ (annotations: CHEBI:CHEBI:15378); NADH (annotations: REACTOME:REACT_2390.1,KEGG_COMPOUND:C00004,HMDB:HMDB0001487,CHEMSPIDER:903,WIKIPEDIA:NADH,CAS:58-68-4,CHEBI:CHEBI:16908,PUBCHEM:928,CHEMBL_COMPOUND:CHEMBL1628272,MESH_2012:D009243)
  Modifiers: malate dehydrogenase 2 (annotations: REACTOME:REACT_11471.1)
  (References: REACTOME:REACT_2172.3|PUBMED:16740313)
RID: 55504 (;State transition'):
  Reactants: AKT1 (annotations: ENTREZ:207,HGNC:391,PUBMED:28416361,HGNC_SYMBOL:AKT1,REFSEQ:NM_005163,UNIPROT:P31749,)
  Products: AKT1 (annotations: ENTREZ:207,HGNC:391,PUBMED:28416361,HGNC_SYMBOL:AKT1,REFSEQ:NM_005163,UNIPROT:P31749,)
  Modifiers: PDPK1 (annotations: ,ENTREZ:5170,HGNC:8816,REFSEQ:NM_001261816,HGNC_SYMBOL:PDPK1,UNIPROT:O15530)
RID: 56195 (;Known transition omitted'):
  Reactants: Lactose (annotations: CHEBI:CHEBI:17716,CHEBI:CHEBI:36218,CHEBI:CHEBI:36219); UDP (annotations: CHEBI:CHEBI:17659,CHEBI:CHEBI:58223)
  Products: UDP-Galactose (annotations: CHEBI:CHEBI:67119); Galactose (annotations: CHEBI:CHEBI:28260)
  Modifiers: None
RID: 55399 (PDmap:re512.0;State transition'):
  Reactants: palmitoyl-CoA (annotations: REACTOME:REACT_11391.1,CHEMSPIDER:14902,PUBCHEM:15667,HMDB:HMDB0001338,KEGG_COMPOUND:C00154,CHEBI:CHEBI:15525,WIKIPEDIA:palmitoyl CoA,CAS:1763-10-6)
  Products: (E)-hexadec-2-enoyl-CoA (annotations: REACTOME:REACT_4177.1,CHEBI:CHEBI:28935)
  Modifiers: ACADVL (annotations: ENTREZ:37,HGNC:92,,UNIPROT:P49748,HGNC_SYMBOL:ACADVL,REFSEQ:NM_000018)
  (References: REACTOME:REACT_398.2|PUBMED:1540149|PUBMED:13295225)
RID: 55887 (;State transition'):
  Reactants: TSC (annotations: PUBMED:28416361)
  Products: TSC (annotations: PUBMED:28416361)
  Modifiers: None
RID: 55430 (PDmap:re385.0;State transition'):
  Reactants: succinyl-CoA (annotations: HMDB:HMDB0001022,CHEMSPIDER:388307,KEGG_COMPOUND:C00091,WIKIPEDIA:Succinyl-CoA,REACTOME:REACT_2852.1,CAS:604-98-8,CHEBI:CHEBI:15380,PUBCHEM:439161); phosphate(3-) (annotations: WIKIPEDIA:Phosphate,PUBCHEM:1061,CAS:14265-44-2,KEGG_COMPOUND:C00009,CHEMSPIDER:1032,CHEBI:CHEBI:18367,REACTOME:REACT_5781.1,HMDB:HMDB0001429); GDP (annotations: CHEMSPIDER:8630,CHEMBL_COMPOUND:CHEMBL384759,HMDB:HMDB0001201,CHEBI:CHEBI:17552,WIKIPEDIA:GDP,CAS:146-91-8,REACTOME:REACT_3998.1,KEGG_COMPOUND:C00035,PUBCHEM:8977)
  Products: succinic acid (annotations: KEGG_COMPOUND:C19806,CHEBI:CHEBI:45969,WIKIPEDIA:1,2,3-Propanetricarboxylic_acid,CHEBI:CHEBI:15741,PUBCHEM:14925,HMDB:HMDB0031193,REACTOME:REACT_2775.1,CAS:99-14-9,CHEMSPIDER:14220); GTP (annotations: REACTOME:REACT_4430.1,CAS:86-01-1,CHEMSPIDER:6569,PUBCHEM:6830,WIKIPEDIA:Guanosine triphosphate,KEGG_COMPOUND:C00044,HMDB:HMDB0001273,CHEBI:CHEBI:15996); coenzyme A (annotations: CHEBI:CHEBI:15346,REACTOME:REACT_3654.2)
  Modifiers: Succinyl-CoA ligase (annotations: REACTOME:REACT_5440.1,REACTOME:REACT_5345.1)
  (References: PUBMED:9765290|PUBMED:9765291|PUBMED:13181903|PUBMED:17668387|PUBMED:15234968|REACTOME:REACT_337.2|PUBMED:10727444)
RID: 55552 (;Positive influence'):
  Reactants: ACC
  Products: Lipogenesis
  Modifiers: None
RID: 56144 (;Truncation'):
  Reactants: Fructose-1-Phosphate (annotations: CHEBI:CHEBI:18105)
  Products: Dihydroxyacetone-Phosphate (annotations: CHEBI:CHEBI:16108); Glyceraldehyde (annotations: CHEBI:CHEBI:5445,CHEBI:CHEBI:17378)
  Modifiers: ALDOB (annotations: ENTREZ:229,REFSEQ:NM_000035,HGNC:417,,HGNC_SYMBOL:ALDOB,UNIPROT:P05062)
RID: 55573 (;State transition'):
  Reactants: PIP3 (annotations: CHEBI:CHEBI:60169)
  Products: PIP2 (annotations: CHEBI:CHEBI:37328)
  Modifiers: PTEN (formerSymbols: BZS,MHAM) (annotations: HGNC:9588,HGNC_SYMBOL:PTEN,ENTREZ:5728,,REFSEQ:NM_000314,UNIPROT:P60484)
RID: 55231 (;State transition'):
  Reactants: Presqualene diphosphate (annotations: CHEBI:CHEBI:15442)
  Products: SQNE (annotations: CHEBI:CHEBI:15440)
  Modifiers: FDFT1
  (References: DOI:10.3180/R-HSA-191273.7|WIKIPATHWAYS:WP4718|DOI:10.1016/B978-0-12-824048-9.00005-5)
RID: 55937 (;State transition'):
  Reactants: Glycerol (annotations: CHEBI:CHEBI:17754)
  Products: Glycerol-3-Phosphate (annotations: CHEBI:CHEBI:15978)
  Modifiers: GK (annotations: ENTREZ:2710,HGNC:4289,REFSEQ:NM_000167,UNIPROT:P32189,HGNC_SYMBOL:GK,)
RID: 55532 (;State transition'):
  Reactants: CREB1 (annotations: REFSEQ:NM_134442,HGNC:2345,ENTREZ:1385,HGNC_SYMBOL:CREB1,UNIPROT:P16220,)
  Products: CREB1 (annotations: REFSEQ:NM_134442,HGNC:2345,ENTREZ:1385,HGNC_SYMBOL:CREB1,UNIPROT:P16220,)
  Modifiers: None
RID: 55604 (;State transition'):
  Reactants: ATP (annotations: CHEBI:CHEBI:15422)
  Products: cAMP (annotations: CHEBI:CHEBI:17489)
  Modifiers: ADCY
  (References: PUBMED:24692138)
RID: 55663 (;Negative influence'):
  Reactants: D-Glucose (annotations: CHEBI:CHEBI:4167)
  Products: PYGL (annotations: ENTREZ:5836,REFSEQ:NM_002863,HGNC_SYMBOL:PYGL,HGNC:9725,,UNIPROT:P06737)
  Modifiers: None
RID: 55276 (;State transition'):
  Reactants: GP4G (annotations: CHEBI:CHEBI:15883); H2O (annotations: HMDB:HMDB0002111,CHEBI:CHEBI:15377,PUBCHEM:962,CHEMSPIDER:937,MESH_2012:D014867,WIKIPEDIA:Water,CAS:7732-18-5,CHEMBL_COMPOUND:CHEMBL1098659,KEGG_COMPOUND:C00001)
  Products: GMP (annotations: PUBCHEM:6804,HMDB:HMDB0001397,WIKIPEDIA:GMP,CAS:85-32-5,CHEBI:CHEBI:17345,CHEMSPIDER:6545,KEGG_COMPOUND:C00144); GTP (annotations: REACTOME:REACT_4430.1,CAS:86-01-1,CHEMSPIDER:6569,PUBCHEM:6830,WIKIPEDIA:Guanosine triphosphate,KEGG_COMPOUND:C00044,HMDB:HMDB0001273,CHEBI:CHEBI:15996)
  Modifiers: NUDT2 (formerSymbols: APAH1) (annotations: HGNC:8049,ENTREZ:318,HGNC_SYMBOL:NUDT2,,UNIPROT:P50583,REFSEQ:NM_001161)
  (References: REACTOME:REACT_264249)
RID: 55745 (;Positive influence'):
  Reactants: RXRA (annotations: UNIPROT:P19793,,HGNC:10477,REFSEQ:NM_002957,ENTREZ:6256,HGNC_SYMBOL:RXRA)
  Products: NR1H4 (annotations: ,ENTREZ:9971,HGNC:7967,UNIPROT:Q96RI1,REFSEQ:NM_005123,HGNC_SYMBOL:NR1H4)
  Modifiers: None
RID: 55410 (PDmap:re241.0;Positive influence'):
  Reactants: superoxide (annotations: HMDB:HMDB0002168,WIKIPEDIA:Superoxide,PUBCHEM:5359597,CHEMSPIDER:4514331,KEGG_COMPOUND:C00704,CHEBI:CHEBI:18421,CAS:11062-77-4)
  Products: ROS (annotations: CHEBI:CHEBI:26523)
  Modifiers: None
  (References: PUBMED:20045723)
RID: 55651 (;Transport'):
  Reactants: H+ (annotations: CHEBI:CHEBI:15378)
  Products: H+ (annotations: CHEBI:CHEBI:15378)
  Modifiers: None
RID: 55661 (;Transport'):
  Reactants: H+ (annotations: CHEBI:CHEBI:15378)
  Products: H+ (annotations: CHEBI:CHEBI:15378)
  Modifiers: Complex I
RID: 55898 (;State transition'):
  Reactants: FF-MAS (annotations: CHEBI:CHEBI:17813)
  Products: Dihydro-FF-MAS (annotations: CHEBI:CHEBI:78904)
  Modifiers: DHCR24 (formerSymbols: DCE) (annotations: REFSEQ:NM_014762,HGNC_SYMBOL:DHCR24,,ENTREZ:1718,UNIPROT:Q15392,HGNC:2859)
  (References: DOI:10.1016/B978-0-12-824048-9.00005-5)
RID: 55557 (;State transition'):
  Reactants: ADCY
  Products: ADCY
  Modifiers: Gα
RID: 55998 (;Positive influence'):
  Reactants: ME1 (annotations: HGNC:6983,REFSEQ:NM_002395,,ENTREZ:4199,UNIPROT:P48163,HGNC_SYMBOL:ME1)
  Products: Malate metabolism (annotations: GO:GO:0006108)
  Modifiers: None
RID: 55984 (;State transition'):
  Reactants: Citrate (annotations: CHEBI:CHEBI:16947,CHEBI:CHEBI:133748,CHEBI:CHEBI:50744)
  Products: Aconitate (annotations: CHEBI:CHEBI:22210)
  Modifiers: ACO
RID: 55916 (;State transition'):
  Reactants: 3-Oxodecanoyl-CoA  (annotations: CHEBI:CHEBI:28528,CHEBI:CHEBI:62548)
  Products: Octanoyl-CoA (annotations: CHEBI:CHEBI:15533); Acetyl-CoA (annotations: CHEBI:CHEBI:15351,CHEBI:CHEBI:57288)
  Modifiers: Mitochondrial trifunctional enzyme
RID: 55815 (;State transition'):
  Reactants: 24,25-Dihydrolanosterol (annotations: CHEBI:CHEBI:28113)
  Products: Dihydro-FF-MAS (annotations: CHEBI:CHEBI:78904)
  Modifiers: CYP51A1 (formerSymbols: CYP51) (annotations: UNIPROT:Q16850,,HGNC_SYMBOL:CYP51A1,ENTREZ:1595,HGNC:2649,REFSEQ:NM_000786)
  (References: DOI:10.1016/B978-0-12-824048-9.00005-5)
RID: 55611 (;Known transition omitted'):
  Reactants: LP(a)
  Products: LP(a)
  Modifiers: Secretion
RID: 55985 (;Positive influence'):
  Reactants: LDLR (annotations: HGNC_SYMBOL:LDLR,HGNC:6547,,ENTREZ:3949,REFSEQ:NM_000527,UNIPROT:P01130)
  Products: Lipid uptake
  Modifiers: None
RID: 55579 (;Negative influence'):
  Reactants: NR1I3 (annotations: ENTREZ:9970,UNIPROT:Q14994,,HGNC:7969,REFSEQ:NM_001077469,HGNC_SYMBOL:NR1I3)
  Products: CPT1A (formerSymbols: CPT1) (annotations: UNIPROT:P50416,PUBMED:19595610,HGNC_SYMBOL:CPT1A,HGNC:2328,ENTREZ:1374,REFSEQ:NM_001876,)
  Modifiers: None
RID: 55426 (PDmap:re564.0;State transition'):
  Reactants: glycerol (annotations: CHEBI:CHEBI:17754,REACTOME:REACT_3756.1)
  Products: sn-glycerol 3-phosphate (annotations: CHEMSPIDER:388308,KEGG_COMPOUND:C00093,WIKIPEDIA:Glycerol 3-phosphate,HMDB:HMDB0000126,REACTOME:REACT_4327.2,CHEBI:CHEBI:15978,PUBCHEM:439162,CAS:57-03-4)
  Modifiers: GK (annotations: ENTREZ:2710,HGNC:4289,REFSEQ:NM_000167,UNIPROT:P32189,HGNC_SYMBOL:GK,)
  (References: PUBMED:15845384|REACTOME:REACT_724.2)
RID: 55142 (;State transition'):
  Reactants: T-MAS (annotations: CHEBI:CHEBI:18364)
  Products: Dihydro-T-MAS (annotations: CHEBI:CHEBI:87044)
  Modifiers: DHCR24 (formerSymbols: DCE) (annotations: REFSEQ:NM_014762,HGNC_SYMBOL:DHCR24,,ENTREZ:1718,UNIPROT:Q15392,HGNC:2859)
  (References: DOI:10.1016/B978-0-12-824048-9.00005-5)
RID: 55717 (;Transport'):
  Reactants: Fructose (annotations: CHEBI:CHEBI:28645,CHEBI:CHEBI:28757)
  Products: Fructose (annotations: CHEBI:CHEBI:28645,CHEBI:CHEBI:28757)
  Modifiers: SLC2A2 (formerSymbols: GLUT2) (annotations: HGNC_SYMBOL:SLC2A2,HGNC:11006,UNIPROT:P11168,REFSEQ:NM_000340,ENTREZ:6514,PUBMED:32591906,)
  (References: PUBMED:32591906)
RID: 55683 (;Positive influence'):
  Reactants: Fatty Acid Synthesis (annotations: GO:GO:0005835)
  Products: Fatty Acid (annotations: CHEBI:CHEBI:35366)
  Modifiers: None
RID: 56031 (;State transition'):
  Reactants: Lysophosphatidic Acid (annotations: CHEBI:CHEBI:32957); Acyl CoA (annotations: CHEBI:CHEBI:37554,CHEBI:CHEBI:58342)
  Products: Phosphatidic Acid
  Modifiers: PNPLA3 (formerSymbols: ADPN,C22orf20) (annotations: UNIPROT:Q9NST1,ENTREZ:80339,REFSEQ:NM_025225,,HGNC:18590,HGNC_SYMBOL:PNPLA3); AGPAT
RID: 55176 (;Transcription'):
  Reactants: ELOVL2 (annotations: UNIPROT:Q9NXB9,ENTREZ:54898,,HGNC_SYMBOL:ELOVL2,REFSEQ:NM_017770,HGNC:14416)
  Products: ELOVL2 (annotations: UNIPROT:Q9NXB9,ENTREZ:54898,,HGNC_SYMBOL:ELOVL2,REFSEQ:NM_017770,HGNC:14416)
  Modifiers: SREBF2 (annotations: HGNC:11290,REFSEQ:NM_004599,UNIPROT:Q12772,,HGNC_SYMBOL:SREBF2,ENTREZ:6721)
  (References: WIKIPATHWAYS:WP4718)
RID: 56189 (;State transition'):
  Reactants: Glycogen (n+1) (annotations: CHEBI:CHEBI:28087)
  Products: D-Glucose (annotations: CHEBI:CHEBI:4167)
  Modifiers: AGL (annotations: ,ENTREZ:178,HGNC_SYMBOL:AGL,UNIPROT:P35573,HGNC:321,REFSEQ:NM_000028)
  (References: WIKIPATHWAYS:WP500)
RID: 55777 (;State transition'):
  Reactants: (S)-3-Hydroxydodecanoyl-CoA (annotations: CHEBI:CHEBI:62558,CHEBI:CHEBI:27668)
  Products: 3-Oxododecanoyl-CoA (annotations: CHEBI:CHEBI:27868)
  Modifiers: HADH (formerSymbols: HADHSC) (annotations: HGNC_SYMBOL:HADH,REFSEQ:NM_005327,,HGNC:4799,ENTREZ:3033,UNIPROT:Q16836)
RID: 55186 (;Known transition omitted'):
  Reactants: 24S-hydroxycholesterol (annotations: CHEBI:CHEBI:34310)
  Products: Bile (annotations: GO:GO:0006699)
  Modifiers: None
RID: 55994 (;State transition'):
  Reactants: Glyceraldehyde (annotations: CHEBI:CHEBI:5445,CHEBI:CHEBI:17378)
  Products: Glyceralaldehyde-3-Phosphate (annotations: CHEBI:CHEBI:17138)
  Modifiers: TKFC (formerSymbols: DAK) (annotations: REFSEQ:NM_015533,HGNC_SYMBOL:TKFC,ENTREZ:26007,,HGNC:24552,UNIPROT:Q3LXA3)
RID: 55365 (PDmap:re532.0;State transition'):
  Reactants: (S)-3-hydroxyhexanoyl-CoA (annotations: CHEBI:CHEBI:28276,REACTOME:REACT_3348.1)
  Products: 3-oxohexanoyl-CoA (annotations: REACTOME:REACT_4535.1,CHEBI:CHEBI:27648)
  Modifiers: HADH (formerSymbols: HADHSC) (annotations: HGNC_SYMBOL:HADH,REFSEQ:NM_005327,,HGNC:4799,ENTREZ:3033,UNIPROT:Q16836)
  (References: REACTOME:REACT_2195.2|PUBMED:8687463)
RID: 55880 (;Positive influence'):
  Reactants: G6PD (annotations: UNIPROT:P11413,HGNC:4057,ENTREZ:2539,HGNC_SYMBOL:G6PD,,REFSEQ:NM_000402)
  Products: Penthose Phosphate Pathway (annotations: WIKIPATHWAYS:WP134)
  Modifiers: None
RID: 56064 (;Positive influence'):
  Reactants: GCGR:GCG (annotations: REFSEQ:NM_002115,HGNC_SYMBOL:HK3,,ENTREZ:3101,HGNC:4925,UNIPROT:P52790)
  Products: Gα
  Modifiers: None
  (References: PUBMED:24692138)
RID: 55686 (;State transition'):
  Reactants: Glucose (annotations: CHEBI:CHEBI:42758,CHEBI:CHEBI:4167,CHEBI:CHEBI:17234)
  Products: Glucose-6-Phosphate (annotations: CHEBI:CHEBI:14314)
  Modifiers: HK1 (annotations: REFSEQ:NM_000188,,HGNC_SYMBOL:HK1,UNIPROT:P19367,HGNC:4922,ENTREZ:3098); GCK (formerSymbols: MODY2) (annotations: ENTREZ:2645,,HGNC_SYMBOL:GCK,REFSEQ:NM_000162,UNIPROT:P35557,HGNC:4195)
RID: 55471 (;Positive influence'):
  Reactants: GCK (formerSymbols: MODY2) (annotations: ,ENTREZ:2645,HGNC_SYMBOL:GCK,PUBMED:28416361,REFSEQ:NM_000162,UNIPROT:P35557,HGNC:4195)
  Products: Glycolysis (annotations: GO:GO:0061621)
  Modifiers: None
RID: 55451 (;State transition'):
  Reactants: glutathione (annotations: CHEMBL_COMPOUND:CHEMBL1543,CHEBI:CHEBI:16856,HMDB:HMDB0000125,KEGG_COMPOUND:C00051,WIKIPEDIA:Glutathione,CHEMSPIDER:111188,CAS:70-18-8,MESH_2012:D005978,PUBCHEM:124886); hydrogen peroxide (annotations: PUBCHEM:784,HMDB:HMDB0003125,KEGG_COMPOUND:C00027,MESH_2012:D006861,CHEBI:CHEBI:16240,WIKIPEDIA:Hydrogen peroxide,CAS:7722-84-1,CHEMBL_COMPOUND:CHEMBL71595,CHEMSPIDER:763)
  Products: glutathione disulfide (annotations: KEGG_COMPOUND:C00127,CHEBI:CHEBI:17858,HMDB:HMDB0003337,PUBCHEM:975,CAS:27025-41-8,WIKIPEDIA:Glutathione disulfide,CHEMBL_COMPOUND:CHEMBL1372,CHEMSPIDER:950); H2O (annotations: HMDB:HMDB0002111,CHEBI:CHEBI:15377,PUBCHEM:962,CHEMSPIDER:937,MESH_2012:D014867,WIKIPEDIA:Water,CAS:7732-18-5,CHEMBL_COMPOUND:CHEMBL1098659,KEGG_COMPOUND:C00001)
  Modifiers: GPX1 (annotations: ENTREZ:2876,HGNC:4553,,UNIPROT:P07203,HGNC_SYMBOL:GPX1,REFSEQ:NM_000581)
  (References: REACTOME:REACT_264249)
RID: 55113 (;Known transition omitted'):
  Reactants: Chylomicron (annotations: GO:GO:0042627)
  Products: Chylomicron remnant (annotations: GO:GO:0034360)
  Modifiers: None
  (References: WIKIPATHWAYS:WP5304)
RID: 55882 (;State transition'):
  Reactants: Gutamate (annotations: CHEBI:CHEBI:18237)
  Products: α-Ketogluatarate (annotations: CHEBI:CHEBI:30915); ammonium (annotations: CHEBI:CHEBI:28938);  NADPH (annotations: CHEBI:CHEBI:57783,CHEBI:CHEBI:16474)
  Modifiers: GLUD
RID: 56001 (;State transition'):
  Reactants: Acetaldehyde (annotations: CHEBI:CHEBI:15343)
  Products: Acetyl-CoA (annotations: CHEBI:CHEBI:15351,CHEBI:CHEBI:57288)
  Modifiers: ACSS2 (formerSymbols: ACAS2) (annotations: ENTREZ:55902,HGNC_SYMBOL:ACSS2,,REFSEQ:NM_018677,HGNC:15814,UNIPROT:Q9NR19)
RID: 55721 (;Positive influence'):
  Reactants: RXRA (annotations: UNIPROT:P19793,,HGNC:10477,REFSEQ:NM_002957,ENTREZ:6256,HGNC_SYMBOL:RXRA)
  Products: NR1I3 (annotations: ENTREZ:9970,UNIPROT:Q14994,,HGNC:7969,REFSEQ:NM_001077469,HGNC_SYMBOL:NR1I3)
  Modifiers: None
RID: 55192 (;State transition'):
  Reactants: 24,25-Dihydrolanosterol (annotations: CHEBI:CHEBI:28113)
  Products: Dihydro-FF-MAS (annotations: CHEBI:CHEBI:78904)
  Modifiers: CYP51A1 (formerSymbols: CYP51) (annotations: UNIPROT:Q16850,,HGNC_SYMBOL:CYP51A1,ENTREZ:1595,HGNC:2649,REFSEQ:NM_000786)
  (References: WIKIPATHWAYS:WP4718|DOI:10.1016/B978-0-12-824048-9.00005-5)
RID: 56075 (;Positive influence'):
  Reactants: CGI-58 (annotations: )
  Products: PNPLA3 (formerSymbols: ADPN,C22orf20) (annotations: UNIPROT:Q9NST1,ENTREZ:80339,REFSEQ:NM_025225,,HGNC:18590,HGNC_SYMBOL:PNPLA3)
  Modifiers: None
RID: 56217 (;State transition'):
  Reactants: FBP1 (formerSymbols: FBP) (annotations: HGNC_SYMBOL:FBP1,UNIPROT:P09467,REFSEQ:NM_000507,PUBMED:31284506,HGNC:3606,ENTREZ:2203,)
  Products: FBP1 (formerSymbols: FBP) (annotations: HGNC_SYMBOL:FBP1,UNIPROT:P09467,REFSEQ:NM_000507,PUBMED:31284506,HGNC:3606,ENTREZ:2203,)
  Modifiers: None
RID: 55835 (;State transition'):
  Reactants: Acetyl-CoA (annotations: CHEBI:CHEBI:15351,CHEBI:CHEBI:57288); Acyl-CoA (annotations: CHEBI:CHEBI:17984)
  Products: 3-oxoacyl-CoA (annotations: CHEBI:CHEBI:15489,CHEBI:CHEBI:90726); CoA (annotations: CHEBI:CHEBI:15346)
  Modifiers: ACAA
RID: 55464 (;Positive influence'):
  Reactants: RPS6KB2 (annotations: REFSEQ:NM_003952,HGNC:10437,ENTREZ:6199,,UNIPROT:Q9UBS0,HGNC_SYMBOL:RPS6KB2)
  Products: Cell Proliferation (annotations: GO:GO:0072574)
  Modifiers: None
RID: 55397 (PDmap:re578.0;State transition'):
  Reactants: hydrogen peroxide (annotations: PUBCHEM:784,HMDB:HMDB0003125,KEGG_COMPOUND:C00027,MESH_2012:D006861,CHEBI:CHEBI:16240,WIKIPEDIA:Hydrogen peroxide,CAS:7722-84-1,CHEMBL_COMPOUND:CHEMBL71595,CHEMSPIDER:763); TXN (annotations: ENTREZ:7295,UNIPROT:P10599,HGNC:12435,,REFSEQ:NM_001244938,HGNC_SYMBOL:TXN)
  Products: H2O (annotations: HMDB:HMDB0002111,CHEBI:CHEBI:15377,PUBCHEM:962,CHEMSPIDER:937,MESH_2012:D014867,WIKIPEDIA:Water,CAS:7732-18-5,CHEMBL_COMPOUND:CHEMBL1098659,KEGG_COMPOUND:C00001); TXN (annotations: ENTREZ:7295,UNIPROT:P10599,HGNC:12435,,REFSEQ:NM_001244938,HGNC_SYMBOL:TXN)
  Modifiers: PRDX1 (formerSymbols: PAGA) (annotations: UNIPROT:Q06830,REFSEQ:NM_181697,ENTREZ:5052,HGNC:9352,,HGNC_SYMBOL:PRDX1); PRDX2 (formerSymbols: TDPX1) (annotations: ENTREZ:7001,REFSEQ:NM_005809,UNIPROT:P32119,,HGNC:9353,HGNC_SYMBOL:PRDX2); PRDX5 (annotations: UNIPROT:P30044,REFSEQ:NM_181651,,HGNC_SYMBOL:PRDX5,HGNC:9355,ENTREZ:25824); PRDX6 (annotations: HGNC:16753,REFSEQ:NM_004905,,HGNC_SYMBOL:PRDX6,ENTREZ:9588,UNIPROT:P30041)
  (References: PUBMED:19427899|PUBMED:23939310)
RID: 55319 (;State transition'):
  Reactants: CCS:Zn2+:Cu1+:SOD1:Zn2+
  Products: SOD1:Zn2+:Cu2+; CCS:Zn2+:Cu1+
  Modifiers: CCS:Zn2+:Cu1+:SOD1:Zn2+
  (References: REACTOME:REACT_264249)
RID: 56153 (;State transition'):
  Reactants: Serine (annotations: CHEBI:CHEBI:17822,CHEBI:CHEBI:17115)
  Products: Pyruvate (annotations: CHEBI:CHEBI:15361); ammonia (annotations: CHEBI:CHEBI:16134)
  Modifiers: SDS (annotations: REFSEQ:NM_006843,UNIPROT:P20132,HGNC_SYMBOL:SDS,ENTREZ:10993,HGNC:10691,)
RID: 55587 (;Positive influence'):
  Reactants: NFE2L2 (annotations: UNIPROT:Q16236,,PUBMED:28416361,ENTREZ:4780,REFSEQ:NM_006164,HGNC:7782,HGNC_SYMBOL:NFE2L2)
  Products: ME1 (annotations: HGNC:6983,REFSEQ:NM_002395,,ENTREZ:4199,UNIPROT:P48163,HGNC_SYMBOL:ME1)
  Modifiers: None
RID: 55843 (;State transition'):
  Reactants: Fatty Acid (annotations: CHEBI:CHEBI:35366)
  Products: Acyl-CoA (annotations: CHEBI:CHEBI:17984)
  Modifiers: ACSM
RID: 55253 (;State transition'):
  Reactants: palmitate (annotations: HMDB:HMDB0000220,PUBCHEM:985,KEGG_COMPOUND:C00249,WIKIPEDIA:Palmitic acid,CHEBI:CHEBI:7896,CAS:57-10-3,CHEMBL_COMPOUND:CHEMBL82293,CHEMSPIDER:960,CHEBI:CHEBI:15756,REACTOME:REACT_3374.1)
  Products: 3-ketoacyl-CoA (annotations: CHEBI:CHEBI:57347)
  Modifiers: ACAA2 (annotations: HGNC_SYMBOL:ACAA2,HGNC:83,,REFSEQ:NM_006111,UNIPROT:P42765,ENTREZ:10449)
  (References: WIKIPATHWAYS:WP357)
RID: 56152 (;State transition'):
  Reactants: Mitochondrial Metabolism
  Products: Citrate (annotations: CHEBI:CHEBI:16947,CHEBI:CHEBI:133748,CHEBI:CHEBI:50744)
  Modifiers: None
RID: 56049 (;Positive influence'):
  Reactants: NR1H4 (annotations: ,ENTREZ:9971,HGNC:7967,UNIPROT:Q96RI1,REFSEQ:NM_005123,HGNC_SYMBOL:NR1H4)
  Products: IRS2 (annotations: UNIPROT:Q9Y4H2,HGNC:6126,ENTREZ:8660,HGNC_SYMBOL:IRS2,REFSEQ:NM_003749,)
  Modifiers: None
RID: 55638 (;State transition'):
  Reactants: Very Long Fatty Acids-CoA
  Products: (2E)-very long FA-CoA (annotations: CHEBI:CHEBI:143004)
  Modifiers: ACOX (annotations: PUBMED:26451809)
RID: 55085 (;State transition'):
  Reactants: Fatty Acids
  Products: Acyl-CoA
  Modifiers: ACSL
RID: 55220 (;Transcription'):
  Reactants: ACAT2 (annotations: ENTREZ:39,HGNC:94,HGNC_SYMBOL:ACAT2,REFSEQ:NM_005891,UNIPROT:Q9BWD1,)
  Products: ACAT2 (annotations: ENTREZ:39,HGNC:94,HGNC_SYMBOL:ACAT2,REFSEQ:NM_005891,UNIPROT:Q9BWD1,)
  Modifiers: SREBF2 (annotations: HGNC:11290,REFSEQ:NM_004599,UNIPROT:Q12772,,HGNC_SYMBOL:SREBF2,ENTREZ:6721)
  (References: WIKIPATHWAYS:WP4718)
RID: 55291 (PDmap:re387.0;State transition'):
  Reactants: (S)-2-hydroxyglutaric acid (annotations: REACTOME:REACT_25542.1,CHEBI:CHEBI:32797); FAD (annotations: KEGG_COMPOUND:C00016,CHEMBL_COMPOUND:CHEMBL1232653,WIKIPEDIA:FAD,CHEMSPIDER:559059,HMDB:HMDB0001248,PUBCHEM:643975,CHEBI:CHEBI:16238,CAS:146-14-5)
  Products: 2-oxoglutaric acid (annotations: KEGG_COMPOUND:C00026,REACTOME:REACT_3871.1,CHEBI:CHEBI:30915,CAS:328-50-7,MESH_2012:C029743,PUBCHEM:51,CHEMSPIDER:50,HMDB:HMDB0000208,WIKIPEDIA:Alpha-Ketoglutaric_acid); FADH2 (annotations: CHEBI:CHEBI:17877,HMDB:HMDB0001197,CHEMBL_COMPOUND:CHEMBL1232653,WIKIPEDIA:FADH,PUBCHEM:446013,CHEMSPIDER:393487,KEGG_COMPOUND:C01352,CAS:146-14-5)
  Modifiers: L2HGDH (formerSymbols: C14orf160) (annotations: REFSEQ:NM_024884,UNIPROT:Q9H9P8,HGNC:20499,ENTREZ:79944,,HGNC_SYMBOL:L2HGDH)
  (References: PUBMED:16005139|PUBMED:15385440|REACTOME:REACT_24926.2|PUBMED:15548604)
RID: 55423 (;State transition'):
  Reactants: NAD(+) (annotations: KEGG_COMPOUND:C00003,CAS:53-84-9,PUBCHEM:5893,CHEMSPIDER:5682,REACTOME:REACT_4970.1,CHEBI:CHEBI:15846,HMDB:HMDB0000902,WIKIPEDIA:NAD)
  Products: NADH (annotations: REACTOME:REACT_2390.1,KEGG_COMPOUND:C00004,HMDB:HMDB0001487,CHEMSPIDER:903,WIKIPEDIA:NADH,CAS:58-68-4,CHEBI:CHEBI:16908,PUBCHEM:928,CHEMBL_COMPOUND:CHEMBL1628272,MESH_2012:D009243)
  Modifiers: malate-aspartate shuttle (annotations: GO:GO:0043490)
  (References: PUBMED:23986233|PUBMED:25809592|PUBMED:23216354|PUBMED:16368075)
RID: 55888 (;State transition'):
  Reactants: UDP-Glucose (annotations: CHEBI:CHEBI:18066)
  Products: UDP-Glucuronate (annotations: CHEBI:CHEBI:17200)
  Modifiers: UGDH (annotations: HGNC:12525,ENTREZ:7358,UNIPROT:O60701,REFSEQ:NM_003359,HGNC_SYMBOL:UGDH,)
RID: 55501 (;State transition'):
  Reactants: GSK3B (annotations: HGNC_SYMBOL:GSK3B,ENTREZ:2932,PUBMED:28416361,,HGNC:4617,UNIPROT:P49841,REFSEQ:NM_001146156)
  Products: GSK3B (annotations: HGNC_SYMBOL:GSK3B,ENTREZ:2932,PUBMED:28416361,,HGNC:4617,UNIPROT:P49841,REFSEQ:NM_001146156)
  Modifiers: None
RID: 55378 (;State transition'):
  Reactants: O2 (annotations: CHEBI:CHEBI:15379,KEGG_COMPOUND:C00007,HMDB:HMDB0001377,PUBCHEM:977,CHEMSPIDER:952,CAS:7782-44-7,WIKIPEDIA:Oxygen)
  Products: superoxide (annotations: HMDB:HMDB0002168,WIKIPEDIA:Superoxide,PUBCHEM:5359597,CHEMSPIDER:4514331,KEGG_COMPOUND:C00704,CHEBI:CHEBI:18421,CAS:11062-77-4)
  Modifiers: ubiquinol (annotations: CHEBI:CHEBI:17976)
  (References: PUBMED:19427899)
RID: 55170 (;Transcription'):
  Reactants: ABCG1 (annotations: HGNC_SYMBOL:ABCG1,ENTREZ:9619,,UNIPROT:P45844,REFSEQ:NM_207174,HGNC:73)
  Products: ABCG1 (annotations: HGNC_SYMBOL:ABCG1,ENTREZ:9619,,UNIPROT:P45844,REFSEQ:NM_207174,HGNC:73)
  Modifiers: SREBF1 (annotations: UNIPROT:P36956,REFSEQ:NM_004176,ENTREZ:6720,HGNC:11289,HGNC_SYMBOL:SREBF1,)
  (References: WIKIPATHWAYS:WP4718)
RID: 55248 (PDmap:re523.0;State transition'):
  Reactants: trans-dec-2-enoyl-CoA (annotations: CHEMSPIDER:4444334,CHEBI:CHEBI:10723,KEGG_COMPOUND:C05275,CAS:10018-95-8,REACTOME:REACT_3903.1,PUBCHEM:5280768,HMDB:HMDB0003948)
  Products: (S)-3-hydroxydecanoyl-CoA (annotations: CHEBI:CHEBI:28325,CHEMSPIDER:17220838,REACTOME:REACT_3098.1,PUBCHEM:16061159,CAS:6245-70-1,KEGG_COMPOUND:C05264,HMDB:HMDB0003938)
  Modifiers: ECHS1 (annotations: HGNC_SYMBOL:ECHS1,,ENTREZ:1892,UNIPROT:P30084,HGNC:3151,REFSEQ:NM_004092)
  (References: REACTOME:REACT_583.2|PUBMED:13295248)
RID: 55636 (;Positive influence'):
  Reactants: CD36 (annotations: HGNC:1663,REFSEQ:NM_001001547,HGNC_SYMBOL:CD36,PUBMED:26451809,ENTREZ:948,,UNIPROT:P16671,PUBMED:18477307)
  Products: Fatty Acid Transport (annotations: WIKIPATHWAYS:WP5061)
  Modifiers: None
RID: 55768 (;Negative influence'):
  Reactants: NR1I3 (annotations: ENTREZ:9970,UNIPROT:Q14994,,HGNC:7969,REFSEQ:NM_001077469,HGNC_SYMBOL:NR1I3)
  Products: PPARA (formerSymbols: PPAR) (annotations: HGNC_SYMBOL:PPARA,ENTREZ:5465,REFSEQ:NM_001001928,,PUBMED:26451809,UNIPROT:Q07869,HGNC:9232)
  Modifiers: None
RID: 55373 (PDmap:re468.0;State transition'):
  Reactants: acetyl-CoA (annotations: CHEBI:CHEBI:15351,WIKIPEDIA:Acetyl-CoA,HMDB:HMDB0001206,CHEMSPIDER:392413,PUBCHEM:444493,REACTOME:REACT_3839.1,CAS:72-89-9,KEGG_COMPOUND:C00024)
  Products: acetoacetyl-CoA (annotations: HMDB:HMDB0001484,CHEBI:CHEBI:15345,PUBCHEM:439214,CHEMSPIDER:388353,CAS:1420-36-6,REACTOME:REACT_2705.1,KEGG_COMPOUND:C00332,WIKIPEDIA:Acetoacetyl-CoA); coenzyme A (annotations: CHEBI:CHEBI:15346,REACTOME:REACT_3654.2)
  Modifiers: ACAT1 (formerSymbols: ACAT) (annotations: ,ENTREZ:38,HGNC_SYMBOL:ACAT1,UNIPROT:P24752,HGNC:93,REFSEQ:NM_000019)
  (References: KEGG_REACTION:R00238|REACTOME:REACT_47.3|PUBMED:3709573)
RID: 56120 (;Known transition omitted'):
  Reactants: IDL
  Products: LDL
  Modifiers: None
RID: 55773 (;State transition'):
  Reactants: HX-CoA
  Products: Trans-Hex-2-enoyl-CoA (annotations: CHEBI:CHEBI:28706)
  Modifiers: None
RID: 55487 (;Positive influence'):
  Reactants: PI3K cascade (annotations: GO:GO:0014065)
  Products: AKT1 (annotations: ENTREZ:207,HGNC:391,PUBMED:28416361,HGNC_SYMBOL:AKT1,REFSEQ:NM_005163,UNIPROT:P31749,)
  Modifiers: None
RID: 55498 (;Positive influence'):
  Reactants: AKT1 (annotations: ENTREZ:207,HGNC:391,PUBMED:28416361,HGNC_SYMBOL:AKT1,REFSEQ:NM_005163,UNIPROT:P31749,)
  Products: mTORC1 (annotations: GO:GO:0031931)
  Modifiers: None
  (References: PUBMED:19143635|PUBMED:23802099)
RID: 55477 (;Reduced trigger'):
  Reactants: IRS2 (annotations: UNIPROT:Q9Y4H2,HGNC:6126,ENTREZ:8660,HGNC_SYMBOL:IRS2,,REFSEQ:NM_003749)
  Products: PI3K
  Modifiers: None
RID: 55794 (;Negative influence'):
  Reactants: RPS6KB1 (formerSymbols: STK14A) (annotations: HGNC:10436,UNIPROT:P23443,ENTREZ:6198,,HGNC_SYMBOL:RPS6KB1,REFSEQ:NM_003161)
  Products: mTORC2 (annotations: GO:GO:0031932,PUBMED:28416361)
  Modifiers: None
  (References: PUBMED:19963289)
RID: 55876 (;Positive influence'):
  Reactants: NR3C1 (formerSymbols: GRL) (annotations: HGNC_SYMBOL:NR3C1,REFSEQ:NM_000176,,HGNC:7978,ENTREZ:2908,PUBMED:26451809,UNIPROT:P04150)
  Products: Glucogenolysis
  Modifiers: None
RID: 55105 (;Known transition omitted'):
  Reactants: LDL (annotations: GO:GO:0034362)
  Products: Cholesterol ester (annotations: CHEBI:CHEBI:17002)
  Modifiers: None
RID: 55699 (;State transition'):
  Reactants: FAPP (annotations: CHEBI:CHEBI:50277)
  Products: Presqualene diphosphate (annotations: CHEBI:CHEBI:15442)
  Modifiers: FDFT1 (annotations: HGNC_SYMBOL:FDFT1,REFSEQ:NM_001287742,,UNIPROT:P37268,ENTREZ:2222,HGNC:3629)
RID: 55195 (;Known transition omitted'):
  Reactants: T-MAS (annotations: CHEBI:CHEBI:18364)
  Products: Zymosterol (annotations: CHEBI:CHEBI:18252)
  Modifiers: MSMO1 (formerSymbols: SC4MOL) (annotations: REFSEQ:NM_006745,ENTREZ:6307,,HGNC:10545,UNIPROT:Q15800,HGNC_SYMBOL:MSMO1); NSDHL (annotations: ENTREZ:50814,HGNC:13398,HGNC_SYMBOL:NSDHL,REFSEQ:NM_015922,UNIPROT:Q15738,); HSD17B7 (annotations: ENTREZ:51478,UNIPROT:P56937,HGNC:5215,HGNC_SYMBOL:HSD17B7,REFSEQ:NM_016371,)
  (References: WIKIPATHWAYS:WP4718|DOI:10.1016/B978-0-12-824048-9.00005-5)
RID: 55353 (;Transport'):
  Reactants: hydrogen peroxide (annotations: PUBCHEM:784,HMDB:HMDB0003125,KEGG_COMPOUND:C00027,MESH_2012:D006861,CHEBI:CHEBI:16240,WIKIPEDIA:Hydrogen peroxide,CAS:7722-84-1,CHEMBL_COMPOUND:CHEMBL71595,CHEMSPIDER:763)
  Products: hydrogen peroxide (annotations: PUBCHEM:784,HMDB:HMDB0003125,KEGG_COMPOUND:C00027,MESH_2012:D006861,CHEBI:CHEBI:16240,WIKIPEDIA:Hydrogen peroxide,CAS:7722-84-1,CHEMBL_COMPOUND:CHEMBL71595,CHEMSPIDER:763)
  Modifiers: AQP8 (annotations: ,REFSEQ:NM_001169,HGNC:642,HGNC_SYMBOL:AQP8,ENTREZ:343,UNIPROT:O94778)
  (References: REACTOME:REACT_264249)
RID: 55415 (PDmap:re234.0;Positive influence'):
  Reactants: hydroxyl (annotations: CHEBI:CHEBI:29191)
  Products: ROS (annotations: CHEBI:CHEBI:26523)
  Modifiers: None
  (References: PUBMED:20045723)
RID: 56134 (;Known transition omitted'):
  Reactants: UDP-Glucose (annotations: CHEBI:CHEBI:18066); Galactose-1-Phosphate (annotations: CHEBI:CHEBI:17973)
  Products: Glucose-1-Phosphate (annotations: CHEBI:CHEBI:29042); UDP-Galactose (annotations: CHEBI:CHEBI:67119)
  Modifiers: GALT (annotations: REFSEQ:NM_000155,,HGNC:4135,HGNC_SYMBOL:GALT,ENTREZ:2592,UNIPROT:P07902)
RID: 55519 (;Positive influence'):
  Reactants: AKT1 (annotations: ENTREZ:207,HGNC:391,PUBMED:28416361,HGNC_SYMBOL:AKT1,REFSEQ:NM_005163,UNIPROT:P31749,)
  Products: RPS6KB2 (annotations: REFSEQ:NM_003952,HGNC:10437,ENTREZ:6199,,UNIPROT:Q9UBS0,HGNC_SYMBOL:RPS6KB2)
  Modifiers: None
RID: 55763 (;State transition'):
  Reactants: (S)-3-hydroxybutanoyl-CoA (annotations: CHEBI:CHEBI:15453,CHEBI:CHEBI:37050,CHEBI:CHEBI:57316)
  Products: Acetoacetyl-CoA (annotations: CHEBI:CHEBI:15345,CHEBI:CHEBI:57286)
  Modifiers: HADH (formerSymbols: HADHSC) (annotations: HGNC_SYMBOL:HADH,REFSEQ:NM_005327,,HGNC:4799,ENTREZ:3033,UNIPROT:Q16836); HSD17B10 (formerSymbols: HADH2,MRXS10) (annotations: HGNC_SYMBOL:HSD17B10,,UNIPROT:Q99714,REFSEQ:NM_004493,HGNC:4800,ENTREZ:3028)
RID: 55418 (PDmap:re694.0;State transition'):
  Reactants: paraquat monocation radical; O2 (annotations: CHEBI:CHEBI:15379,KEGG_COMPOUND:C00007,HMDB:HMDB0001377,PUBCHEM:977,CHEMSPIDER:952,CAS:7782-44-7,WIKIPEDIA:Oxygen)
  Products: paraquat dication; superoxide (annotations: HMDB:HMDB0002168,WIKIPEDIA:Superoxide,PUBCHEM:5359597,CHEMSPIDER:4514331,KEGG_COMPOUND:C00704,CHEBI:CHEBI:18421,CAS:11062-77-4)
  Modifiers: None
  (References: PUBMED:18039652)
RID: 55118 (;Transport'):
  Reactants: Fatty acyl-CoA (annotations: CHEBI:CHEBI:37554)
  Products: Microsomal Omega-Oxidation (annotations: WIKIPATHWAYS:WP206,GO:GO:0010430)
  Modifiers: DBI (annotations: HGNC_SYMBOL:DBI,ENTREZ:1622,,UNIPROT:P07108,PUBMED:18477307,HGNC:2690,REFSEQ:NM_020548)
RID: 55588 (;Positive influence'):
  Reactants: Xenobiotics
  Products: NR1I2 (annotations: ,HGNC_SYMBOL:NR1I2,HGNC:7968,REFSEQ:NM_003889,ENTREZ:8856,UNIPROT:O75469)
  Modifiers: None
RID: 55549 (;State transition'):
  Reactants: GYS
  Products: GYS
  Modifiers: PKA
RID: 55230 (;Known transition omitted'):
  Reactants: ACSL4 (formerSymbols: FACL4,MRX63,MRX68) (annotations: HGNC:3571,REFSEQ:NM_004458,ENTREZ:2182,HGNC_SYMBOL:ACSL4,UNIPROT:O60488,)
  Products: Fatty Acid Biosynthesis (annotations: WIKIPATHWAYS:WP4491,GO:GO:0006633)
  Modifiers: None
RID: 55917 (;State transition'):
  Reactants: GPAT4 (formerSymbols: AGPAT6) (annotations: ,HGNC_SYMBOL:GPAT4,ENTREZ:137964,UNIPROT:Q86UL3,HGNC:20880,REFSEQ:NM_178819)
  Products: GPAT4 (formerSymbols: AGPAT6) (annotations: ,HGNC_SYMBOL:GPAT4,ENTREZ:137964,UNIPROT:Q86UL3,HGNC:20880,REFSEQ:NM_178819)
  Modifiers: None
RID: 55897 (;Negative influence'):
  Reactants: NR3C1 (formerSymbols: GRL) (annotations: HGNC_SYMBOL:NR3C1,REFSEQ:NM_000176,,HGNC:7978,ENTREZ:2908,PUBMED:26451809,UNIPROT:P04150)
  Products: Mitochondrial Beta-Oxidation (annotations: WIKIPATHWAYS:WP143)
  Modifiers: None
RID: 55497 (;Negative influence'):
  Reactants: GSK3B (annotations: HGNC_SYMBOL:GSK3B,ENTREZ:2932,PUBMED:28416361,,HGNC:4617,UNIPROT:P49841,REFSEQ:NM_001146156)
  Products: Glycogen Synthesis (annotations: GO:GO:0005978,PUBMED:28416361)
  Modifiers: None
RID: 55333 (;State transition'):
  Reactants:  ; mtDNA encoded OXPHOS units (annotations: PUBMED:23149385,PUBMED:30030361)
  Products: complex IV (annotations: GO:GO:0045277)
  Modifiers: OXPHOS factors (annotations: PUBMED:23149385,PUBMED:30030361)
  (References: PUBMED:23149385|TAXONOMY:10090|PUBMED:30030361)
RID: 56073 (;Positive influence'):
  Reactants: Complex III
  Products: Cytochrome c (annotations: CHEBI:CHEBI:18070)
  Modifiers: None
RID: 55776 (;Known transition omitted'):
  Reactants: Pyruvate (annotations: CHEBI:CHEBI:15361); Glutamate (annotations: CHEBI:CHEBI:29987,CHEBI:CHEBI:14321,CHEBI:CHEBI:16015,CHEBI:CHEBI:18237)
  Products: Alanin (annotations: CHEBI:CHEBI:16449); α-Ketogluatarate (annotations: CHEBI:CHEBI:30915)
  Modifiers: GPT (annotations: HGNC_SYMBOL:GPT,ENTREZ:2875,HGNC:4552,,REFSEQ:NM_001382664,UNIPROT:P24298)
RID: 56129 (;State transition'):
  Reactants: Trans-Oct-2-enoyl-CoA (annotations: CHEBI:CHEBI:27537)
  Products: (S)-Hydroxyoctanoyl-CoA (annotations: CHEBI:CHEBI:28632)
  Modifiers: ECHS1 (annotations: HGNC_SYMBOL:ECHS1,,ENTREZ:1892,UNIPROT:P30084,HGNC:3151,REFSEQ:NM_004092)
RID: 55858 (;Known transition omitted'):
  Reactants: Lactose (annotations: CHEBI:CHEBI:17716,CHEBI:CHEBI:36218,CHEBI:CHEBI:36219); UDP (annotations: CHEBI:CHEBI:17659,CHEBI:CHEBI:58223)
  Products: UDP-Galactose (annotations: CHEBI:CHEBI:67119); Galactose (annotations: CHEBI:CHEBI:28260)
  Modifiers: None
RID: 55615 (;State transition'):
  Reactants: Propionyl-CoA (annotations: CHEBI:CHEBI:15539)
  Products: (S)-methylmalonyl-CoA (annotations: CHEBI:CHEBI:15466,CHEBI:CHEBI:57327)
  Modifiers: Propionyl-CoA carboxylase
RID: 55748 (;Positive influence'):
  Reactants: ACOX (annotations: PUBMED:26451809,PUBMED:18477307)
  Products: Peroxisomal Beta-Oxidation (annotations: WIKIPATHWAYS:WP1941)
  Modifiers: None
RID: 55737 (;Negative influence'):
  Reactants: PLIN2 (formerSymbols: ADFP) (annotations: HGNC:248,REFSEQ:NM_001122,,HGNC_SYMBOL:PLIN2,ENTREZ:123,UNIPROT:Q99541)
  Products: LIPC (annotations: HGNC_SYMBOL:LIPC,,ENTREZ:3990,REFSEQ:NM_000236,HGNC:6619,UNIPROT:P11150)
  Modifiers: None
RID: 55524 (;State transition'):
  Reactants: CREB1 (annotations: REFSEQ:NM_134442,HGNC:2345,ENTREZ:1385,HGNC_SYMBOL:CREB1,UNIPROT:P16220,)
  Products: CREB1 (annotations: REFSEQ:NM_134442,HGNC:2345,ENTREZ:1385,HGNC_SYMBOL:CREB1,UNIPROT:P16220,)
  Modifiers: PKA
RID: 55462 (;Positive influence'):
  Reactants: CDKN1A (formerSymbols: CDKN1) (annotations: REFSEQ:NM_078467,UNIPROT:P38936,HGNC_SYMBOL:CDKN1A,,HGNC:1784,ENTREZ:1026)
  Products: Cell Proliferation (annotations: GO:GO:0072574)
  Modifiers: None
RID: 55886 (;State transition'):
  Reactants: Dihydro-FF-MAS (annotations: CHEBI:CHEBI:78904)
  Products: Dihydro-T-MAS (annotations: CHEBI:CHEBI:87044)
  Modifiers: TM7SF2 (annotations: ,HGNC:11863,REFSEQ:NM_003273,UNIPROT:O76062,ENTREZ:7108,HGNC_SYMBOL:TM7SF2); LBR (annotations: HGNC_SYMBOL:LBR,UNIPROT:Q14739,REFSEQ:NM_002296,HGNC:6518,ENTREZ:3930,)
  (References: DOI:10.1016/B978-0-12-824048-9.00005-5)
RID: 55161 (;Known transition omitted'):
  Reactants: FASN (annotations: HGNC:3594,UNIPROT:P49327,REFSEQ:NM_004104,,ENTREZ:2194,HGNC_SYMBOL:FASN)
  Products: Fatty Acid Biosynthesis (annotations: WIKIPATHWAYS:WP4491,GO:GO:0006633)
  Modifiers: None
RID: 56124 (;Positive influence'):
  Reactants: INS (formerSymbols: IDDM1,IDDM2) (annotations: HGNC_SYMBOL:INS,PUBMED:28416361,HGNC:6081,REFSEQ:NM_000207,ENTREZ:3630,,UNIPROT:P01308)
  Products: GYS
  Modifiers: None
RID: 55919 (;Positive influence'):
  Reactants: PCK1 (annotations: ,PUBMED:28416361,HGNC:8724,UNIPROT:P35558,HGNC_SYMBOL:PCK1,REFSEQ:NM_002591,ENTREZ:5105)
  Products: Gluconeogenesis (annotations: GO:GO:0006094)
  Modifiers: None
RID: 55310 (;Transport'):
  Reactants: ADP (annotations: HMDB:HMDB0001341,WIKIPEDIA:ADP,CAS:58-64-0,KEGG_COMPOUND:C00008,PUBCHEM:6022,CHEBI:CHEBI:16761,CHEMBL_COMPOUND:CHEMBL14830,CHEMSPIDER:5800)
  Products: ADP (annotations: HMDB:HMDB0001341,WIKIPEDIA:ADP,CAS:58-64-0,KEGG_COMPOUND:C00008,PUBCHEM:6022,CHEBI:CHEBI:16761,CHEMBL_COMPOUND:CHEMBL14830,CHEMSPIDER:5800)
  Modifiers: None
RID: 55691 (;Truncation'):
  Reactants: Ketoacyl-CoA (annotations: CHEBI:CHEBI:57347)
  Products: Acyl-CoA (annotations: CHEBI:CHEBI:17984); Acetyl-CoA (annotations: CHEBI:CHEBI:15351,CHEBI:CHEBI:57288)
  Modifiers: ACAA
RID: 56157 (;State transition'):
  Reactants: Glucose-6-Phosphate (annotations: CHEBI:CHEBI:14314)
  Products: Glucose-1-Phosphate (annotations: CHEBI:CHEBI:29042)
  Modifiers: PGM1 (annotations: ,HGNC:8905,HGNC_SYMBOL:PGM1,REFSEQ:NM_002633,UNIPROT:P36871,ENTREZ:5236)
  (References: WIKIPATHWAYS:WP500)
RID: 56168 (;State transition'):
  Reactants: 3-Phosphoglycerate (annotations: CHEBI:CHEBI:17050,CHEBI:CHEBI:17794,CHEBI:CHEBI:57998)
  Products: 3-Phospho-Hydroxy-Pyruvate (annotations: CHEBI:CHEBI:18110)
  Modifiers: PHGDH (annotations: HGNC_SYMBOL:PHGDH,ENTREZ:26227,REFSEQ:NM_006623,HGNC:8923,UNIPROT:O43175,)
RID: 55859 (;Positive influence'):
  Reactants: Cortisol (annotations: CHEBI:CHEBI:17650)
  Products: NR3C1 (formerSymbols: GRL) (annotations: HGNC_SYMBOL:NR3C1,REFSEQ:NM_000176,,HGNC:7978,ENTREZ:2908,PUBMED:26451809,UNIPROT:P04150)
  Modifiers: None
RID: 55226 (;Transcription'):
  Reactants: ACSL4 (formerSymbols: FACL4,MRX63,MRX68) (annotations: HGNC:3571,REFSEQ:NM_004458,ENTREZ:2182,HGNC_SYMBOL:ACSL4,UNIPROT:O60488,)
  Products: ACSL4 (formerSymbols: FACL4,MRX63,MRX68) (annotations: HGNC:3571,REFSEQ:NM_004458,ENTREZ:2182,HGNC_SYMBOL:ACSL4,UNIPROT:O60488,)
  Modifiers: SREBF2 (annotations: HGNC:11290,REFSEQ:NM_004599,UNIPROT:Q12772,,HGNC_SYMBOL:SREBF2,ENTREZ:6721)
  (References: WIKIPATHWAYS:WP4718)
RID: 55088 (;State transition'):
  Reactants: Glycerol
  Products: Glycerol-3-P
  Modifiers: GK (annotations: ENTREZ:2710,HGNC:4289,REFSEQ:NM_000167,UNIPROT:P32189,HGNC_SYMBOL:GK,)
RID: 55819 (;Negative influence'):
  Reactants: NR1I2 (annotations: ,HGNC_SYMBOL:NR1I2,HGNC:7968,REFSEQ:NM_003889,ENTREZ:8856,UNIPROT:O75469)
  Products: FOXA2 (formerSymbols: HNF3B) (annotations: ENTREZ:3170,HGNC_SYMBOL:FOXA2,UNIPROT:Q9Y261,REFSEQ:NM_021784,,HGNC:5022)
  Modifiers: None
RID: 55507 (;State transition'):
  Reactants: FOXO1 (formerSymbols: FKHR,FOXO1A) (annotations: HGNC:3819,,REFSEQ:NM_002015,ENTREZ:2308,PUBMED:28416361,HGNC_SYMBOL:FOXO1,UNIPROT:Q12778)
  Products: FOXO1 (formerSymbols: FKHR,FOXO1A) (annotations: HGNC:3819,,REFSEQ:NM_002015,ENTREZ:2308,PUBMED:28416361,HGNC_SYMBOL:FOXO1,UNIPROT:Q12778)
  Modifiers: None
RID: 56201 (;State transition'):
  Reactants: Dihydroxyacetone-Phosphate (annotations: CHEBI:CHEBI:16108)
  Products: Triacylglyceride synthesis (annotations: WIKIPATHWAYS:WP325)
  Modifiers: None
RID: 55445 (;Transcription'):
  Reactants: mt DNA (annotations: GO:GO:0000262)
  Products: MT tRNAs (annotations: PUBMED:23149385)
  Modifiers: Mt-tRNA synthetase (annotations: PUBMED:23149385); TRMT1 (annotations: PUBMED:28752201,REFSEQ:NM_017722,HGNC_SYMBOL:TRMT1,ENTREZ:55621,,UNIPROT:Q9NXH9,EC:2.1.1.216,HGNC:25980)
  (References: PUBMED:23149385|TAXONOMY:10090|TAXONOMY:4891|DOI:10.1101/gad.316547.118)
RID: 55874 (;State transition'):
  Reactants: UDP-Glucose (annotations: CHEBI:CHEBI:18066)
  Products: Glycogen (n) (annotations: CHEBI:CHEBI:28087)
  Modifiers: GYG
RID: 55753 (;State transition'):
  Reactants: 2-trans-Dodecenoyl-CoA (annotations: CHEBI:CHEBI:15471)
  Products: (S)-3-Hydroxydodecanoyl-CoA (annotations: CHEBI:CHEBI:62558,CHEBI:CHEBI:27668)
  Modifiers: ECHS1 (annotations: HGNC_SYMBOL:ECHS1,,ENTREZ:1892,UNIPROT:P30084,HGNC:3151,REFSEQ:NM_004092)
RID: 55772 (;Positive influence'):
  Reactants: CD36 (annotations: HGNC:1663,REFSEQ:NM_001001547,HGNC_SYMBOL:CD36,,ENTREZ:948,UNIPROT:P16671,PUBMED:18477307)
  Products: SLC27A
  Modifiers: None
  (References: PUBMED:18477307)
RID: 55348 (PDmap:re584.0;State transition'):
  Reactants: hydrogen peroxide (annotations: PUBCHEM:784,HMDB:HMDB0003125,KEGG_COMPOUND:C00027,MESH_2012:D006861,CHEBI:CHEBI:16240,WIKIPEDIA:Hydrogen peroxide,CAS:7722-84-1,CHEMBL_COMPOUND:CHEMBL71595,CHEMSPIDER:763); hydroxyl (annotations: CHEBI:CHEBI:29191)
  Products: superoxide (annotations: HMDB:HMDB0002168,WIKIPEDIA:Superoxide,PUBCHEM:5359597,CHEMSPIDER:4514331,KEGG_COMPOUND:C00704,CHEBI:CHEBI:18421,CAS:11062-77-4); H2O (annotations: HMDB:HMDB0002111,CHEBI:CHEBI:15377,PUBCHEM:962,CHEMSPIDER:937,MESH_2012:D014867,WIKIPEDIA:Water,CAS:7732-18-5,CHEMBL_COMPOUND:CHEMBL1098659,KEGG_COMPOUND:C00001); H+ (annotations: CHEBI:CHEBI:15378)
  Modifiers: None
  (References: PUBMED:2172697)
RID: 55235 (;Positive influence'):
  Reactants: Cholesterol (annotations: CHEBI:CHEBI:16113,KEGG_COMPOUND:C00187)
  Products: Cell membranes (annotations: GO:GO:0044091)
  Modifiers: None
RID: 55440 (PDmap:re517.0;State transition'):
  Reactants: 3-oxotetradecanoyl-CoA (annotations: CAS:122364-86-7,KEGG_COMPOUND:C05261,REACTOME:REACT_5544.1,HMDB:HMDB0003935,CHEBI:CHEBI:28726,CHEMSPIDER:10140190,PUBCHEM:11966197)
  Products: lauroyl-CoA (annotations: CHEBI:CHEBI:15521,KEGG_COMPOUND:C01832,CHEMSPIDER:145018,CAS:6244-92-4,REACTOME:REACT_2800.1,HMDB:HMDB0003571,PUBCHEM:165436)
  Modifiers: trifunctional Protein
  (References: PUBMED:1550553|REACTOME:REACT_1519.2)
RID: 55339 (PDmap:re384.0;State transition'):
  Reactants: fumaric acid (annotations: REACTOME:REACT_5289.1,CHEBI:CHEBI:29806); H2O (annotations: HMDB:HMDB0002111,CHEBI:CHEBI:15377,PUBCHEM:962,CHEMSPIDER:937,MESH_2012:D014867,WIKIPEDIA:Water,CAS:7732-18-5,CHEMBL_COMPOUND:CHEMBL1098659,KEGG_COMPOUND:C00001)
  Products: (S)-malate(2-) (annotations: KEGG_COMPOUND:C00149,HMDB:HMDB0000156,PUBCHEM:222656,REACTOME:REACT_4778.1,CHEMSPIDER:193317,WIKIPEDIA:Apple acid,CHEBI:CHEBI:30797,CHEBI:CHEBI:15589,CAS:97-67-6)
  Modifiers: fumarate hydratase (annotations: REACTOME:REACT_21885.1)
  (References: REACTOME:REACT_1656.4|PUBMED:8200987)
RID: 55492 (;Positive influence'):
  Reactants: FOXO1 (formerSymbols: FKHR,FOXO1A) (annotations: HGNC:3819,,REFSEQ:NM_002015,ENTREZ:2308,PUBMED:28416361,HGNC_SYMBOL:FOXO1,UNIPROT:Q12778)
  Products: G6PC (annotations: PUBMED:28416361,)
  Modifiers: None
RID: 56041 (;Positive influence'):
  Reactants: SREBP-1c (annotations: PUBMED:26451809)
  Products: FASN (annotations: HGNC:3594,UNIPROT:P49327,REFSEQ:NM_004104,,ENTREZ:2194,HGNC_SYMBOL:FASN)
  Modifiers: None
RID: 55836 (;State transition'):
  Reactants: Cis,cis-3,6-Dodecadienoyl-CoA (annotations: CHEBI:CHEBI:28002)
  Products: Trans,cis-Lauro-2,6-dienoyl-CoA (annotations: CHEBI:CHEBI:28387)
  Modifiers: ECI1 (formerSymbols: DCI) (annotations: ENTREZ:1632,HGNC_SYMBOL:ECI1,UNIPROT:P42126,,HGNC:2703,REFSEQ:NM_001178029)
RID: 55622 (;State transition'):
  Reactants: Fibulose-5-Phosphate
  Products: Xylulosse-5-Phosphate (annotations: CHEBI:CHEBI:16332)
  Modifiers: RPE (annotations: ,ENTREZ:6120,UNIPROT:Q96AT9,REFSEQ:NM_006916,HGNC_SYMBOL:RPE,HGNC:10293)
RID: 55508 (;State transition'):
  Reactants: MDM2 (annotations: HGNC:6973,ENTREZ:4193,REFSEQ:NM_002392,,HGNC_SYMBOL:MDM2,UNIPROT:Q00987)
  Products: MDM2 (annotations: HGNC:6973,ENTREZ:4193,REFSEQ:NM_002392,,HGNC_SYMBOL:MDM2,UNIPROT:Q00987)
  Modifiers: AKT1 (annotations: ENTREZ:207,HGNC:391,PUBMED:28416361,HGNC_SYMBOL:AKT1,REFSEQ:NM_005163,UNIPROT:P31749,)
RID: 55386 (;State transition'):
  Reactants: CYCS (annotations: HGNC:19986,UNIPROT:P99999,ENTREZ:54205,HGNC_SYMBOL:CYCS,,REFSEQ:NM_018947); superoxide (annotations: HMDB:HMDB0002168,WIKIPEDIA:Superoxide,PUBCHEM:5359597,CHEMSPIDER:4514331,KEGG_COMPOUND:C00704,CHEBI:CHEBI:18421,CAS:11062-77-4)
  Products: CYCS (annotations: HGNC:19986,UNIPROT:P99999,ENTREZ:54205,HGNC_SYMBOL:CYCS,,REFSEQ:NM_018947); O2 (annotations: CHEBI:CHEBI:15379,KEGG_COMPOUND:C00007,HMDB:HMDB0001377,PUBCHEM:977,CHEMSPIDER:952,CAS:7782-44-7,WIKIPEDIA:Oxygen)
  Modifiers: None
  (References: REACTOME:REACT_264439)
RID: 55303 (PDmap:re383.0;State transition'):
  Reactants: (S)-malate(2-) (annotations: KEGG_COMPOUND:C00149,HMDB:HMDB0000156,PUBCHEM:222656,REACTOME:REACT_4778.1,CHEMSPIDER:193317,WIKIPEDIA:Apple acid,CHEBI:CHEBI:30797,CHEBI:CHEBI:15589,CAS:97-67-6)
  Products: fumaric acid (annotations: REACTOME:REACT_5289.1,CHEBI:CHEBI:29806); H2O (annotations: HMDB:HMDB0002111,CHEBI:CHEBI:15377,PUBCHEM:962,CHEMSPIDER:937,MESH_2012:D014867,WIKIPEDIA:Water,CAS:7732-18-5,CHEMBL_COMPOUND:CHEMBL1098659,KEGG_COMPOUND:C00001)
  Modifiers: fumarate hydratase (annotations: REACTOME:REACT_21885.1)
  (References: REACTOME:REACT_21360.1|PUBMED:8200987)
RID: 55895 (;State transition'):
  Reactants: SQNE (annotations: CHEBI:CHEBI:15440)
  Products: SQOX (annotations: CHEBI:CHEBI:78662)
  Modifiers: SQLE (annotations: HGNC:11279,,UNIPROT:Q14534,HGNC_SYMBOL:SQLE,ENTREZ:6713,REFSEQ:NM_003129)
  (References: DOI:10.1016/B978-0-12-824048-9.00005-5)
RID: 55122 (;Known transition omitted'):
  Reactants: LDL (annotations: GO:GO:0034362)
  Products: LP(a)
  Modifiers: None
  (References: WIKIPATHWAYS:WP5304)
RID: 55845 (;Positive influence'):
  Reactants: CASP9 (annotations: HGNC_SYMBOL:CASP9,REFSEQ:NM_032996,ENTREZ:842,,HGNC:1511,UNIPROT:P55211)
  Products: Apoptosis (annotations: GO:GO:1900117,GO:GO:0097194)
  Modifiers: None
RID: 55653 (;Positive influence'):
  Reactants: Ubiquinone (annotations: CHEBI:CHEBI:16389)
  Products: Complex III
  Modifiers: None
RID: 55844 (;Positive influence'):
  Reactants: PFKFB
  Products: Gluconeogenesis (annotations: GO:GO:0006094)
  Modifiers: None
RID: 55562 (;Positive influence'):
  Reactants: PPARG:PPARGC1A
  Products: CPT1
  Modifiers: None
RID: 56020 (;State transition'):
  Reactants: Oxalacetate (annotations: CHEBI:CHEBI:16452); Acetyl-CoA (annotations: CHEBI:CHEBI:15351,CHEBI:CHEBI:57288)
  Products: Citrate (annotations: CHEBI:CHEBI:16947,CHEBI:CHEBI:133748,CHEBI:CHEBI:50744)
  Modifiers: CS (annotations: HGNC_SYMBOL:CS,HGNC:2422,REFSEQ:NM_004077,,UNIPROT:O75390,ENTREZ:1431)
RID: 55782 (;State transition'):
  Reactants: mTORC1 (annotations: GO:GO:0031931)
  Products: mTORC1 (annotations: GO:GO:0031931)
  Modifiers: None
RID: 56033 (;State transition'):
  Reactants: Glycerol-3-Phosphate (annotations: CHEBI:CHEBI:15978)
  Products: Lysophosphatidic Acid (annotations: CHEBI:CHEBI:32957)
  Modifiers: GPAT4 (formerSymbols: AGPAT6) (annotations: ,HGNC_SYMBOL:GPAT4,ENTREZ:137964,UNIPROT:Q86UL3,HGNC:20880,REFSEQ:NM_178819)
RID: 55431 (PDmap:re547.0;State transition'):
  Reactants: citrate(3-) (annotations: KEGG_COMPOUND:C00158,PUBCHEM:311,CHEBI:CHEBI:30769,CHEBI:CHEBI:16947,WIKIPEDIA:Citric acid,REACTOME:REACT_2769.1,CHEMBL_COMPOUND:CHEMBL1261,CHEMSPIDER:305,HMDB:HMDB0000094,CAS:77-92-9)
  Products: acetyl-CoA (annotations: CHEBI:CHEBI:15351,WIKIPEDIA:Acetyl-CoA,HMDB:HMDB0001206,CHEMSPIDER:392413,PUBCHEM:444493,REACTOME:REACT_3839.1,CAS:72-89-9,KEGG_COMPOUND:C00024); oxaloacetate(2-) (annotations: PUBCHEM:970,CHEBI:CHEBI:30744,KEGG_COMPOUND:C00036,CAS:328-42-7,HMDB:HMDB0000223,CHEMSPIDER:945,REACTOME:REACT_5376.1,CHEBI:CHEBI:16452,WIKIPEDIA:Oxalacetic acid)
  Modifiers: ACLY (annotations: HGNC:115,REFSEQ:NM_001096,,ENTREZ:47,HGNC_SYMBOL:ACLY,UNIPROT:P53396)
  (References: PUBMED:1371749|REACTOME:REACT_1141.2)
RID: 55271 (PDmap:re466.0;State transition'):
  Reactants: acetoacetate (annotations: CAS:541-50-4,CHEBI:CHEBI:15344,CHEMBL_COMPOUND:CHEMBL1230762,WIKIPEDIA:Acetoacetic acid,PUBCHEM:96,REACTOME:REACT_5224.1,CHEMSPIDER:94,HMDB:HMDB0000060,KEGG_COMPOUND:C00164); succinyl-CoA (annotations: HMDB:HMDB0001022,CHEMSPIDER:388307,KEGG_COMPOUND:C00091,WIKIPEDIA:Succinyl-CoA,REACTOME:REACT_2852.1,CAS:604-98-8,CHEBI:CHEBI:15380,PUBCHEM:439161)
  Products: acetoacetyl-CoA (annotations: HMDB:HMDB0001484,CHEBI:CHEBI:15345,PUBCHEM:439214,CHEMSPIDER:388353,CAS:1420-36-6,REACTOME:REACT_2705.1,KEGG_COMPOUND:C00332,WIKIPEDIA:Acetoacetyl-CoA); succinic acid (annotations: KEGG_COMPOUND:C19806,CHEBI:CHEBI:45969,WIKIPEDIA:1,2,3-Propanetricarboxylic_acid,CHEBI:CHEBI:15741,PUBCHEM:14925,HMDB:HMDB0031193,REACTOME:REACT_2775.1,CAS:99-14-9,CHEMSPIDER:14220)
  Modifiers: OXCT1 (formerSymbols: OXCT) (annotations: ,HGNC:8527,ENTREZ:5019,HGNC_SYMBOL:OXCT1,REFSEQ:NM_000436,UNIPROT:P55809)
  (References: REACTOME:REACT_1796.4|KEGG_REACTION:R00410|PUBMED:8751852)
RID: 55668 (;Negative influence'):
  Reactants: PLIN2 (formerSymbols: ADFP) (annotations: HGNC:248,REFSEQ:NM_001122,,HGNC_SYMBOL:PLIN2,ENTREZ:123,UNIPROT:Q99541)
  Products: PNPLA2 (annotations: ,ENTREZ:57104,REFSEQ:NM_020376,HGNC:30802,UNIPROT:Q96AD5,HGNC_SYMBOL:PNPLA2)
  Modifiers: None
RID: 55258 (PDmap:re812.0;Transport'):
  Reactants: citrate(3-) (annotations: KEGG_COMPOUND:C00158,PUBCHEM:311,CHEBI:CHEBI:30769,CHEBI:CHEBI:16947,WIKIPEDIA:Citric acid,REACTOME:REACT_2769.1,CHEMBL_COMPOUND:CHEMBL1261,CHEMSPIDER:305,HMDB:HMDB0000094,CAS:77-92-9); (S)-malate(2-) (annotations: KEGG_COMPOUND:C00149,HMDB:HMDB0000156,PUBCHEM:222656,REACTOME:REACT_4778.1,CHEMSPIDER:193317,WIKIPEDIA:Apple acid,CHEBI:CHEBI:30797,CHEBI:CHEBI:15589,CAS:97-67-6)
  Products: citrate(3-) (annotations: KEGG_COMPOUND:C00158,PUBCHEM:311,CHEBI:CHEBI:30769,CHEBI:CHEBI:16947,WIKIPEDIA:Citric acid,REACTOME:REACT_2769.1,CHEMBL_COMPOUND:CHEMBL1261,CHEMSPIDER:305,HMDB:HMDB0000094,CAS:77-92-9); (S)-malate(2-) (annotations: KEGG_COMPOUND:C00149,HMDB:HMDB0000156,PUBCHEM:222656,REACTOME:REACT_4778.1,CHEMSPIDER:193317,WIKIPEDIA:Apple acid,CHEBI:CHEBI:30797,CHEBI:CHEBI:15589,CAS:97-67-6)
  Modifiers: SLC25A1 (formerSymbols: SLC20A3) (annotations: HGNC_SYMBOL:SLC25A1,REFSEQ:NM_005984,UNIPROT:P53007,,ENTREZ:6576,HGNC:10979)
  (References: REACTOME:REACT_1605.2)
RID: 56166 (;State transition'):
  Reactants: 3-Phosphoserine (annotations: CHEBI:CHEBI:15811)
  Products: Serine (annotations: CHEBI:CHEBI:17822,CHEBI:CHEBI:17115)
  Modifiers: PSPH (formerSymbols: PSP) (annotations: UNIPROT:P78330,HGNC:9577,REFSEQ:NM_004577,,HGNC_SYMBOL:PSPH,ENTREZ:5723)
RID: 56117 (;State transition'):
  Reactants: Pyruvate (annotations: CHEBI:CHEBI:15361)
  Products: Oxalacetate (annotations: CHEBI:CHEBI:16452)
  Modifiers: PC (annotations: HGNC_SYMBOL:PC,HGNC:8636,REFSEQ:NM_001040716,UNIPROT:P11498,,ENTREZ:5091)
RID: 55229 (;State transition'):
  Reactants: SREBF2 (annotations: HGNC:11290,REFSEQ:NM_004599,UNIPROT:Q12772,,HGNC_SYMBOL:SREBF2,ENTREZ:6721)
  Products: SREBF2 (annotations: HGNC:11290,REFSEQ:NM_004599,UNIPROT:Q12772,,HGNC_SYMBOL:SREBF2,ENTREZ:6721)
  Modifiers: Desmosterol (annotations: CHEBI:CHEBI:17737); 25-hydroxycholesterol
  (References: WIKIPATHWAYS:WP4718)
RID: 55377 (PDmap:re365.0;State transition'):
  Reactants: superoxide (annotations: HMDB:HMDB0002168,WIKIPEDIA:Superoxide,PUBCHEM:5359597,CHEMSPIDER:4514331,KEGG_COMPOUND:C00704,CHEBI:CHEBI:18421,CAS:11062-77-4); H+ (annotations: CHEBI:CHEBI:15378)
  Products: hydrogen peroxide (annotations: PUBCHEM:784,HMDB:HMDB0003125,KEGG_COMPOUND:C00027,MESH_2012:D006861,CHEBI:CHEBI:16240,WIKIPEDIA:Hydrogen peroxide,CAS:7722-84-1,CHEMBL_COMPOUND:CHEMBL71595,CHEMSPIDER:763); O2 (annotations: CHEBI:CHEBI:15379,KEGG_COMPOUND:C00007,HMDB:HMDB0001377,PUBCHEM:977,CHEMSPIDER:952,CAS:7782-44-7,WIKIPEDIA:Oxygen)
  Modifiers: SOD2 (annotations: ,HGNC:11180,ENTREZ:6648,,UNIPROT:P04179,REFSEQ:NM_000636,HGNC_SYMBOL:SOD2)
  (References: PUBMED:19427899|REACTOME:REACT_264249)
RID: 56046 (;Positive influence'):
  Reactants: PGD (annotations: UNIPROT:P52209,HGNC_SYMBOL:PGD,REFSEQ:NM_002631,,HGNC:8891,ENTREZ:5226)
  Products: Penthose Phosphate Pathway (annotations: WIKIPATHWAYS:WP134)
  Modifiers: None
RID: 56036 (;Positive influence'):
  Reactants: SREBP-1c (annotations: PUBMED:26451809)
  Products: ACACA (formerSymbols: ACAC,ACC) (annotations: REFSEQ:NM_198836,UNIPROT:Q13085,HGNC_SYMBOL:ACACA,ENTREZ:31,HGNC:84,)
  Modifiers: None
RID: 55245 (;State transition'):
  Reactants: complex II (annotations: GO:GO:0045281,REACTOME:REACT_3127.2); ubiquinol (annotations: CHEBI:CHEBI:17976)
  Products: complex II (annotations: GO:GO:0045281,REACTOME:REACT_3127.2,DOI:10.1021/bi901627u); ubiquinone (annotations: CHEMBL_COMPOUND:CHEMBL454801,HMDB:HMDB0002012,KEGG_COMPOUND:C00399,MESH_2012:D014451,CHEMSPIDER:4307,PUBCHEM:4462,CAS:727-81-1,WIKIPEDIA:Ubiquinone,CHEBI:CHEBI:16389)
  Modifiers: complex I (annotations: GO:GO:0005747)
  (References: PUBMED:25991374)
RID: 55602 (;Heterodimer association'):
  Reactants: Acetyl-CoA (annotations: CHEBI:CHEBI:15351,CHEBI:CHEBI:57288); Acetoacetyl-CoA (annotations: CHEBI:CHEBI:15345,CHEBI:CHEBI:57286)
  Products: HMG-CoA (annotations: CHEBI:CHEBI:15467)
  Modifiers: HMGCS2 (annotations: UNIPROT:P54868,HGNC:5008,HGNC_SYMBOL:HMGCS2,ENTREZ:3158,,REFSEQ:NM_005518)
RID: 55802 (;State transition'):
  Reactants: GSK3B (annotations: HGNC_SYMBOL:GSK3B,ENTREZ:2932,PUBMED:28416361,,HGNC:4617,UNIPROT:P49841,REFSEQ:NM_001146156)
  Products: GSK3B (annotations: HGNC_SYMBOL:GSK3B,ENTREZ:2932,PUBMED:28416361,,HGNC:4617,UNIPROT:P49841,REFSEQ:NM_001146156)
  Modifiers: AKT1 (annotations: ENTREZ:207,HGNC:391,PUBMED:28416361,HGNC_SYMBOL:AKT1,REFSEQ:NM_005163,UNIPROT:P31749,)
RID: 55988 (;Transport'):
  Reactants: Phospholipids
  Products: Phospholipids
  Modifiers: MTTP (formerSymbols: MTP) (annotations: HGNC:7467,REFSEQ:NM_000253,ENTREZ:4547,HGNC_SYMBOL:MTTP,,WIKIPATHWAYS:WP430,UNIPROT:P55157,PUBMED:18477307)
RID: 55722 (;Positive influence'):
  Reactants: CPT2 (formerSymbols: CPT1) (annotations: HGNC_SYMBOL:CPT2,PUBMED:19595610,HGNC:2330,REFSEQ:NM_000098,UNIPROT:P23786,,ENTREZ:1376)
  Products: Mitochondrial Beta-Oxidation (annotations: WIKIPATHWAYS:WP143)
  Modifiers: None
RID: 55367 (PDmap:re613.0;State transition'):
  Reactants: Arachidonic acid (annotations: PUBCHEM:444899,CHEMBL_COMPOUND:CHEMBL15594,HMDB:HMDB0001043,CHEMSPIDER:392692,KEGG_COMPOUND:C00219,CAS:506-32-1,WIKIPEDIA:Arachidonic acid,REACTOME:REACT_15656.1,CHEBI:CHEBI:15843,MESH_2012:D016718)
  Products: prostaglandin G2 (annotations: CHEBI:CHEBI:27647)
  Modifiers: PTGS1:heme; PTGS2:heme
  (References: REACTOME:REACT_147811.1|PUBMED:11729303|REACTOME:REACT_528.8)
RID: 55137 (;Heterodimer association'):
  Reactants: Fatty acyl-CoA (annotations: CHEBI:CHEBI:37554); DBI (annotations: HGNC_SYMBOL:DBI,ENTREZ:1622,,UNIPROT:P07108,PUBMED:18477307,HGNC:2690,REFSEQ:NM_020548)
  Products: DBI:FA
  Modifiers: None
  (References: PUBMED:12856180)
RID: 56164 (;State transition'):
  Reactants: Mitochondrial Metabolism
  Products: Aspartate (annotations: CHEBI:CHEBI:29995,CHEBI:CHEBI:72314)
  Modifiers: None
RID: 56070 (;Transport'):
  Reactants: VLDL
  Products: VLDL
  Modifiers: SORT1 (annotations: ENTREZ:6272,,REFSEQ:NM_002959,UNIPROT:Q99523,HGNC:11186,HGNC_SYMBOL:SORT1)
RID: 55531 (;State transition'):
  Reactants: Protein kinase cAMP-activated (PKA); cAMP
  Products: Protein kinase cAMP-activated (PKA); PKA; PKA
  Modifiers: None
RID: 55165 (;Transcription'):
  Reactants: ELOVL3 (annotations: UNIPROT:Q9HB03,HGNC:18047,ENTREZ:83401,HGNC_SYMBOL:ELOVL3,REFSEQ:NM_152310,)
  Products: ELOVL3 (annotations: UNIPROT:Q9HB03,HGNC:18047,ENTREZ:83401,HGNC_SYMBOL:ELOVL3,REFSEQ:NM_152310,)
  Modifiers: SREBF2 (annotations: HGNC:11290,REFSEQ:NM_004599,UNIPROT:Q12772,,HGNC_SYMBOL:SREBF2,ENTREZ:6721)
  (References: WIKIPATHWAYS:WP4718)
RID: 55978 (;State transition'):
  Reactants: (S)-Hydroxyoctanoyl-CoA (annotations: CHEBI:CHEBI:28632)
  Products: 3-Oxooctanoyl-CoA (annotations: CHEBI:CHEBI:62619,CHEBI:CHEBI:28264)
  Modifiers: HADH (formerSymbols: HADHSC) (annotations: HGNC_SYMBOL:HADH,REFSEQ:NM_005327,,HGNC:4799,ENTREZ:3033,UNIPROT:Q16836)
RID: 55288 (;Known transition omitted'):
  Reactants: SOD3 (annotations: HGNC:11181,REFSEQ:NM_003102,ENTREZ:6649,,HGNC_SYMBOL:SOD3,UNIPROT:P08294); ATP (annotations: CHEBI:CHEBI:15422,PUBCHEM:5957,CAS:56-65-5,MESH_2012:D000255,CHEMBL_COMPOUND:CHEMBL14249,CHEMSPIDER:5742,WIKIPEDIA:Adenosine triphosphate,HMDB:HMDB0000538,KEGG_COMPOUND:C00002); H2O (annotations: HMDB:HMDB0002111,CHEBI:CHEBI:15377,PUBCHEM:962,CHEMSPIDER:937,MESH_2012:D014867,WIKIPEDIA:Water,CAS:7732-18-5,CHEMBL_COMPOUND:CHEMBL1098659,KEGG_COMPOUND:C00001); Zn2+ (annotations: CHEBI:CHEBI:29105,VMH_METABOLITE:zn2); ATOX1:Cu1+
  Products: SOD3:Cu2+:Zn2+; ATOX1 (annotations: HGNC:798,UNIPROT:O00244,,HGNC_SYMBOL:ATOX1,REFSEQ:NM_004045,ENTREZ:475); ADP (annotations: HMDB:HMDB0001341,WIKIPEDIA:ADP,CAS:58-64-0,KEGG_COMPOUND:C00008,PUBCHEM:6022,CHEBI:CHEBI:16761,CHEMBL_COMPOUND:CHEMBL14830,CHEMSPIDER:5800); phosphate(3-) (annotations: WIKIPEDIA:Phosphate,PUBCHEM:1061,CAS:14265-44-2,KEGG_COMPOUND:C00009,CHEMSPIDER:1032,CHEBI:CHEBI:18367,REACTOME:REACT_5781.1,HMDB:HMDB0001429)
  Modifiers: ATP7A (formerSymbols: MNK) (annotations: HGNC_SYMBOL:ATP7A,ENTREZ:538,HGNC:869,REFSEQ:NM_000052,UNIPROT:Q04656,)
  (References: REACTOME:REACT_264249)
RID: 55342 (PDmap:re814.0;State transition'):
  Reactants: L-palmitoylcarnitine (annotations: PUBCHEM:11953816,CHEBI:CHEBI:17490,HMDB:HMDB0000222,CAS:2364-67-2,REACTOME:REACT_11789.2,KEGG_COMPOUND:C02990,CHEMSPIDER:10128117)
  Products: L-palmitoylcarnitine (annotations: PUBCHEM:11953816,CHEBI:CHEBI:17490,HMDB:HMDB0000222,CAS:2364-67-2,REACTOME:REACT_11789.2,KEGG_COMPOUND:C02990,CHEMSPIDER:10128117)
  Modifiers: SLC25A20 (formerSymbols: CACT) (annotations: REFSEQ:NM_000387,HGNC:1421,ENTREZ:788,,UNIPROT:O43772,HGNC_SYMBOL:SLC25A20); carnitine (annotations: CHEBI:CHEBI:17126,REACTOME:REACT_11423.1)
  (References: REACTOME:REACT_11180.3)
RID: 55250 (;Positive influence'):
  Reactants: PARK7 (annotations: HGNC:16369,HGNC_SYMBOL:PARK7,,REFSEQ:NM_007262,ENTREZ:11315,UNIPROT:Q99497)
  Products: complex I (annotations: GO:GO:0005747)
  Modifiers: None
  (References: PUBMED:19822128|PUBMED:23064436)
RID: 56192 (;Transport'):
  Reactants: Mitochondrial Metabolism
  Products: α-Ketogluatarate (annotations: CHEBI:CHEBI:30915)
  Modifiers: None
RID: 55797 (;Positive influence'):
  Reactants: PCK1 (annotations: ,PUBMED:28416361,HGNC:8724,UNIPROT:P35558,HGNC_SYMBOL:PCK1,REFSEQ:NM_002591,ENTREZ:5105)
  Products: Gluconeogenesis (annotations: GO:GO:0006094)
  Modifiers: None
RID: 55513 (;State transition'):
  Reactants: RPS6KB1 (formerSymbols: STK14A) (annotations: HGNC:10436,UNIPROT:P23443,ENTREZ:6198,,HGNC_SYMBOL:RPS6KB1,REFSEQ:NM_003161)
  Products: RPS6KB1 (formerSymbols: STK14A) (annotations: HGNC:10436,UNIPROT:P23443,ENTREZ:6198,,HGNC_SYMBOL:RPS6KB1,REFSEQ:NM_003161)
  Modifiers: mTORC1 (annotations: GO:GO:0031931)
RID: 55100 (;Transport'):
  Reactants: Long-chain Fatty Acids (annotations: CHEBI:CHEBI:15904)
  Products: Mitochondrial Beta-Oxidation (annotations: GO:GO:0006635,WIKIPATHWAYS:WP143)
  Modifiers: FABP
RID: 55140 (;State transition'):
  Reactants: Acetyl-CoA (annotations: CHEBI:CHEBI:15351)
  Products: Acetoacetyl-CoA (annotations: CHEBI:CHEBI:15345)
  Modifiers: ACAT2 (annotations: ENTREZ:39,HGNC:94,HGNC_SYMBOL:ACAT2,REFSEQ:NM_005891,UNIPROT:Q9BWD1,)
  (References: WIKIPATHWAYS:WP4718|DOI:10.1016/B978-0-12-824048-9.00005-5)
RID: 55829 (;State transition'):
  Reactants: Triacylglycerol (annotations: CHEBI:CHEBI:17855)
  Products: Diacylglycerol; Fatty Acid (annotations: CHEBI:CHEBI:35366)
  Modifiers: PNPLA2 (annotations: ,ENTREZ:57104,REFSEQ:NM_020376,HGNC:30802,UNIPROT:Q96AD5,HGNC_SYMBOL:PNPLA2)
RID: 55249 (;State transition'):
  Reactants: crotonoyl-ACP
  Products: butyryl-ACP (annotations: CHEBI:CHEBI:3247)
  Modifiers: FASN (annotations: HGNC:3594,UNIPROT:P49327,REFSEQ:NM_004104,,ENTREZ:2194,HGNC_SYMBOL:FASN)
  (References: WIKIPATHWAYS:WP357)
RID: 56052 (;State transition'):
  Reactants: Beta-ketoacyl-ACP
  Products: Beta-hydroxyacyl-ACP
  Modifiers: HSD17B12 (annotations: ENTREZ:51144,UNIPROT:Q53GQ0,HGNC_SYMBOL:HSD17B12,HGNC:18646,REFSEQ:NM_016142,)
RID: 55639 (;Positive influence'):
  Reactants: NFE2L2 (annotations: UNIPROT:Q16236,,PUBMED:28416361,ENTREZ:4780,REFSEQ:NM_006164,HGNC:7782,HGNC_SYMBOL:NFE2L2)
  Products: CYP4A11 (formerSymbols: CYP4A2) (annotations: ENTREZ:1579,HGNC:2642,UNIPROT:Q02928,REFSEQ:NM_000778,HGNC_SYMBOL:CYP4A11,)
  Modifiers: None
RID: 55265 (PDmap:re539.0;State transition'):
  Reactants: propionyl-CoA (annotations: HMDB:HMDB0001275,WIKIPEDIA:Propionyl-CoA,CHEMSPIDER:388310,CHEBI:CHEBI:15539,PUBCHEM:439164,KEGG_COMPOUND:C00100,CAS:317-66-8)
  Products: (S)-methylmalonyl-CoA (annotations: REACTOME:REACT_4910.1,CHEBI:CHEBI:15466,HMDB:HMDB0001269,WIKIPEDIA:Methylmalonyl-CoA,PUBCHEM:439291,CHEMSPIDER:388424,CAS:104809-02-1,KEGG_COMPOUND:C00683)
  Modifiers: proprionyl-CoA carboxylase (annotations: EC:6.4.1.3)
  (References: PUBMED:6765947|PUBMED:13752080|REACTOME:REACT_580.4|PUBMED:16023992)
RID: 55795 (;Transport'):
  Reactants: Fatty acyl-CoA
  Products: Fatty acyl-CoA
  Modifiers: DBI (annotations: HGNC_SYMBOL:DBI,ENTREZ:1622,,UNIPROT:P07108,PUBMED:18477307,HGNC:2690,REFSEQ:NM_020548)
  (References: PUBMED:18477307)
RID: 55662 (;Positive influence'):
  Reactants: FBP1 (formerSymbols: FBP) (annotations: HGNC_SYMBOL:FBP1,UNIPROT:P09467,REFSEQ:NM_000507,PUBMED:31284506,HGNC:3606,ENTREZ:2203,)
  Products: Gluconeogenesis (annotations: GO:GO:0006094)
  Modifiers: None
RID: 55905 (;Positive influence'):
  Reactants: SREBP-1c (annotations: PUBMED:26451809)
  Products: ACACB (annotations: UNIPROT:O00763,HGNC_SYMBOL:ACACB,HGNC:85,REFSEQ:NM_001093,ENTREZ:32,)
  Modifiers: None
RID: 55900 (;Positive influence'):
  Reactants: ESR1 (formerSymbols: ESR) (annotations: HGNC:3467,ENTREZ:2099,,REFSEQ:NM_000125,UNIPROT:P03372,HGNC_SYMBOL:ESR1)
  Products: ACOX1 (annotations: UNIPROT:Q15067,HGNC:119,,ENTREZ:51,HGNC_SYMBOL:ACOX1,REFSEQ:NM_001185039)
  Modifiers: None
RID: 55556 (;State transition'):
  Reactants: GYS
  Products: GYS
  Modifiers: None
RID: 55793 (;Transport'):
  Reactants: H+ (annotations: CHEBI:CHEBI:15378)
  Products: H+ (annotations: CHEBI:CHEBI:15378)
  Modifiers: UCP2 (formerSymbols: BMIQ4) (annotations: HGNC:12518,REFSEQ:NM_003355,HGNC_SYMBOL:UCP2,,ENTREZ:7351,UNIPROT:P55851,PUBMED:18477307)
RID: 55133 (;Known transition omitted'):
  Reactants: VLDL (annotations: GO:GO:0034361)
  Products: IDL (annotations: GO:GO:0034363)
  Modifiers: None
  (References: WIKIPATHWAYS:WP5304)
RID: 55179 (;State transition'):
  Reactants: Mevalonic acid (annotations: CHEBI:CHEBI:25351)
  Products: Mevalonate-P (annotations: CHEBI:CHEBI:25350)
  Modifiers: MVK (annotations: REFSEQ:NM_000431,HGNC_SYMBOL:MVK,HGNC:7530,ENTREZ:4598,,UNIPROT:Q03426)
  (References: WIKIPATHWAYS:WP4718|DOI:10.1016/B978-0-12-824048-9.00005-5)
RID: 55120 (;State transition'):
  Reactants: Cholesterol (annotations: CHEBI:CHEBI:16113,KEGG_COMPOUND:C00187)
  Products: Cholesterol ester (annotations: CHEBI:CHEBI:17002)
  Modifiers: SOAT
  (References: KEGG_PATHWAY:map04979|WIKIPATHWAYS:WP5304)
RID: 55421 (PDmap:re436.0;State transition'):
  Reactants: CYCS (annotations: HGNC:19986,UNIPROT:P99999,ENTREZ:54205,HGNC_SYMBOL:CYCS,,REFSEQ:NM_018947)
  Products: CYCS (annotations: HGNC:19986,UNIPROT:P99999,ENTREZ:54205,HGNC_SYMBOL:CYCS,,REFSEQ:NM_018947)
  Modifiers: SIRT5 (annotations: UNIPROT:Q9NXA8,HGNC_SYMBOL:SIRT5,HGNC:14933,ENTREZ:23408,,REFSEQ:NM_001193267)
  (References: PUBMED:18680753|PUBMED:21658599)
RID: 55798 (;State transition'):
  Reactants: PYGL (annotations: ENTREZ:5836,REFSEQ:NM_002863,HGNC_SYMBOL:PYGL,HGNC:9725,,UNIPROT:P06737)
  Products: PYGL (annotations: ENTREZ:5836,REFSEQ:NM_002863,HGNC_SYMBOL:PYGL,HGNC:9725,,UNIPROT:P06737)
  Modifiers: None
RID: 55891 (;Negative influence'):
  Reactants: NR1I3 (annotations: ENTREZ:9970,UNIPROT:Q14994,,HGNC:7969,REFSEQ:NM_001077469,HGNC_SYMBOL:NR1I3)
  Products: INSIG1 (annotations: REFSEQ:NM_198336,PUBMED:19595610,,ENTREZ:3638,UNIPROT:O15503,HGNC_SYMBOL:INSIG1,HGNC:6083)
  Modifiers: None
RID: 56191 (;Transport'):
  Reactants: Pyruvate (annotations: CHEBI:CHEBI:15361)
  Products: Pyruvate (annotations: CHEBI:CHEBI:15361)
  Modifiers: MPC (annotations: PUBMED:25748677)
  (References: WIKIPATHWAYS:WP534)
RID: 55666 (;Transport'):
  Reactants: Glutamate (annotations: CHEBI:CHEBI:29987,CHEBI:CHEBI:14321,CHEBI:CHEBI:16015,CHEBI:CHEBI:18237)
  Products: Glutamate (annotations: CHEBI:CHEBI:29987,CHEBI:CHEBI:14321,CHEBI:CHEBI:16015,CHEBI:CHEBI:18237)
  Modifiers: DIC
RID: 55227 (;State transition'):
  Reactants: SQOX (annotations: CHEBI:CHEBI:78662)
  Products: Diepoxy-Squalene (annotations: CHEBI:CHEBI:138307)
  Modifiers: SQLE (annotations: HGNC:11279,,UNIPROT:Q14534,HGNC_SYMBOL:SQLE,ENTREZ:6713,REFSEQ:NM_003129)
  (References: WIKIPATHWAYS:WP4718)
RID: 55511 (;State transition'):
  Reactants: IRS2 (annotations: UNIPROT:Q9Y4H2,HGNC:6126,ENTREZ:8660,HGNC_SYMBOL:IRS2,,REFSEQ:NM_003749)
  Products: IRS2 (annotations: UNIPROT:Q9Y4H2,HGNC:6126,ENTREZ:8660,HGNC_SYMBOL:IRS2,,REFSEQ:NM_003749)
  Modifiers: RPS6KB1 (formerSymbols: STK14A) (annotations: HGNC:10436,UNIPROT:P23443,ENTREZ:6198,,HGNC_SYMBOL:RPS6KB1,REFSEQ:NM_003161); MAPK14 (formerSymbols: CSBP1,CSBP2,CSPB1) (annotations: ,HGNC:6876,UNIPROT:Q16539,HGNC_SYMBOL:MAPK14,ENTREZ:1432,REFSEQ:NM_001315)
RID: 55889 (;State transition'):
  Reactants: Cholestadienol (annotations: CHEBI:CHEBI:145214)
  Products: 7-Dehydrodemosterol (annotations: CHEBI:CHEBI:27910)
  Modifiers: SC5D (formerSymbols: SC5DL) (annotations: ENTREZ:6309,HGNC:10547,HGNC_SYMBOL:SC5D,REFSEQ:NM_001024956,,UNIPROT:O75845)
  (References: DOI:10.1016/B978-0-12-824048-9.00005-5)
RID: 55925 (;State transition'):
  Reactants: Serine (annotations: CHEBI:CHEBI:17822,CHEBI:CHEBI:17115)
  Products: Pyruvate (annotations: CHEBI:CHEBI:15361); ammonia (annotations: CHEBI:CHEBI:16134)
  Modifiers: SDS (annotations: REFSEQ:NM_006843,UNIPROT:P20132,HGNC_SYMBOL:SDS,ENTREZ:10993,HGNC:10691,)
RID: 55821 (;State transition'):
  Reactants: cAMP (annotations: CHEBI:CHEBI:17489)
  Products: ATP (annotations: CHEBI:CHEBI:15422)
  Modifiers: PDE (annotations: )
  (References: PUBMED:24692138)
RID: 55766 (;Positive influence'):
  Reactants: ChREBP (annotations: PUBMED:26451809)
  Products: ACACA (formerSymbols: ACAC,ACC) (annotations: REFSEQ:NM_198836,UNIPROT:Q13085,HGNC_SYMBOL:ACACA,ENTREZ:31,HGNC:84,)
  Modifiers: None
RID: 55933 (;State transition'):
  Reactants: PKLR (annotations: HGNC_SYMBOL:PKLR,REFSEQ:NM_000298,HGNC:9020,UNIPROT:P30613,ENTREZ:5313,)
  Products: PKLR (annotations: HGNC_SYMBOL:PKLR,REFSEQ:NM_000298,PUBMED:31284506,HGNC:9020,UNIPROT:P30613,ENTREZ:5313,)
  Modifiers: None
RID: 55863 (;Positive influence'):
  Reactants: NR1B1
  Products: Lipid synthesis
  Modifiers: None
RID: 55381 (PDmap:re467.0;State transition'):
  Reactants: acetoacetyl-CoA (annotations: HMDB:HMDB0001484,CHEBI:CHEBI:15345,PUBCHEM:439214,CHEMSPIDER:388353,CAS:1420-36-6,REACTOME:REACT_2705.1,KEGG_COMPOUND:C00332,WIKIPEDIA:Acetoacetyl-CoA); acetyl-CoA (annotations: CHEBI:CHEBI:15351,WIKIPEDIA:Acetyl-CoA,HMDB:HMDB0001206,CHEMSPIDER:392413,PUBCHEM:444493,REACTOME:REACT_3839.1,CAS:72-89-9,KEGG_COMPOUND:C00024)
  Products: (3S)-3-hydroxy-3-methylglutaryl-CoA (annotations: KEGG_COMPOUND:C00356,CHEBI:CHEBI:15467,HMDB:HMDB0001375,CAS:1553-55-5,WIKIPEDIA:3-hydroxy-3-methylglutaryl-CoA,PUBCHEM:439218,CHEMSPIDER:388357); coenzyme A (annotations: CHEBI:CHEBI:15346,REACTOME:REACT_3654.2)
  Modifiers: HMGCS2 (annotations: UNIPROT:P54868,HGNC:5008,HGNC_SYMBOL:HMGCS2,ENTREZ:3158,,REFSEQ:NM_005518)
  (References: KEGG_REACTION:R01978|PUBMED:11479731|REACTOME:REACT_1099.4)
RID: 55287 (;State transition'):
  Reactants: complex II (annotations: GO:GO:0045281,REACTOME:REACT_3127.2,DOI:10.1021/bi901627u)
  Products: complex II (annotations: GO:GO:0045281,REACTOME:REACT_3127.2,DOI:10.1021/bi901627u)
  Modifiers: SIRT3 (annotations: ENTREZ:23410,HGNC_SYMBOL:SIRT3,UNIPROT:Q9NTG7,HGNC:14931,REFSEQ:NM_001017524,); OXPHOS factors (annotations: PUBMED:23149385,PUBMED:30030361)
  (References: PUBMED:20000467|PUBMED:21658599)
RID: 55993 (;Known transition omitted'):
  Reactants: Fatty acyl-carnitine
  Products: Fatty acyl-CoA
  Modifiers: None
RID: 56045 (;State transition'):
  Reactants: Presqualene diphosphate (annotations: CHEBI:CHEBI:15442)
  Products: Presqualene monophosphate  (annotations: CHEBI:CHEBI:134117)
  Modifiers: PLPP6 (formerSymbols: PPAPDC2) (annotations: HGNC_SYMBOL:PLPP6,ENTREZ:403313,,HGNC:23682,UNIPROT:Q8IY26,REFSEQ:NM_203453)
RID: 55322 (PDmap:re617.0;State transition'):
  Reactants: prostaglandin H2 (annotations: CHEBI:CHEBI:15554,WIKIPEDIA:Prostaglandin H2,PUBCHEM:445049,KEGG_COMPOUND:C00427,CAS:42935-17-1,CHEMSPIDER:392800,HMDB:HMDB0001381)
  Products: prostaglandin F2 alpha (annotations: CHEBI:CHEBI:15553,CAS:551-11-1,CHEMSPIDER:4446204,KEGG_COMPOUND:C00639,HMDB:HMDB0001139,PUBCHEM:5283078)
  Modifiers: AKR1C3 (formerSymbols: HSD17B5) (annotations: HGNC_SYMBOL:AKR1C3,,REFSEQ:NM_003739,ENTREZ:8644,HGNC:386,UNIPROT:P42330)
  (References: PUBMED:11729303)
RID: 55282 (PDmap:re541.0;State transition'):
  Reactants: (2-trans,4-cis)-deca-2,4-dienoyl-CoA (annotations: REACTOME:REACT_3866.1,CHEBI:CHEBI:29119)
  Products: trans-dec-3-enoyl-CoA (annotations: CHEBI:CHEBI:29126,REACTOME:REACT_3172.1)
  Modifiers: DECR1 (formerSymbols: DECR) (annotations: ENTREZ:1666,UNIPROT:Q16698,HGNC:2753,HGNC_SYMBOL:DECR1,REFSEQ:NM_001330575,)
  (References: REACTOME:REACT_164.1)
RID: 56051 (;Positive influence'):
  Reactants: Phenols (annotations: CHEBI:CHEBI:33853)
  Products: AHR (annotations: HGNC:348,HGNC_SYMBOL:AHR,,UNIPROT:P35869,REFSEQ:NM_001621,ENTREZ:196)
  Modifiers: None
RID: 55473 (;State transition'):
  Reactants: FOXO1 (formerSymbols: FKHR,FOXO1A) (annotations: HGNC:3819,,REFSEQ:NM_002015,ENTREZ:2308,PUBMED:28416361,HGNC_SYMBOL:FOXO1,UNIPROT:Q12778)
  Products: FOXO1 (formerSymbols: FKHR,FOXO1A) (annotations: HGNC:3819,,REFSEQ:NM_002015,ENTREZ:2308,PUBMED:28416361,HGNC_SYMBOL:FOXO1,UNIPROT:Q12778)
  Modifiers: AKT1 (annotations: ENTREZ:207,HGNC:391,PUBMED:28416361,HGNC_SYMBOL:AKT1,REFSEQ:NM_005163,UNIPROT:P31749,)
RID: 55697 (;Positive influence'):
  Reactants: CDKN1A (formerSymbols: CDKN1) (annotations: REFSEQ:NM_078467,UNIPROT:P38936,HGNC_SYMBOL:CDKN1A,,HGNC:1784,ENTREZ:1026)
  Products: Cell Proliferation (annotations: GO:GO:0072574)
  Modifiers: None
RID: 55438 (;Transport'):
  Reactants: citrate(3-) (annotations: KEGG_COMPOUND:C00158,PUBCHEM:311,CHEBI:CHEBI:30769,CHEBI:CHEBI:16947,WIKIPEDIA:Citric acid,REACTOME:REACT_2769.1,CHEMBL_COMPOUND:CHEMBL1261,CHEMSPIDER:305,HMDB:HMDB0000094,CAS:77-92-9)
  Products: citrate(3-) (annotations: KEGG_COMPOUND:C00158,PUBCHEM:311,CHEBI:CHEBI:30769,CHEBI:CHEBI:16947,WIKIPEDIA:Citric acid,REACTOME:REACT_2769.1,CHEMBL_COMPOUND:CHEMBL1261,CHEMSPIDER:305,HMDB:HMDB0000094,CAS:77-92-9)
  Modifiers: None
RID: 56083 (;State transition'):
  Reactants: Malate (annotations: CHEBI:CHEBI:15595,CHEBI:CHEBI:30797)
  Products: Oxalacetate (annotations: CHEBI:CHEBI:16452); NADH (annotations: CHEBI:CHEBI:16908)
  Modifiers: MDH2 (annotations: ,HGNC:6971,ENTREZ:4191,HGNC_SYMBOL:MDH2,REFSEQ:NM_005918,UNIPROT:P40926)
RID: 55788 (;State transition'):
  Reactants: Pyruvate (annotations: CHEBI:CHEBI:15361)
  Products: Acetyl-CoA (annotations: CHEBI:CHEBI:15351,CHEBI:CHEBI:57288)
  Modifiers: Pyruvate Dehydrogenase 1
RID: 55774 (;State transition'):
  Reactants: LNSOL (annotations: CHEBI:CHEBI:16521)
  Products: FF-MAS (annotations: CHEBI:CHEBI:17813)
  Modifiers: CYP51A1 (formerSymbols: CYP51) (annotations: UNIPROT:Q16850,,HGNC_SYMBOL:CYP51A1,ENTREZ:1595,HGNC:2649,REFSEQ:NM_000786)
  (References: DOI:10.1016/B978-0-12-824048-9.00005-5)
RID: 55432 (PDmap:re470.0;State transition'):
  Reactants: HMGCS2 (annotations: UNIPROT:P54868,HGNC:5008,HGNC_SYMBOL:HMGCS2,ENTREZ:3158,,REFSEQ:NM_005518)
  Products: HMGCS2 (annotations: UNIPROT:P54868,HGNC:5008,HGNC_SYMBOL:HMGCS2,ENTREZ:3158,,REFSEQ:NM_005518)
  Modifiers: SIRT3 (annotations: ENTREZ:23410,HGNC_SYMBOL:SIRT3,UNIPROT:Q9NTG7,HGNC:14931,REFSEQ:NM_001017524,)
  (References: PUBMED:21109197)
RID: 56068 (;State transition'):
  Reactants: Dihydroxyacetone-Phosphate (annotations: CHEBI:CHEBI:16108)
  Products: Glycerol-3-Phosphate (annotations: CHEBI:CHEBI:15978)
  Modifiers: GPD1 (annotations: ,UNIPROT:P21695,HGNC:4455,HGNC_SYMBOL:GPD1,ENTREZ:2819,REFSEQ:NM_001257199)
RID: 55989 (;Positive influence'):
  Reactants: SLC27A1 (annotations: ENTREZ:376497,UNIPROT:Q6PCB7,HGNC:10995,HGNC_SYMBOL:SLC27A1,REFSEQ:NM_198580,)
  Products: Fatty Acid Transport (annotations: WIKIPATHWAYS:WP5061)
  Modifiers: None
RID: 55469 (;Positive influence'):
  Reactants: GSK3B (annotations: HGNC_SYMBOL:GSK3B,ENTREZ:2932,PUBMED:28416361,,HGNC:4617,UNIPROT:P49841,REFSEQ:NM_001146156)
  Products: Apoptosis (annotations: GO:GO:1900117,GO:GO:0097194)
  Modifiers: None
RID: 56176 (;State transition'):
  Reactants: Malate (annotations: CHEBI:CHEBI:15595,CHEBI:CHEBI:30797)
  Products: Oxalacetate (annotations: CHEBI:CHEBI:16452)
  Modifiers: MDH1 (annotations: HGNC_SYMBOL:MDH1,UNIPROT:P40925,HGNC:6970,ENTREZ:4190,REFSEQ:NM_001316374,)
RID: 55349 (PDmap:re520.0;State transition'):
  Reactants: (S)-3-hydroxylauroyl-CoA (annotations: REACTOME:REACT_5323.1,KEGG_COMPOUND:C05262,HMDB:HMDB0003936,CAS:72059-49-5,CHEMSPIDER:389501,CHEBI:CHEBI:27668,PUBCHEM:440603)
  Products: 3-oxolauroyl-CoA (annotations: REACTOME:REACT_4368.1,CAS:78303-19-2,KEGG_COMPOUND:C05263,PUBCHEM:440604,CHEMSPIDER:389502,CHEBI:CHEBI:27868,HMDB:HMDB0003937)
  Modifiers: HADH (formerSymbols: HADHSC) (annotations: HGNC_SYMBOL:HADH,REFSEQ:NM_005327,,HGNC:4799,ENTREZ:3033,UNIPROT:Q16836)
  (References: REACTOME:REACT_242.2|PUBMED:8687463)
RID: 55188 (;State transition'):
  Reactants: LNSOL (annotations: CHEBI:CHEBI:16521)
  Products: 24,25-Dihydrolanosterol (annotations: CHEBI:CHEBI:28113)
  Modifiers: DHCR24 (formerSymbols: DCE) (annotations: REFSEQ:NM_014762,HGNC_SYMBOL:DHCR24,,ENTREZ:1718,UNIPROT:Q15392,HGNC:2859)
  (References: DOI:10.1016/B978-0-12-824048-9.00005-5)
RID: 55090 (;State transition'):
  Reactants: Cholesterol (annotations: CHEBI:CHEBI:16113,KEGG_COMPOUND:C00187)
  Products: Cholesterol ester (annotations: CHEBI:CHEBI:17002)
  Modifiers: SOAT
RID: 55908 (;State transition'):
  Reactants: Glucose-6-Phosphate (annotations: CHEBI:CHEBI:14314)
  Products: Fructose-6-Phosphate (annotations: CHEBI:CHEBI:15946,CHEBI:CHEBI:16084)
  Modifiers: GPI (annotations: ENTREZ:2821,,HGNC_SYMBOL:GPI,HGNC:4458,REFSEQ:NM_000175,UNIPROT:P06744)
RID: 56211 (;State transition'):
  Reactants: Glycin (annotations: CHEBI:CHEBI:55443,CHEBI:CHEBI:15428)
  Products: Methylene-FH4 (annotations: CHEBI:CHEBI:20502); CO2 (annotations: CHEBI:CHEBI:16526)
  Modifiers: Glycine Decarboxylase Complex
RID: 55724 (;Transport'):
  Reactants: Triacylglycerol (annotations: CHEBI:CHEBI:17855)
  Products: Triacylglycerol (annotations: CHEBI:CHEBI:17855)
  Modifiers: MTTP (formerSymbols: MTP) (annotations: HGNC:7467,REFSEQ:NM_000253,ENTREZ:4547,HGNC_SYMBOL:MTTP,,WIKIPATHWAYS:WP430,UNIPROT:P55157,PUBMED:18477307)
RID: 55298 (PDmap:re542.0;State transition'):
  Reactants: trans-dec-3-enoyl-CoA (annotations: CHEBI:CHEBI:29126,REACTOME:REACT_3172.1)
  Products: trans-dec-2-enoyl-CoA (annotations: CHEMSPIDER:4444334,CHEBI:CHEBI:10723,KEGG_COMPOUND:C05275,CAS:10018-95-8,REACTOME:REACT_3903.1,PUBCHEM:5280768,HMDB:HMDB0003948)
  Modifiers: ECI1 (formerSymbols: DCI) (annotations: ENTREZ:1632,HGNC_SYMBOL:ECI1,UNIPROT:P42126,,HGNC:2703,REFSEQ:NM_001178029)
  (References: REACTOME:REACT_1445.1)
RID: 55244 (PDmap:re393.0;State transition'):
  Reactants: isocitric acid (annotations: CHEBI:CHEBI:30887,KEGG_COMPOUND:C00311,CHEMBL_COMPOUND:CHEMBL539669,CHEMSPIDER:1161,WIKIPEDIA:Isocitric acid,CAS:320-77-4,PUBCHEM:1198,HMDB:HMDB0000193); NADP(+) (annotations: CHEBI:CHEBI:18009,WIKIPEDIA:NADP,KEGG_COMPOUND:C00006,CAS:53-59-8,PUBCHEM:5886,CHEMBL_COMPOUND:CHEMBL213053,HMDB:HMDB0000217,CHEMSPIDER:5675)
  Products: 2-oxoglutaric acid (annotations: KEGG_COMPOUND:C00026,REACTOME:REACT_3871.1,CHEBI:CHEBI:30915,CAS:328-50-7,MESH_2012:C029743,PUBCHEM:51,CHEMSPIDER:50,HMDB:HMDB0000208,WIKIPEDIA:Alpha-Ketoglutaric_acid); NADPH (annotations: KEGG_COMPOUND:C00005,HMDB:HMDB0000221,CHEMSPIDER:17215925,CHEMBL_COMPOUND:CHEMBL213053,CHEBI:CHEBI:16474,CAS:53-57-6,WIKIPEDIA:NADPH,PUBCHEM:22833512); CO2 (annotations: CHEMSPIDER:274,CHEBI:CHEBI:16526,MESH_2012:D002245,CHEMBL_COMPOUND:CHEMBL1231871,PUBCHEM:280,WIKIPEDIA:Carbon Dioxide,HMDB:HMDB0001967,KEGG_COMPOUND:C00011,CAS:124-38-9); H+ (annotations: CHEBI:CHEBI:15378)
  Modifiers: isocitrate dehydrogenase (annotations: REACTOME:REACT_21933.1)
  (References: REACTOME:REACT_21355.1|PUBMED:12207025)
RID: 55894 (;Positive influence'):
  Reactants: NFE2L2 (annotations: UNIPROT:Q16236,,PUBMED:28416361,ENTREZ:4780,REFSEQ:NM_006164,HGNC:7782,HGNC_SYMBOL:NFE2L2)
  Products: NR1H4 (annotations: ENTREZ:9971,,HGNC:7967,UNIPROT:Q96RI1,REFSEQ:NM_005123,HGNC_SYMBOL:NR1H4)
  Modifiers: None
RID: 56113 (;Positive influence'):
  Reactants: INS (formerSymbols: IDDM1,IDDM2) (annotations: HGNC_SYMBOL:INS,PUBMED:28416361,HGNC:6081,REFSEQ:NM_000207,ENTREZ:3630,,UNIPROT:P01308)
  Products: AKT1 (annotations: ENTREZ:207,HGNC:391,PUBMED:28416361,HGNC_SYMBOL:AKT1,REFSEQ:NM_005163,UNIPROT:P31749,)
  Modifiers: None
RID: 56082 (;State transition'):
  Reactants: PFKL (annotations: HGNC:8876,UNIPROT:P17858,PUBMED:31284506,REFSEQ:NM_001002021,,ENTREZ:5211,HGNC_SYMBOL:PFKL)
  Products: PFKL (annotations: HGNC:8876,UNIPROT:P17858,PUBMED:31284506,REFSEQ:NM_001002021,,ENTREZ:5211,HGNC_SYMBOL:PFKL)
  Modifiers: None
RID: 55751 (;Positive influence'):
  Reactants: PPARA (formerSymbols: PPAR) (annotations: HGNC_SYMBOL:PPARA,ENTREZ:5465,REFSEQ:NM_001001928,,PUBMED:26451809,UNIPROT:Q07869,HGNC:9232)
  Products: SCP2 (annotations: HGNC_SYMBOL:SCP2,ENTREZ:6342,REFSEQ:NM_002979,,UNIPROT:P22307,HGNC:10606)
  Modifiers: None
RID: 55529 (;Positive influence'):
  Reactants: PKA
  Products: Phosphorylase kinase (PHK)
  Modifiers: None
RID: 55428 (;State transition'):
  Reactants:  ; mtDNA encoded OXPHOS units (annotations: PUBMED:23149385,PUBMED:30030361)
  Products: complex III (annotations: GO:GO:0045275)
  Modifiers: OXPHOS factors (annotations: PUBMED:23149385,PUBMED:30030361)
  (References: PUBMED:23149385|TAXONOMY:10090|PUBMED:30030361)
RID: 55820 (;State transition'):
  Reactants: Monoacylglycerol (annotations: CHEBI:CHEBI:17408); Acyl CoA (annotations: CHEBI:CHEBI:37554,CHEBI:CHEBI:58342)
  Products: Diacylglycerol
  Modifiers: MOGAT
RID: 55644 (;State transition'):
  Reactants: PFKFB1 (formerSymbols: PFRX) (annotations: ENTREZ:5207,REFSEQ:NM_001271804,UNIPROT:P16118,HGNC:8872,HGNC_SYMBOL:PFKFB1,)
  Products: PFKFB1 (formerSymbols: PFRX) (annotations: ENTREZ:5207,REFSEQ:NM_001271804,UNIPROT:P16118,HGNC:8872,HGNC_SYMBOL:PFKFB1,)
  Modifiers: PRKA
RID: 55485 (;Negative influence'):
  Reactants: RPS6KB1 (formerSymbols: STK14A) (annotations: HGNC:10436,UNIPROT:P23443,ENTREZ:6198,,HGNC_SYMBOL:RPS6KB1,REFSEQ:NM_003161)
  Products: mTORC2 (annotations: GO:GO:0031932,PUBMED:28416361)
  Modifiers: None
  (References: PUBMED:19963289)
RID: 56099 (;State transition'):
  Reactants: 3-trans-decenoyl-CoA (annotations: CHEBI:CHEBI:29126)
  Products: Trans-dec-2-enoyl-CoA (annotations: CHEBI:CHEBI:10723)
  Modifiers: ECI1 (formerSymbols: DCI) (annotations: ENTREZ:1632,HGNC_SYMBOL:ECI1,UNIPROT:P42126,,HGNC:2703,REFSEQ:NM_001178029)
RID: 55362 (PDmap:re531.0;State transition'):
  Reactants: trans-hex-2-enoyl-CoA (annotations: CAS:10018-93-6,PUBCHEM:5280765,KEGG_COMPOUND:C05271,CHEBI:CHEBI:28706,HMDB:HMDB0003944,CHEMSPIDER:4444331,REACTOME:REACT_2759.1)
  Products: (S)-3-hydroxyhexanoyl-CoA (annotations: CHEBI:CHEBI:28276,REACTOME:REACT_3348.1)
  Modifiers: ECHS1 (annotations: HGNC_SYMBOL:ECHS1,,ENTREZ:1892,UNIPROT:P30084,HGNC:3151,REFSEQ:NM_004092)
  (References: REACTOME:REACT_87.2|PUBMED:13295248)
RID: 55266 (PDmap:re571.0;State transition'):
  Reactants: Arachidonic acid (annotations: PUBCHEM:444899,CHEMBL_COMPOUND:CHEMBL15594,HMDB:HMDB0001043,CHEMSPIDER:392692,KEGG_COMPOUND:C00219,CAS:506-32-1,WIKIPEDIA:Arachidonic acid,REACTOME:REACT_15656.1,CHEBI:CHEBI:15843,MESH_2012:D016718)
  Products: arachidonoyl-CoA (annotations: REACTOME:REACT_22603.1,CHEBI:CHEBI:15514)
  Modifiers: ACSL4 (formerSymbols: FACL4,MRX63,MRX68) (annotations: HGNC:3571,REFSEQ:NM_004458,ENTREZ:2182,HGNC_SYMBOL:ACSL4,UNIPROT:O60488,)
  (References: PUBMED:11889465|REACTOME:REACT_22376.1|PUBMED:12525535)
RID: 55930 (;State transition'):
  Reactants: Glucose-6-Phosphate (annotations: CHEBI:CHEBI:14314)
  Products: Glucose (annotations: CHEBI:CHEBI:42758,CHEBI:CHEBI:4167,CHEBI:CHEBI:17234)
  Modifiers: G6PC (annotations: PUBMED:28416361,)
RID: 55496 (;Positive influence'):
  Reactants: FOXO1 (formerSymbols: FKHR,FOXO1A) (annotations: HGNC:3819,,REFSEQ:NM_002015,ENTREZ:2308,PUBMED:28416361,HGNC_SYMBOL:FOXO1,UNIPROT:Q12778)
  Products: GCK (formerSymbols: MODY2) (annotations: ,ENTREZ:2645,HGNC_SYMBOL:GCK,PUBMED:28416361,REFSEQ:NM_000162,UNIPROT:P35557,HGNC:4195)
  Modifiers: None
RID: 55395 (;State transition'):
  Reactants: superoxide (annotations: HMDB:HMDB0002168,WIKIPEDIA:Superoxide,PUBCHEM:5359597,CHEMSPIDER:4514331,KEGG_COMPOUND:C00704,CHEBI:CHEBI:18421,CAS:11062-77-4); H+ (annotations: CHEBI:CHEBI:15378)
  Products: hydrogen peroxide (annotations: PUBCHEM:784,HMDB:HMDB0003125,KEGG_COMPOUND:C00027,MESH_2012:D006861,CHEBI:CHEBI:16240,WIKIPEDIA:Hydrogen peroxide,CAS:7722-84-1,CHEMBL_COMPOUND:CHEMBL71595,CHEMSPIDER:763)
  Modifiers: SOD1 (formerSymbols: ALS,ALS1) (annotations: REFSEQ:NM_000454,UNIPROT:P00441,,HGNC:11179,HGNC_SYMBOL:SOD1,ENTREZ:6647)
  (References: PUBMED:19427899|REACTOME:REACT_264249)
RID: 56204 (;State transition'):
  Reactants: Fructose-2,6-Bisphosphate (annotations: CHEBI:CHEBI:28602)
  Products: Fructose-6-Phosphate (annotations: CHEBI:CHEBI:15946,CHEBI:CHEBI:16084)
  Modifiers: PFKFB1 (formerSymbols: PFRX) (annotations: ENTREZ:5207,REFSEQ:NM_001271804,UNIPROT:P16118,HGNC:8872,HGNC_SYMBOL:PFKFB1,)
RID: 55814 (;State transition'):
  Reactants: β-Hydroxybutyrate (annotations: CHEBI:CHEBI:20067)
  Products: Acetoacetate (annotations: CHEBI:CHEBI:13705)
  Modifiers: BDH
RID: 56042 (;State transition'):
  Reactants: 6-Phosphogluconate (annotations: CHEBI:CHEBI:48928)
  Products: Fibulose-5-Phosphate
  Modifiers: PGD (annotations: UNIPROT:P52209,HGNC_SYMBOL:PGD,REFSEQ:NM_002631,,HGNC:8891,ENTREZ:5226)
RID: 55781 (;Heterodimer association'):
  Reactants: GCG (annotations: HGNC_SYMBOL:GCG,,REFSEQ:NM_002054,PUBMED:24692138,HGNC:4191,UNIPROT:P01275,ENTREZ:2641); GCGR (annotations: HGNC_SYMBOL:GCGR,HGNC:4192,REFSEQ:NM_000160,UNIPROT:P47871,,ENTREZ:2642)
  Products: GCGR:GCG (annotations: REFSEQ:NM_002115,HGNC_SYMBOL:HK3,,ENTREZ:3101,HGNC:4925,UNIPROT:P52790)
  Modifiers: None
  (References: PUBMED:24692138)
RID: 55648 (;Positive influence'):
  Reactants: Odd-chain fatty acids oxidation
  Products: Propionyl-CoA (annotations: CHEBI:CHEBI:15539)
  Modifiers: None
RID: 55605 (;State transition'):
  Reactants: FOXO1 (formerSymbols: FKHR,FOXO1A) (annotations: HGNC:3819,,REFSEQ:NM_002015,ENTREZ:2308,PUBMED:28416361,HGNC_SYMBOL:FOXO1,UNIPROT:Q12778)
  Products: FOXO1 (formerSymbols: FKHR,FOXO1A) (annotations: HGNC:3819,,REFSEQ:NM_002015,ENTREZ:2308,PUBMED:28416361,HGNC_SYMBOL:FOXO1,UNIPROT:Q12778)
  Modifiers: None
RID: 55345 (PDmap:re529.0;State transition'):
  Reactants: 3-oxooctanoyl-CoA (annotations: REACTOME:REACT_4358.1,CHEBI:CHEBI:28264)
  Products: hexanoyl-CoA (annotations: KEGG_COMPOUND:C05270,CHEBI:CHEBI:27540,CHEMSPIDER:389509,HMDB:HMDB0002845,CAS:5060-32-2,PUBCHEM:440611,REACTOME:REACT_5004.1)
  Modifiers: trifunctional Protein
  (References: REACTOME:REACT_481.2|PUBMED:1550553)
RID: 55289 (;State transition'):
  Reactants: 3-L-Hydroxyacyl-CoA (annotations: CHEBI:CHEBI:57318)
  Products: trans-delta2-enoyl-CoA
  Modifiers: ECH1 (annotations: REFSEQ:NM_001398,HGNC_SYMBOL:ECH1,HGNC:3149,UNIPROT:Q13011,ENTREZ:1891,); ECHS1 (annotations: HGNC_SYMBOL:ECHS1,,ENTREZ:1892,UNIPROT:P30084,HGNC:3151,REFSEQ:NM_004092); ECHDC1 (annotations: ,UNIPROT:Q9NTX5,HGNC_SYMBOL:ECHDC1,HGNC:21489,ENTREZ:55862,REFSEQ:NM_001002030); ECHDC2 (annotations: HGNC_SYMBOL:ECHDC2,UNIPROT:Q86YB7,HGNC:23408,ENTREZ:55268,,REFSEQ:NM_018281); ECHDC3 (annotations: HGNC_SYMBOL:ECHDC3,REFSEQ:NM_024693,HGNC:23489,ENTREZ:79746,UNIPROT:Q96DC8,)
  (References: WIKIPATHWAYS:WP357)
RID: 56015 (;State transition'):
  Reactants: 3-Phosphoglycerate (annotations: CHEBI:CHEBI:17050,CHEBI:CHEBI:17794,CHEBI:CHEBI:57998)
  Products: 3-Phospho-Hydroxy-Pyruvate (annotations: CHEBI:CHEBI:18110)
  Modifiers: PHGDH (annotations: HGNC_SYMBOL:PHGDH,ENTREZ:26227,REFSEQ:NM_006623,HGNC:8923,UNIPROT:O43175,)
RID: 55177 (;Transcription'):
  Reactants: ACSL3 (formerSymbols: FACL3) (annotations: REFSEQ:NM_004457,ENTREZ:2181,UNIPROT:O95573,,HGNC_SYMBOL:ACSL3,HGNC:3570)
  Products: ACSL3 (formerSymbols: FACL3) (annotations: REFSEQ:NM_004457,ENTREZ:2181,UNIPROT:O95573,,HGNC_SYMBOL:ACSL3,HGNC:3570)
  Modifiers: SREBF2 (annotations: HGNC:11290,REFSEQ:NM_004599,UNIPROT:Q12772,,HGNC_SYMBOL:SREBF2,ENTREZ:6721)
  (References: WIKIPATHWAYS:WP4718)
RID: 55901 (;Positive influence'):
  Reactants: NR1I2 (annotations: ,HGNC_SYMBOL:NR1I2,HGNC:7968,REFSEQ:NM_003889,ENTREZ:8856,UNIPROT:O75469)
  Products: CYP4F12 (annotations: UNIPROT:Q9HCS2,HGNC:18857,HGNC_SYMBOL:CYP4F12,,ENTREZ:66002,REFSEQ:NM_023944)
  Modifiers: None
RID: 56182 (;State transition'):
  Reactants: 1,3-Bisphosphoglycerate (annotations: CHEBI:CHEBI:89363)
  Products: 3-Phosphoglycerate (annotations: CHEBI:CHEBI:17050,CHEBI:CHEBI:17794,CHEBI:CHEBI:57998)
  Modifiers: PGK1 (annotations: ,UNIPROT:P00558,HGNC:8896,HGNC_SYMBOL:PGK1,ENTREZ:5230,REFSEQ:NM_000291)
  (References: WIKIPATHWAYS:WP534)
RID: 55977 (;Positive influence'):
  Reactants: ChREBP (annotations: PUBMED:26451809)
  Products: SREBP-1c (annotations: PUBMED:26451809)
  Modifiers: None
RID: 55285 (PDmap:re534.0;State transition'):
  Reactants: butyryl-CoA (annotations: CHEBI:CHEBI:15517)
  Products: crotonoyl-CoA (annotations: KEGG_COMPOUND:C00877,REACTOME:REACT_5111.1,CHEBI:CHEBI:15473,HMDB:HMDB0002009,PUBCHEM:5280381,CAS:102680-35-3,CHEMSPIDER:4444072,WIKIPEDIA:Crotonyl-coenzyme A)
  Modifiers: ACADS (annotations: HGNC:90,UNIPROT:P16219,HGNC_SYMBOL:ACADS,,ENTREZ:35,REFSEQ:NM_000017)
  (References: REACTOME:REACT_1592.2|PUBMED:13295225|PUBMED:3597357)
RID: 55197 (;State transition'):
  Reactants: NR1H2 (formerSymbols: UNR) (annotations: UNIPROT:P55055,ENTREZ:7376,REFSEQ:NM_001256647,HGNC:7965,,HGNC_SYMBOL:NR1H2)
  Products: NR1H2 (formerSymbols: UNR) (annotations: UNIPROT:P55055,ENTREZ:7376,REFSEQ:NM_001256647,HGNC:7965,,HGNC_SYMBOL:NR1H2)
  Modifiers: Desmosterol (annotations: CHEBI:CHEBI:17737)
  (References: WIKIPATHWAYS:WP4718)
RID: 55609 (;Positive influence'):
  Reactants: mTORC1 (annotations: GO:GO:0031931)
  Products: Protein Synthesis
  Modifiers: None
RID: 55809 (;Positive influence'):
  Reactants: INS (formerSymbols: IDDM1,IDDM2) (annotations: HGNC_SYMBOL:INS,PUBMED:28416361,HGNC:6081,REFSEQ:NM_000207,ENTREZ:3630,,UNIPROT:P01308)
  Products: PFKFB1 (formerSymbols: PFRX) (annotations: ENTREZ:5207,REFSEQ:NM_001271804,UNIPROT:P16118,HGNC:8872,HGNC_SYMBOL:PFKFB1,)
  Modifiers: None
RID: 55582 (;Positive influence'):
  Reactants: Cholesterol (annotations: CHEBI:CHEBI:16113,KEGG_COMPOUND:C00187)
  Products: Steroid synthesis (annotations: GO:GO:0006694)
  Modifiers: None
RID: 55754 (;State transition'):
  Reactants: Trans-dec-2-enoyl-CoA (annotations: CHEBI:CHEBI:10723)
  Products: (S)-Hydroxydecanoyl-CoA (annotations: CHEBI:CHEBI:28325)
  Modifiers: ECHS1 (annotations: HGNC_SYMBOL:ECHS1,,ENTREZ:1892,UNIPROT:P30084,HGNC:3151,REFSEQ:NM_004092)
RID: 56208 (;State transition'):
  Reactants: Glucose (annotations: CHEBI:CHEBI:17234)
  Products: Glucose-6-Phosphate (annotations: CHEBI:CHEBI:14314)
  Modifiers: HK1 (annotations: REFSEQ:NM_000188,,HGNC_SYMBOL:HK1,UNIPROT:P19367,HGNC:4922,ENTREZ:3098); GCK (formerSymbols: MODY2) (annotations: ENTREZ:2645,,HGNC_SYMBOL:GCK,REFSEQ:NM_000162,UNIPROT:P35557,HGNC:4195)
RID: 55839 (;Positive influence'):
  Reactants: Cholesterol (annotations: CHEBI:CHEBI:16113,KEGG_COMPOUND:C00187)
  Products: Bile (annotations: GO:GO:0006699)
  Modifiers: None
RID: 55995 (;Positive influence'):
  Reactants: AKT1 (annotations: ENTREZ:207,HGNC:391,PUBMED:28416361,HGNC_SYMBOL:AKT1,REFSEQ:NM_005163,UNIPROT:P31749,)
  Products: mTORC1 (annotations: GO:GO:0031931)
  Modifiers: None
  (References: PUBMED:19143635|PUBMED:23802099)
RID: 55621 (;State transition'):
  Reactants: DMAPP (annotations: CHEBI:CHEBI:57623)
  Products: GPP (annotations: CHEBI:CHEBI:17211)
  Modifiers: GGPS1 (annotations: ENTREZ:9453,UNIPROT:O95749,HGNC:4249,HGNC_SYMBOL:GGPS1,REFSEQ:NM_004837,); FDPS (annotations: REFSEQ:NM_002004,HGNC:3631,HGNC_SYMBOL:FDPS,UNIPROT:P14324,,ENTREZ:2224)
  (References: DOI:10.1016/B978-0-12-824048-9.00005-5)
RID: 55347 (PDmap:re392.0;State transition'):
  Reactants: citrate(3-) (annotations: KEGG_COMPOUND:C00158,PUBCHEM:311,CHEBI:CHEBI:30769,CHEBI:CHEBI:16947,WIKIPEDIA:Citric acid,REACTOME:REACT_2769.1,CHEMBL_COMPOUND:CHEMBL1261,CHEMSPIDER:305,HMDB:HMDB0000094,CAS:77-92-9)
  Products: isocitric acid (annotations: CHEBI:CHEBI:30887,KEGG_COMPOUND:C00311,CHEMBL_COMPOUND:CHEMBL539669,CHEMSPIDER:1161,WIKIPEDIA:Isocitric acid,CAS:320-77-4,PUBCHEM:1198,HMDB:HMDB0000193)
  Modifiers: ACO2 (annotations: HGNC_SYMBOL:ACO2,ENTREZ:50,HGNC:118,REFSEQ:NM_001098,,UNIPROT:Q99798)
  (References: PUBMED:1946331|REACTOME:REACT_21262.1|PUBMED:1052766)
RID: 55450 (PDmap:re551.0;State transition'):
  Reactants: malonyl-CoA (annotations: REACTOME:REACT_3059.1,WIKIPEDIA:Malonyl-CoA,HMDB:HMDB0001175,CAS:524-14-1,CHEBI:CHEBI:15531,PUBCHEM:10663,KEGG_COMPOUND:C00083,CHEMSPIDER:10213); acetyl-CoA (annotations: CHEBI:CHEBI:15351,WIKIPEDIA:Acetyl-CoA,HMDB:HMDB0001206,CHEMSPIDER:392413,PUBCHEM:444493,REACTOME:REACT_3839.1,CAS:72-89-9,KEGG_COMPOUND:C00024)
  Products: palmitate (annotations: HMDB:HMDB0000220,PUBCHEM:985,KEGG_COMPOUND:C00249,WIKIPEDIA:Palmitic acid,CHEBI:CHEBI:7896,CAS:57-10-3,CHEMBL_COMPOUND:CHEMBL82293,CHEMSPIDER:960,CHEBI:CHEBI:15756,REACTOME:REACT_3374.1)
  Modifiers: FASN (annotations: HGNC:3594,UNIPROT:P49327,REFSEQ:NM_004104,,ENTREZ:2194,HGNC_SYMBOL:FASN)
  (References: REACTOME:REACT_1497.3|PUBMED:12689621)
RID: 55942 (;State transition'):
  Reactants: FBP1 (formerSymbols: FBP) (annotations: HGNC_SYMBOL:FBP1,UNIPROT:P09467,REFSEQ:NM_000507,PUBMED:31284506,HGNC:3606,ENTREZ:2203,)
  Products: FBP1 (formerSymbols: FBP) (annotations: HGNC_SYMBOL:FBP1,UNIPROT:P09467,REFSEQ:NM_000507,PUBMED:31284506,HGNC:3606,ENTREZ:2203,)
  Modifiers: PKA
RID: 55847 (;State transition'):
  Reactants: PYGL (annotations: ENTREZ:5836,REFSEQ:NM_002863,HGNC_SYMBOL:PYGL,HGNC:9725,,UNIPROT:P06737)
  Products: PYGL (annotations: ENTREZ:5836,REFSEQ:NM_002863,HGNC_SYMBOL:PYGL,HGNC:9725,,UNIPROT:P06737)
  Modifiers: None
RID: 56080 (;Known transition omitted'):
  Reactants: Acyl-CoA (annotations: CHEBI:CHEBI:17984)
  Products: Unsaturated Fatty Acids
  Modifiers: SCD (formerSymbols: SCDOS) (annotations: ,ENTREZ:6319,HGNC_SYMBOL:SCD,UNIPROT:O00767,HGNC:10571,REFSEQ:NM_005063)
RID: 56005 (;State transition'):
  Reactants: 3-Oxododecanoyl-CoA (annotations: CHEBI:CHEBI:27868)
  Products: Decanoyl-CoA (annotations: CHEBI:CHEBI:28493); Acetyl-CoA (annotations: CHEBI:CHEBI:15351,CHEBI:CHEBI:57288)
  Modifiers: Mitochondrial trifunctional enzyme
RID: 55480 (;State transition'):
  Reactants: SREBF1 (annotations: PUBMED:28416361,UNIPROT:P36956,REFSEQ:NM_004176,ENTREZ:6720,HGNC:11289,HGNC_SYMBOL:SREBF1,)
  Products: SREBF1 (annotations: PUBMED:28416361,UNIPROT:P36956,REFSEQ:NM_004176,ENTREZ:6720,HGNC:11289,HGNC_SYMBOL:SREBF1,)
  Modifiers: mTORC1 (annotations: GO:GO:0031931)
RID: 55425 (;Positive influence'):
  Reactants: Ca2+ (annotations: CHEBI:CHEBI:29108)
  Products: SLC25A23 (annotations: ENTREZ:79085,HGNC_SYMBOL:SLC25A23,REFSEQ:NM_024103,HGNC:19375,,UNIPROT:Q9BV35)
  Modifiers: None
  (References: PUBMED:22443365|PUBMED:25809592)
RID: 55412 (PDmap:re568.0;State transition'):
  Reactants: 1,2-diacyl-sn-glycerol (annotations: CHEBI:CHEBI:17815,REACTOME:REACT_4481.3); fatty acyl-CoA (annotations: CHEBI:CHEBI:37554,REACTOME:REACT_5036.3)
  Products: triglyceride (annotations: CHEBI:CHEBI:17855,REACTOME:REACT_22886.2); coenzyme A (annotations: CHEBI:CHEBI:15346,REACTOME:REACT_3654.2)
  Modifiers: DGAT1 (formerSymbols: DGAT) (annotations: HGNC_SYMBOL:DGAT1,UNIPROT:O75907,ENTREZ:8694,REFSEQ:NM_012079,HGNC:2843,)
  (References: REACTOME:REACT_659.5|PUBMED:11672446)
RID: 55204 (;State transition'):
  Reactants: Mevalonate-PP (annotations: CHEBI:CHEBI:25350)
  Products: Isopentenyl diphosphate (annotations: CHEBI:CHEBI:16584)
  Modifiers: MVD (annotations: HGNC_SYMBOL:MVD,REFSEQ:NM_002461,UNIPROT:P53602,ENTREZ:4597,,HGNC:7529)
  (References: WIKIPATHWAYS:WP4718|DOI:10.1016/B978-0-12-824048-9.00005-5)
RID: 55896 (;Transport'):
  Reactants: H+ (annotations: CHEBI:CHEBI:15378)
  Products: H+ (annotations: CHEBI:CHEBI:15378)
  Modifiers: Complex IV
RID: 55657 (;State transition'):
  Reactants: 3-Phosphoserine (annotations: CHEBI:CHEBI:15811)
  Products: Serine (annotations: CHEBI:CHEBI:17822,CHEBI:CHEBI:17115)
  Modifiers: PSPH (formerSymbols: PSP) (annotations: UNIPROT:P78330,HGNC:9577,REFSEQ:NM_004577,,HGNC_SYMBOL:PSPH,ENTREZ:5723)
RID: 55181 (;State transition'):
  Reactants: Cholesterol (annotations: CHEBI:CHEBI:16113,KEGG_COMPOUND:C00187)
  Products: 25-hydroxycholesterol
  Modifiers: CH25H (annotations: ENTREZ:9023,HGNC:1907,UNIPROT:O95992,,HGNC_SYMBOL:CH25H,REFSEQ:NM_003956)
  (References: WIKIPATHWAYS:WP4718)
RID: 55361 (;State transition'):
  Reactants: glutathione (annotations: CHEMBL_COMPOUND:CHEMBL1543,CHEBI:CHEBI:16856,HMDB:HMDB0000125,KEGG_COMPOUND:C00051,WIKIPEDIA:Glutathione,CHEMSPIDER:111188,CAS:70-18-8,MESH_2012:D005978,PUBCHEM:124886); hydrogen peroxide (annotations: PUBCHEM:784,HMDB:HMDB0003125,KEGG_COMPOUND:C00027,MESH_2012:D006861,CHEBI:CHEBI:16240,WIKIPEDIA:Hydrogen peroxide,CAS:7722-84-1,CHEMBL_COMPOUND:CHEMBL71595,CHEMSPIDER:763)
  Products: glutathione disulfide (annotations: KEGG_COMPOUND:C00127,CHEBI:CHEBI:17858,HMDB:HMDB0003337,PUBCHEM:975,CAS:27025-41-8,WIKIPEDIA:Glutathione disulfide,CHEMBL_COMPOUND:CHEMBL1372,CHEMSPIDER:950); H2O (annotations: HMDB:HMDB0002111,CHEBI:CHEBI:15377,PUBCHEM:962,CHEMSPIDER:937,MESH_2012:D014867,WIKIPEDIA:Water,CAS:7732-18-5,CHEMBL_COMPOUND:CHEMBL1098659,KEGG_COMPOUND:C00001)
  Modifiers: GPX2 (annotations: ENTREZ:2877,HGNC:4554,HGNC_SYMBOL:GPX2,REFSEQ:NM_002083,UNIPROT:P18283,)
  (References: REACTOME:REACT_264249)
RID: 56061 (;Known transition omitted'):
  Reactants: Palmitoyl-CoA (annotations: CHEBI:CHEBI:15525)
  Products: Trans-Hexadec-2-enoyl-CoA (annotations: CHEBI:CHEBI:28935)
  Modifiers: ACADVL (annotations: ENTREZ:37,HGNC:92,,UNIPROT:P49748,HGNC_SYMBOL:ACADVL,REFSEQ:NM_000018)
RID: 56000 (;Positive influence'):
  Reactants: Prostaglandins
  Products: PPARA (formerSymbols: PPAR) (annotations: HGNC_SYMBOL:PPARA,ENTREZ:5465,REFSEQ:NM_001001928,,PUBMED:26451809,UNIPROT:Q07869,HGNC:9232)
  Modifiers: None
RID: 55359 (PDmap:re547.0;State transition'):
  Reactants: citrate(3-) (annotations: KEGG_COMPOUND:C00158,PUBCHEM:311,CHEBI:CHEBI:30769,CHEBI:CHEBI:16947,WIKIPEDIA:Citric acid,REACTOME:REACT_2769.1,CHEMBL_COMPOUND:CHEMBL1261,CHEMSPIDER:305,HMDB:HMDB0000094,CAS:77-92-9)
  Products: acetyl-CoA (annotations: CHEBI:CHEBI:15351,WIKIPEDIA:Acetyl-CoA,HMDB:HMDB0001206,CHEMSPIDER:392413,PUBCHEM:444493,REACTOME:REACT_3839.1,CAS:72-89-9,KEGG_COMPOUND:C00024); oxaloacetate(2-) (annotations: PUBCHEM:970,CHEBI:CHEBI:30744,KEGG_COMPOUND:C00036,CAS:328-42-7,HMDB:HMDB0000223,CHEMSPIDER:945,REACTOME:REACT_5376.1,CHEBI:CHEBI:16452,WIKIPEDIA:Oxalacetic acid)
  Modifiers: ACLY (annotations: HGNC:115,REFSEQ:NM_001096,,ENTREZ:47,HGNC_SYMBOL:ACLY,UNIPROT:P53396)
  (References: PUBMED:1371749|REACTOME:REACT_1141.2)
RID: 55804 (;Positive influence'):
  Reactants: Fatty acyl-CoA
  Products: Triacylglyceride synthesis (annotations: WIKIPATHWAYS:WP325)
  Modifiers: None
RID: 55734 (;Positive influence'):
  Reactants: PI3K cascade (annotations: GO:GO:0014065)
  Products: AKT1 (annotations: ENTREZ:207,HGNC:391,PUBMED:28416361,HGNC_SYMBOL:AKT1,REFSEQ:NM_005163,UNIPROT:P31749,)
  Modifiers: None
RID: 56089 (;Known transition omitted'):
  Reactants: NR1I2 (annotations: ,HGNC_SYMBOL:NR1I2,HGNC:7968,REFSEQ:NM_003889,ENTREZ:8856,UNIPROT:O75469)
  Products: NR1I2 (annotations: ,HGNC_SYMBOL:NR1I2,HGNC:7968,REFSEQ:NM_003889,ENTREZ:8856,UNIPROT:O75469)
  Modifiers: None
RID: 55817 (;Positive influence'):
  Reactants: RXRA (annotations: UNIPROT:P19793,,HGNC:10477,REFSEQ:NM_002957,ENTREZ:6256,HGNC_SYMBOL:RXRA)
  Products: NFE2L2 (annotations: UNIPROT:Q16236,,PUBMED:28416361,ENTREZ:4780,REFSEQ:NM_006164,HGNC:7782,HGNC_SYMBOL:NFE2L2)
  Modifiers: None
RID: 55467 (;State transition'):
  Reactants: TSC (annotations: PUBMED:28416361)
  Products: TSC (annotations: PUBMED:28416361)
  Modifiers: None
RID: 55593 (;Positive influence'):
  Reactants: PPARA (formerSymbols: PPAR) (annotations: HGNC_SYMBOL:PPARA,ENTREZ:5465,REFSEQ:NM_001001928,,PUBMED:26451809,UNIPROT:Q07869,HGNC:9232)
  Products: ACAA1 (annotations: HGNC_SYMBOL:ACAA1,,REFSEQ:NM_001607,HGNC:82,ENTREZ:30,UNIPROT:P09110)
  Modifiers: None
RID: 55350 (;State transition'):
  Reactants: glutathione disulfide (annotations: KEGG_COMPOUND:C00127,CHEBI:CHEBI:17858,HMDB:HMDB0003337,PUBCHEM:975,CAS:27025-41-8,WIKIPEDIA:Glutathione disulfide,CHEMBL_COMPOUND:CHEMBL1372,CHEMSPIDER:950); H+ (annotations: CHEBI:CHEBI:15378); NADPH (annotations: KEGG_COMPOUND:C00005,HMDB:HMDB0000221,CHEMSPIDER:17215925,CHEMBL_COMPOUND:CHEMBL213053,CHEBI:CHEBI:16474,CAS:53-57-6,WIKIPEDIA:NADPH,PUBCHEM:22833512)
  Products: glutathione (annotations: CHEMBL_COMPOUND:CHEMBL1543,CHEBI:CHEBI:16856,HMDB:HMDB0000125,KEGG_COMPOUND:C00051,WIKIPEDIA:Glutathione,CHEMSPIDER:111188,CAS:70-18-8,MESH_2012:D005978,PUBCHEM:124886); NADP+ (annotations: CHEBI:CHEBI:18009,WIKIPEDIA:NADP,KEGG_COMPOUND:C00006,CAS:53-59-8,PUBCHEM:5886,CHEMBL_COMPOUND:CHEMBL213053,HMDB:HMDB0000217,CHEMSPIDER:5675,REACTOME:REACT_4609.3)
  Modifiers: GSR:FAD
  (References: REACTOME:REACT_264249)
RID: 55238 (PDmap:re574.0;State transition'):
  Reactants: tetracosanoyl-CoA (annotations: CHEBI:CHEBI:52974,REACTOME:REACT_23048.1)
  Products: 3-oxodocosanoyl-CoA (annotations: REACTOME:REACT_22766.1,CHEBI:CHEBI:52328)
  Modifiers: ELOVL4 (formerSymbols: SCA34,STGD2,STGD3) (annotations: ,HGNC_SYMBOL:ELOVL4,UNIPROT:Q9GZR5,HGNC:14415,ENTREZ:6785,REFSEQ:NM_022726)
  (References: REACTOME:REACT_22242.1|PUBMED:16036915|PUBMED:18728184)
RID: 55743 (;Known transition omitted'):
  Reactants: Palmitoyl-CoA (annotations: CHEBI:CHEBI:15525)
  Products: Sphingolipids (annotations: CHEBI:CHEBI:26739)
  Modifiers: None
RID: 55463 (;Positive influence'):
  Reactants: CASP9 (annotations: HGNC_SYMBOL:CASP9,REFSEQ:NM_032996,ENTREZ:842,,HGNC:1511,UNIPROT:P55211)
  Products: Apoptosis (annotations: GO:GO:1900117,GO:GO:0097194)
  Modifiers: None
RID: 55273 (;Negative influence'):
  Reactants: H+ (annotations: CHEBI:CHEBI:15378)
  Products: mitochondrial depolarization (annotations: GO:GO:0051882)
  Modifiers: None
  (References: PUBMED:15738989)
RID: 55879 (;Positive influence'):
  Reactants: FA > C14 < C22
  Products: Fatty acyl-CoA
  Modifiers: None
RID: 55569 (;Positive influence'):
  Reactants: PPARA (formerSymbols: PPAR) (annotations: HGNC_SYMBOL:PPARA,ENTREZ:5465,REFSEQ:NM_001001928,,PUBMED:26451809,UNIPROT:Q07869,HGNC:9232)
  Products: APOA2 (annotations: HGNC:601,,ENTREZ:336,UNIPROT:P02652,HGNC_SYMBOL:APOA2,REFSEQ:NM_001643)
  Modifiers: None
RID: 55741 (;State transition'):
  Reactants: D-Glucose (annotations: CHEBI:CHEBI:4167)
  Products: Glucose-6-Phosphate (annotations: CHEBI:CHEBI:14314)
  Modifiers: HK1 (annotations: REFSEQ:NM_000188,,HGNC_SYMBOL:HK1,UNIPROT:P19367,HGNC:4922,ENTREZ:3098)
RID: 55626 (;State transition'):
  Reactants: 3-Phosphoglycerate (annotations: CHEBI:CHEBI:17050,CHEBI:CHEBI:17794,CHEBI:CHEBI:57998)
  Products: 2-Phosphoglycerate (annotations: CHEBI:CHEBI:24344)
  Modifiers: PGAM1 (formerSymbols: PGAMA) (annotations: ,HGNC:8888,ENTREZ:5223,UNIPROT:P18669,HGNC_SYMBOL:PGAM1,REFSEQ:NM_002629)
RID: 55865 (;Transport'):
  Reactants: Cholesterol (annotations: CHEBI:CHEBI:16113,KEGG_COMPOUND:C00187)
  Products: Cell membranes (annotations: GO:GO:0044091)
  Modifiers: None
RID: 55881 (;State transition'):
  Reactants: Glycin (annotations: CHEBI:CHEBI:55443,CHEBI:CHEBI:15428)
  Products: Methylene-FH4 (annotations: CHEBI:CHEBI:20502); CO2 (annotations: CHEBI:CHEBI:16526)
  Modifiers: Glycine Decarboxylase Complex
RID: 56162 (;Known transition omitted'):
  Reactants: Pyruvate (annotations: CHEBI:CHEBI:15361); Glutamate (annotations: CHEBI:CHEBI:29987,CHEBI:CHEBI:14321,CHEBI:CHEBI:16015,CHEBI:CHEBI:18237)
  Products: Alanin (annotations: CHEBI:CHEBI:16449); α-Ketogluatarate (annotations: CHEBI:CHEBI:30915)
  Modifiers: GPT (annotations: HGNC_SYMBOL:GPT,ENTREZ:2875,HGNC:4552,,REFSEQ:NM_001382664,UNIPROT:P24298)
RID: 55848 (;Positive influence'):
  Reactants: Cholesterol (annotations: CHEBI:CHEBI:16113,KEGG_COMPOUND:C00187)
  Products: Cell membranes (annotations: GO:GO:0044091)
  Modifiers: None
RID: 56100 (;State transition'):
  Reactants: FBP1 (formerSymbols: FBP) (annotations: HGNC_SYMBOL:FBP1,UNIPROT:P09467,REFSEQ:NM_000507,PUBMED:31284506,HGNC:3606,ENTREZ:2203,)
  Products: FBP1 (formerSymbols: FBP) (annotations: HGNC_SYMBOL:FBP1,UNIPROT:P09467,REFSEQ:NM_000507,PUBMED:31284506,HGNC:3606,ENTREZ:2203,)
  Modifiers: None
RID: 55269 (PDmap:re565.0;State transition'):
  Reactants: sn-glycerol 3-phosphate (annotations: CHEMSPIDER:388308,KEGG_COMPOUND:C00093,WIKIPEDIA:Glycerol 3-phosphate,HMDB:HMDB0000126,REACTOME:REACT_4327.2,CHEBI:CHEBI:15978,PUBCHEM:439162,CAS:57-03-4)
  Products: 1-acyl-sn-glycerol 3-phosphate (annotations: REACTOME:REACT_4701.3,CHEBI:CHEBI:16975)
  Modifiers: GPAT4 (formerSymbols: AGPAT6) (annotations: ,HGNC_SYMBOL:GPAT4,ENTREZ:137964,UNIPROT:Q86UL3,HGNC:20880,REFSEQ:NM_178819); GPAT3 (formerSymbols: AGPAT9) (annotations: HGNC:28157,HGNC_SYMBOL:GPAT3,UNIPROT:Q53EU6,,ENTREZ:84803,REFSEQ:NM_032717); GPAM (annotations: REFSEQ:NM_020918,HGNC:24865,HGNC_SYMBOL:GPAM,ENTREZ:57678,,UNIPROT:Q9HCL2); GPAT2 (annotations: ENTREZ:150763,HGNC_SYMBOL:GPAT2,,REFSEQ:NM_207328,UNIPROT:Q6NUI2,HGNC:27168)
  (References: PUBMED:19336658|REACTOME:REACT_22419.3|PUBMED:17170135|REACTOME:REACT_839.3|PUBMED:19318427|PUBMED:18238778|PUBMED:18718904)
RID: 55924 (;State transition'):
  Reactants: Fructose (annotations: CHEBI:CHEBI:28645,CHEBI:CHEBI:28757)
  Products: Fructose-6-Phosphate (annotations: CHEBI:CHEBI:15946,CHEBI:CHEBI:16084)
  Modifiers: HK1 (annotations: REFSEQ:NM_000188,,HGNC_SYMBOL:HK1,UNIPROT:P19367,HGNC:4922,ENTREZ:3098)
RID: 55558 (;State transition'):
  Reactants: ACC
  Products: ACC
  Modifiers: AMPK (annotations: GO:GO:0031588)
RID: 56059 (;State transition'):
  Reactants: Glyceralaldehyde-3-Phosphate (annotations: CHEBI:CHEBI:17138)
  Products: 1,3-Bisphosphoglycerate (annotations: CHEBI:CHEBI:89363)
  Modifiers: GAPDH (formerSymbols: GAPD) (annotations: REFSEQ:NM_002046,HGNC_SYMBOL:GAPDH,,ENTREZ:2597,UNIPROT:P04406,HGNC:4141)
RID: 55752 (;Positive influence'):
  Reactants: RPS6KB1 (formerSymbols: STK14A) (annotations: HGNC:10436,UNIPROT:P23443,ENTREZ:6198,,HGNC_SYMBOL:RPS6KB1,REFSEQ:NM_003161)
  Products: Translation (annotations: GO:GO:0006412)
  Modifiers: None
RID: 55559 (;Known transition omitted'):
  Reactants: PPARGC1A (formerSymbols: PPARGC1) (annotations: UNIPROT:Q9UBK2,ENTREZ:10891,HGNC:9237,HGNC_SYMBOL:PPARGC1A,,REFSEQ:NM_013261)
  Products: PPARGC1A (formerSymbols: PPARGC1) (annotations: UNIPROT:Q9UBK2,ENTREZ:10891,HGNC:9237,HGNC_SYMBOL:PPARGC1A,,REFSEQ:NM_013261)
  Modifiers: None
RID: 55620 (;State transition'):
  Reactants: Glycogen (n+1) (annotations: CHEBI:CHEBI:28087)
  Products: Glycogen (n) (annotations: CHEBI:CHEBI:28087); Glucose-1-Phosphate (annotations: CHEBI:CHEBI:29042)
  Modifiers: PYGL (annotations: ENTREZ:5836,REFSEQ:NM_002863,HGNC_SYMBOL:PYGL,HGNC:9725,,UNIPROT:P06737)
RID: 55527 (;Positive influence'):
  Reactants: PFKL (annotations: HGNC:8876,UNIPROT:P17858,PUBMED:31284506,REFSEQ:NM_001002021,,ENTREZ:5211,HGNC_SYMBOL:PFKL)
  Products: Glycolysis
  Modifiers: None
RID: 55522 (;Positive influence'):
  Reactants: PPARG:PPARGC1A
  Products: G6PC (annotations: PUBMED:28416361,)
  Modifiers: None
RID: 55883 (;State transition'):
  Reactants: Fatty acyl-CoA; Carnitin (annotations: CHEBI:CHEBI:16347)
  Products: Fatty acyl-carnitine; CoA (annotations: CHEBI:CHEBI:15346)
  Modifiers: CPT1A (formerSymbols: CPT1) (annotations: UNIPROT:P50416,HGNC_SYMBOL:CPT1A,HGNC:2328,ENTREZ:1374,PUBMED:26451809,REFSEQ:NM_001876,)
RID: 55196 (;State transition'):
  Reactants: NR1H3 (annotations: REFSEQ:NM_001130101,,HGNC:7966,ENTREZ:10062,UNIPROT:Q13133,HGNC_SYMBOL:NR1H3)
  Products: NR1H3 (annotations: REFSEQ:NM_001130101,,HGNC:7966,ENTREZ:10062,UNIPROT:Q13133,HGNC_SYMBOL:NR1H3)
  Modifiers: None
RID: 56071 (;State transition'):
  Reactants: Galactose (annotations: CHEBI:CHEBI:28260)
  Products: Galactose-1-Phosphate (annotations: CHEBI:CHEBI:17973)
  Modifiers: GALK
RID: 56149 (;State transition'):
  Reactants: 6-Phosphogluconolactone (annotations: CHEBI:CHEBI:16938)
  Products: 6-Phosphogluconate (annotations: CHEBI:CHEBI:48928)
  Modifiers: PGLS (annotations: ENTREZ:25796,REFSEQ:NM_012088,,HGNC_SYMBOL:PGLS,UNIPROT:O95336,HGNC:8903)
  (References: WIKIPATHWAYS:WP134)
RID: 55241 (PDmap:re546.0;State transition'):
  Reactants: linoleoyl-CoA (annotations: CHEBI:CHEBI:15530,CHEMSPIDER:10637815,REACTOME:REACT_3246.1,KEGG_COMPOUND:C02050,PUBCHEM:5462164,CAS:6709-57-5,HMDB:HMDB0001064)
  Products: cis,cis-dodeca-3,6-dienoyl-CoA (annotations: CHEBI:CHEBI:28002,REACTOME:REACT_3487.1)
  Modifiers: ACADL (annotations: REFSEQ:NM_001608,,HGNC_SYMBOL:ACADL,HGNC:88,ENTREZ:33,UNIPROT:P28330); trifunctional Protein
  (References: REACTOME:REACT_2238.2)
RID: 55861 (;Positive influence'):
  Reactants: NR1H4 (annotations: ,ENTREZ:9971,HGNC:7967,UNIPROT:Q96RI1,REFSEQ:NM_005123,HGNC_SYMBOL:NR1H4)
  Products: SLC27A5 (annotations: HGNC:10999,REFSEQ:NM_012254,ENTREZ:10998,UNIPROT:Q9Y2P5,HGNC_SYMBOL:SLC27A5,)
  Modifiers: None
RID: 55180 (;Known transition omitted'):
  Reactants: FADS2 (formerSymbols: LLCDL2) (annotations: ,HGNC:3575,HGNC_SYMBOL:FADS2,REFSEQ:NM_004265,UNIPROT:O95864,ENTREZ:9415)
  Products: Fatty Acid Biosynthesis (annotations: WIKIPATHWAYS:WP4491,GO:GO:0006633)
  Modifiers: None
RID: 55628 (;State transition'):
  Reactants: IRS2 (formerSymbols: ECHD) (annotations: UNIPROT:Q9Y4H2,HGNC:6126,ENTREZ:8660,HGNC_SYMBOL:IRS2,,REFSEQ:NM_003749)
  Products: IRS2 (formerSymbols: ECHD) (annotations: UNIPROT:Q9Y4H2,HGNC:6126,ENTREZ:8660,HGNC_SYMBOL:IRS2,,REFSEQ:NM_003749)
  Modifiers: RPS6KB1 (formerSymbols: STK14A) (annotations: HGNC:10436,UNIPROT:P23443,ENTREZ:6198,,HGNC_SYMBOL:RPS6KB1,REFSEQ:NM_003161); MAPK14 (formerSymbols: CSBP1,CSBP2,CSPB1) (annotations: ,HGNC:6876,UNIPROT:Q16539,HGNC_SYMBOL:MAPK14,ENTREZ:1432,REFSEQ:NM_001315)
RID: 55340 (;State transition'):
  Reactants: acetoacetyl-ACP
  Products: beta-hydroxybutyryl
  Modifiers: FASN (annotations: HGNC:3594,UNIPROT:P49327,REFSEQ:NM_004104,,ENTREZ:2194,HGNC_SYMBOL:FASN)
  (References: WIKIPATHWAYS:WP357)
RID: 55318 (;State transition'):
  Reactants: hydrogen peroxide (annotations: PUBCHEM:784,HMDB:HMDB0003125,KEGG_COMPOUND:C00027,MESH_2012:D006861,CHEBI:CHEBI:16240,WIKIPEDIA:Hydrogen peroxide,CAS:7722-84-1,CHEMBL_COMPOUND:CHEMBL71595,CHEMSPIDER:763); glutathione (annotations: CHEMBL_COMPOUND:CHEMBL1543,CHEBI:CHEBI:16856,HMDB:HMDB0000125,KEGG_COMPOUND:C00051,WIKIPEDIA:Glutathione,CHEMSPIDER:111188,CAS:70-18-8,MESH_2012:D005978,PUBCHEM:124886)
  Products: H2O (annotations: HMDB:HMDB0002111,CHEBI:CHEBI:15377,PUBCHEM:962,CHEMSPIDER:937,MESH_2012:D014867,WIKIPEDIA:Water,CAS:7732-18-5,CHEMBL_COMPOUND:CHEMBL1098659,KEGG_COMPOUND:C00001); glutathione disulfide (annotations: KEGG_COMPOUND:C00127,CHEBI:CHEBI:17858,HMDB:HMDB0003337,PUBCHEM:975,CAS:27025-41-8,WIKIPEDIA:Glutathione disulfide,CHEMBL_COMPOUND:CHEMBL1372,CHEMSPIDER:950)
  Modifiers: GPX5:GPX6
  (References: REACTOME:REACT_264249)
RID: 55317 (;State transition'):
  Reactants: 3-ketoacyl-CoA (annotations: CHEBI:CHEBI:57347)
  Products: 3-L-Hydroxyacyl-CoA (annotations: CHEBI:CHEBI:57318)
  Modifiers: HADHSC
  (References: WIKIPATHWAYS:WP357)
RID: 55968 (;Known transition omitted'):
  Reactants: NR1H4 (annotations: ENTREZ:9971,,HGNC:7967,UNIPROT:Q96RI1,REFSEQ:NM_005123,HGNC_SYMBOL:NR1H4)
  Products: NR1H4 (annotations: ,ENTREZ:9971,HGNC:7967,UNIPROT:Q96RI1,REFSEQ:NM_005123,HGNC_SYMBOL:NR1H4)
  Modifiers: None
RID: 55698 (;State transition'):
  Reactants: Diacylglycerol; Acyl CoA (annotations: CHEBI:CHEBI:37554,CHEBI:CHEBI:58342)
  Products: Triacylglycerol (annotations: CHEBI:CHEBI:17855)
  Modifiers: DGAT
RID: 55466 (;State transition'):
  Reactants: TSC (annotations: PUBMED:28416361)
  Products: TSC (annotations: PUBMED:28416361)
  Modifiers: AKT1 (annotations: ENTREZ:207,HGNC:391,PUBMED:28416361,HGNC_SYMBOL:AKT1,REFSEQ:NM_005163,UNIPROT:P31749,)
RID: 55236 (PDmap:re515.0;State transition'):
  Reactants: trans-tetradec-2-enoyl-CoA (annotations: CHEBI:CHEBI:27721,KEGG_COMPOUND:C05273,CHEMSPIDER:4444333,CAS:38795-33-4,REACTOME:REACT_3421.1,HMDB:HMDB0003946,PUBCHEM:5280767)
  Products: (S)-3-hydroxytetradecanoyl-CoA (annotations: CHEBI:CHEBI:27466,REACTOME:REACT_5705.1,KEGG_COMPOUND:C05260,CHEMSPIDER:389500,HMDB:HMDB0003934,PUBCHEM:440602)
  Modifiers: trifunctional Protein
  (References: REACTOME:REACT_1081.2|PUBMED:1550553)
RID: 55145 (;State transition'):
  Reactants: Isopentenyl diphosphate (annotations: CHEBI:CHEBI:16584)
  Products: DMAPP (annotations: CHEBI:CHEBI:57623)
  Modifiers: IDI1 (annotations: ,HGNC:5387,UNIPROT:Q13907,HGNC_SYMBOL:IDI1,REFSEQ:NM_004508,ENTREZ:3422); IDI2 (annotations: ENTREZ:91734,REFSEQ:NM_033261,HGNC_SYMBOL:IDI2,UNIPROT:Q9BXS1,,HGNC:23487)
  (References: WIKIPATHWAYS:WP4718|DOI:10.1016/B978-0-12-824048-9.00005-5)
RID: 55225 (;Known transition omitted'):
  Reactants: ELOVL5 (formerSymbols: SCA38) (annotations: REFSEQ:NM_021814,UNIPROT:Q9NYP7,HGNC_SYMBOL:ELOVL5,,ENTREZ:60481,HGNC:21308)
  Products: Fatty Acid Biosynthesis (annotations: WIKIPATHWAYS:WP4491,GO:GO:0006633)
  Modifiers: None
RID: 55189 (;State transition'):
  Reactants: Cholesterol (annotations: CHEBI:CHEBI:16113,KEGG_COMPOUND:C00187)
  Products: 4beta-hydroxycholesterol (annotations: CHEBI:CHEBI:85778)
  Modifiers: None
  (References: WIKIPATHWAYS:WP4718)
RID: 55957 (;Transport'):
  Reactants: Mitochondrial Beta-Oxidation (annotations: WIKIPATHWAYS:WP143)
  Products: Palmitoyl-CoA (annotations: CHEBI:CHEBI:15525)
  Modifiers: None
RID: 56079 (;Positive influence'):
  Reactants: NR1I3 (annotations: ENTREZ:9970,UNIPROT:Q14994,,HGNC:7969,REFSEQ:NM_001077469,HGNC_SYMBOL:NR1I3)
  Products: FOXO1 (formerSymbols: FKHR,FOXO1A) (annotations: HGNC:3819,,REFSEQ:NM_002015,ENTREZ:2308,HGNC_SYMBOL:FOXO1,UNIPROT:Q12778)
  Modifiers: None
RID: 55372 (PDmap:re614.0;State transition'):
  Reactants: prostaglandin G2 (annotations: CHEBI:CHEBI:27647)
  Products: prostaglandin H2 (annotations: CHEBI:CHEBI:15554,WIKIPEDIA:Prostaglandin H2,PUBCHEM:445049,KEGG_COMPOUND:C00427,CAS:42935-17-1,CHEMSPIDER:392800,HMDB:HMDB0001381); peroxide (annotations: CHEBI:CHEBI:44785)
  Modifiers: PTGS1:heme; PTGS2:heme
  (References: REACTOME:REACT_147811.1|REACTOME:REACT_810.8|PUBMED:11729303)
RID: 56178 (;State transition'):
  Reactants: Fructose-6-Phosphate (annotations: CHEBI:CHEBI:15946,CHEBI:CHEBI:16084)
  Products: Fructose-2,6-Bisphosphate (annotations: CHEBI:CHEBI:28602)
  Modifiers: PFKFB1 (formerSymbols: PFRX) (annotations: ENTREZ:5207,REFSEQ:NM_001271804,UNIPROT:P16118,HGNC:8872,HGNC_SYMBOL:PFKFB1,)
RID: 56086 (;Known transition omitted'):
  Reactants: Fatty Dicarboxilic Acid
  Products: Beta-Oxidation
  Modifiers: None
  (References: WIKIPATHWAYS:WP206)
RID: 55458 (PDmap:re555.0;State transition'):
  Reactants: palmitate (annotations: HMDB:HMDB0000220,PUBCHEM:985,KEGG_COMPOUND:C00249,WIKIPEDIA:Palmitic acid,CHEBI:CHEBI:7896,CAS:57-10-3,CHEMBL_COMPOUND:CHEMBL82293,CHEMSPIDER:960,CHEBI:CHEBI:15756,REACTOME:REACT_3374.1)
  Products: palmitoyl-CoA (annotations: REACTOME:REACT_11391.1,CHEMSPIDER:14902,PUBCHEM:15667,HMDB:HMDB0001338,KEGG_COMPOUND:C00154,CHEBI:CHEBI:15525,WIKIPEDIA:palmitoyl CoA,CAS:1763-10-6)
  Modifiers: ACSL6 (formerSymbols: FACL6) (annotations: ,HGNC:16496,UNIPROT:Q9UKU0,HGNC_SYMBOL:ACSL6,REFSEQ:NM_015256,ENTREZ:23305); ACSL5 (formerSymbols: FACL5) (annotations: ,REFSEQ:NM_016234,HGNC:16526,HGNC_SYMBOL:ACSL5,UNIPROT:Q9ULC5,ENTREZ:51703); ACSL3 (formerSymbols: FACL3) (annotations: REFSEQ:NM_004457,ENTREZ:2181,UNIPROT:O95573,,HGNC_SYMBOL:ACSL3,HGNC:3570); ACSL1 (formerSymbols: FACL2) (annotations: ENTREZ:2180,HGNC:3569,REFSEQ:NM_001995,UNIPROT:P33121,HGNC_SYMBOL:ACSL1,)
  (References: PUBMED:17379924|REACTOME:REACT_11137.3|PUBMED:10548543|PUBMED:17681178)
RID: 56174 (;State transition'):
  Reactants: Glycerol-3-Phosphate (annotations: CHEBI:CHEBI:15978)
  Products: Triacylglyceride synthesis (annotations: WIKIPATHWAYS:WP325)
  Modifiers: None
RID: 55646 (;Positive influence'):
  Reactants: not so very long FA-CoA
  Products: Very Long Fatty Acids-CoA
  Modifiers: None
RID: 55383 (PDmap:re582.0;State transition'):
  Reactants: hydrogen peroxide (annotations: PUBCHEM:784,HMDB:HMDB0003125,KEGG_COMPOUND:C00027,MESH_2012:D006861,CHEBI:CHEBI:16240,WIKIPEDIA:Hydrogen peroxide,CAS:7722-84-1,CHEMBL_COMPOUND:CHEMBL71595,CHEMSPIDER:763); Fe2+ (annotations: CHEBI:CHEBI:29033)
  Products: hydroxide (annotations: PUBCHEM:961,CHEBI:CHEBI:16234,KEGG_COMPOUND:C01328,HMDB:HMDB0001039,CHEMSPIDER:936,CAS:14280-30-9,WIKIPEDIA:Hydroxide,MESH_2012:C031356); Fe3+ (annotations: CHEBI:CHEBI:29034); hydroxyl (annotations: CHEBI:CHEBI:29191)
  Modifiers: None
  (References: PUBMED:2172697)
RID: 55536 (;Unknown positive influence'):
  Reactants: PKA
  Products: AMPK (annotations: GO:GO:0031588)
  Modifiers: None
RID: 55301 (PDmap:re581.0;State transition'):
  Reactants: glutathione disulfide (annotations: KEGG_COMPOUND:C00127,CHEBI:CHEBI:17858,HMDB:HMDB0003337,PUBCHEM:975,CAS:27025-41-8,WIKIPEDIA:Glutathione disulfide,CHEMBL_COMPOUND:CHEMBL1372,CHEMSPIDER:950); NADPH (annotations: KEGG_COMPOUND:C00005,HMDB:HMDB0000221,CHEMSPIDER:17215925,CHEMBL_COMPOUND:CHEMBL213053,CHEBI:CHEBI:16474,CAS:53-57-6,WIKIPEDIA:NADPH,PUBCHEM:22833512); H+ (annotations: CHEBI:CHEBI:15378)
  Products: glutathione (annotations: CHEMBL_COMPOUND:CHEMBL1543,CHEBI:CHEBI:16856,HMDB:HMDB0000125,KEGG_COMPOUND:C00051,WIKIPEDIA:Glutathione,CHEMSPIDER:111188,CAS:70-18-8,MESH_2012:D005978,PUBCHEM:124886); NADP(+) (annotations: CHEBI:CHEBI:18009,WIKIPEDIA:NADP,KEGG_COMPOUND:C00006,CAS:53-59-8,PUBCHEM:5886,CHEMBL_COMPOUND:CHEMBL213053,HMDB:HMDB0000217,CHEMSPIDER:5675)
  Modifiers: GSR (annotations: ,HGNC:4623,ENTREZ:2936,REFSEQ:NM_000637,HGNC_SYMBOL:GSR,UNIPROT:P00390)
  (References: PUBMED:19427899|REACTOME:REACT_264249)
RID: 56122 (;Transport'):
  Reactants: Acetyl-CoA (annotations: CHEBI:CHEBI:15351,CHEBI:CHEBI:57288)
  Products: Acetyl-CoA (annotations: CHEBI:CHEBI:15351,CHEBI:CHEBI:57288)
  Modifiers: None
RID: 55765 (;State transition'):
  Reactants: Trans-Hex-2-enoyl-CoA (annotations: CHEBI:CHEBI:28706)
  Products: (S)-Hydroxyhexanoyl-CoA (annotations: CHEBI:CHEBI:28276)
  Modifiers: ECHS1 (annotations: HGNC_SYMBOL:ECHS1,,ENTREZ:1892,UNIPROT:P30084,HGNC:3151,REFSEQ:NM_004092)
RID: 55694 (;State transition'):
  Reactants: Glycogen (n+1) (annotations: CHEBI:CHEBI:28087)
  Products: D-Glucose (annotations: CHEBI:CHEBI:4167)
  Modifiers: AGL (annotations: ,ENTREZ:178,HGNC_SYMBOL:AGL,UNIPROT:P35573,HGNC:321,REFSEQ:NM_000028)
RID: 55107 (;State transition'):
  Reactants: Cholesterol ester (annotations: CHEBI:CHEBI:17002)
  Products: Cholesterol (annotations: CHEBI:CHEBI:16113,KEGG_COMPOUND:C00187)
  Modifiers: LIPA (annotations: HGNC_SYMBOL:LIPA,ENTREZ:3988,,HGNC:6617,REFSEQ:NM_000235,UNIPROT:P38571)
  (References: WIKIPATHWAYS:WP5304)
RID: 55807 (;Transport'):
  Reactants: Long-chain Fatty Acids
  Products: Fatty acyl-CoA
  Modifiers: SLC27A
  (References: PUBMED:18477307)
RID: 55598 (;State transition'):
  Reactants: Octanoyl-CoA (annotations: CHEBI:CHEBI:15533)
  Products: Trans-Oct-2-enoyl-CoA (annotations: CHEBI:CHEBI:27537)
  Modifiers: ACADM (annotations: UNIPROT:P11310,HGNC_SYMBOL:ACADM,,HGNC:89,REFSEQ:NM_000016,ENTREZ:34)
RID: 55547 (;State transition'):
  Reactants: PFKFB
  Products: PFKFB
  Modifiers: AKT1 (annotations: ENTREZ:207,HGNC:391,PUBMED:28416361,HGNC_SYMBOL:AKT1,REFSEQ:NM_005163,UNIPROT:P31749,)
RID: 55687 (;Positive influence'):
  Reactants: SLC27A5 (annotations: HGNC:10999,REFSEQ:NM_012254,ENTREZ:10998,UNIPROT:Q9Y2P5,HGNC_SYMBOL:SLC27A5,)
  Products: Fatty Acid Transport (annotations: WIKIPATHWAYS:WP5061)
  Modifiers: None
RID: 55553 (;Positive influence'):
  Reactants: GCGR:GCG
  Products: Gα
  Modifiers: None
RID: 56050 (;Transport'):
  Reactants: Cholesterol ester (annotations: CHEBI:CHEBI:17002)
  Products: Cholesterol ester (annotations: CHEBI:CHEBI:17002)
  Modifiers: MTTP (formerSymbols: MTP) (annotations: HGNC:7467,REFSEQ:NM_000253,ENTREZ:4547,HGNC_SYMBOL:MTTP,,WIKIPATHWAYS:WP430,UNIPROT:P55157,PUBMED:18477307)
RID: 55796 (;Unknown negative influence'):
  Reactants: FOXO1 (formerSymbols: FKHR,FOXO1A) (annotations: HGNC:3819,,REFSEQ:NM_002015,ENTREZ:2308,PUBMED:28416361,HGNC_SYMBOL:FOXO1,UNIPROT:Q12778)
  Products: mTORC1 (annotations: GO:GO:0031931)
  Modifiers: None
RID: 56103 (;Positive influence'):
  Reactants: PPARG:PPARGC1A
  Products: PCK1 (annotations: ,PUBMED:28416361,HGNC:8724,UNIPROT:P35558,HGNC_SYMBOL:PCK1,REFSEQ:NM_002591,ENTREZ:5105)
  Modifiers: None
RID: 55478 (;Positive influence'):
  Reactants: MDM2 (annotations: HGNC:6973,ENTREZ:4193,REFSEQ:NM_002392,,HGNC_SYMBOL:MDM2,UNIPROT:Q00987)
  Products: Apoptosis (annotations: GO:GO:1900117,GO:GO:0097194)
  Modifiers: None
RID: 55393 (PDmap:re53.0;State transition'):
  Reactants: 2-oxoglutaric acid (annotations: KEGG_COMPOUND:C00026,REACTOME:REACT_3871.1,CHEBI:CHEBI:30915,CAS:328-50-7,MESH_2012:C029743,PUBCHEM:51,CHEMSPIDER:50,HMDB:HMDB0000208,WIKIPEDIA:Alpha-Ketoglutaric_acid); coenzyme A (annotations: CHEBI:CHEBI:15346,REACTOME:REACT_3654.2); NAD(+) (annotations: KEGG_COMPOUND:C00003,CAS:53-84-9,PUBCHEM:5893,CHEMSPIDER:5682,REACTOME:REACT_4970.1,CHEBI:CHEBI:15846,HMDB:HMDB0000902,WIKIPEDIA:NAD)
  Products: succinyl-CoA (annotations: HMDB:HMDB0001022,CHEMSPIDER:388307,KEGG_COMPOUND:C00091,WIKIPEDIA:Succinyl-CoA,REACTOME:REACT_2852.1,CAS:604-98-8,CHEBI:CHEBI:15380,PUBCHEM:439161); H+ (annotations: CHEBI:CHEBI:15378); NADH (annotations: REACTOME:REACT_2390.1,KEGG_COMPOUND:C00004,HMDB:HMDB0001487,CHEMSPIDER:903,WIKIPEDIA:NADH,CAS:58-68-4,CHEBI:CHEBI:16908,PUBCHEM:928,CHEMBL_COMPOUND:CHEMBL1628272,MESH_2012:D009243); CO2 (annotations: CHEMSPIDER:274,CHEBI:CHEBI:16526,MESH_2012:D002245,CHEMBL_COMPOUND:CHEMBL1231871,PUBCHEM:280,WIKIPEDIA:Carbon Dioxide,HMDB:HMDB0001967,KEGG_COMPOUND:C00011,CAS:124-38-9)
  Modifiers: alpha-ketoglutarate dehydrogenase (annotations: REACTOME:REACT_5646.1,GO:GO:0045252); Ca2+ (annotations: CHEBI:CHEBI:29108)
  (References: PUBMED:11752427|PUBMED:20144582|PUBMED:15946682|PUBMED:9727038|PUBMED:19413950|PUBMED:2188967|REACTOME:REACT_66.3)
RID: 55853 (;Negative influence'):
  Reactants: NR1I3 (annotations: ENTREZ:9970,UNIPROT:Q14994,,HGNC:7969,REFSEQ:NM_001077469,HGNC_SYMBOL:NR1I3)
  Products: PPARGC1A (formerSymbols: PPARGC1) (annotations: UNIPROT:Q9UBK2,ENTREZ:10891,HGNC:9237,HGNC_SYMBOL:PPARGC1A,,REFSEQ:NM_013261)
  Modifiers: None
RID: 55767 (;Known transition omitted'):
  Reactants: Acyl Dihydroxyacetone Phosphate; Acyl CoA (annotations: CHEBI:CHEBI:37554,CHEBI:CHEBI:58342)
  Products: Lysophosphatidic Acid (annotations: CHEBI:CHEBI:32957)
  Modifiers: None
RID: 55673 (;Transport'):
  Reactants: H+ (annotations: CHEBI:CHEBI:15378)
  Products: H+ (annotations: CHEBI:CHEBI:15378)
  Modifiers: UCP3 (annotations: HGNC_SYMBOL:UCP3,UNIPROT:P55916,REFSEQ:NM_003356,,ENTREZ:7352,PUBMED:18477307,HGNC:12519)
RID: 55143 (;Known transition omitted'):
  Reactants: SCD (formerSymbols: SCDOS) (annotations: ,ENTREZ:6319,HGNC_SYMBOL:SCD,UNIPROT:O00767,HGNC:10571,REFSEQ:NM_005063)
  Products: Fatty Acid Biosynthesis (annotations: WIKIPATHWAYS:WP4491,GO:GO:0006633)
  Modifiers: None
RID: 55761 (;Positive influence'):
  Reactants: Fatty Acids
  Products: PPARA (formerSymbols: PPAR) (annotations: HGNC_SYMBOL:PPARA,ENTREZ:5465,REFSEQ:NM_001001928,,PUBMED:26451809,UNIPROT:Q07869,HGNC:9232)
  Modifiers: None
RID: 56214 (;State transition'):
  Reactants: Fibulose-5-Phosphate
  Products: Ribose-5-Phosphate (annotations: CHEBI:CHEBI:78679)
  Modifiers: RPIA (annotations: ,REFSEQ:NM_144563,HGNC:10297,HGNC_SYMBOL:RPIA,ENTREZ:22934,UNIPROT:P49247)
  (References: WIKIPATHWAYS:WP134)
RID: 55518 (;State transition'):
  Reactants: PIP3
  Products: PIP2
  Modifiers: PTEN (formerSymbols: BZS,MHAM) (annotations: HGNC:9588,HGNC_SYMBOL:PTEN,ENTREZ:5728,,REFSEQ:NM_000314,UNIPROT:P60484)
RID: 55331 (PDmap:re435.0;State transition'):
  Reactants: isocitrate dehydrogenase (annotations: REACTOME:REACT_21933.1)
  Products: isocitrate dehydrogenase (annotations: REACTOME:REACT_21933.1)
  Modifiers: SIRT3 (annotations: ENTREZ:23410,HGNC_SYMBOL:SIRT3,UNIPROT:Q9NTG7,HGNC:14931,REFSEQ:NM_001017524,)
  (References: PUBMED:21094524|PUBMED:21658599)
RID: 55155 (;State transition'):
  Reactants: SREBF1 (annotations: UNIPROT:P36956,REFSEQ:NM_004176,ENTREZ:6720,HGNC:11289,HGNC_SYMBOL:SREBF1,)
  Products: SREBF1 (annotations: UNIPROT:P36956,REFSEQ:NM_004176,ENTREZ:6720,HGNC:11289,HGNC_SYMBOL:SREBF1,)
  Modifiers: NR1H3 (annotations: REFSEQ:NM_001130101,,HGNC:7966,ENTREZ:10062,UNIPROT:Q13133,HGNC_SYMBOL:NR1H3); NR1H2 (formerSymbols: UNR) (annotations: UNIPROT:P55055,ENTREZ:7376,REFSEQ:NM_001256647,HGNC:7965,,HGNC_SYMBOL:NR1H2)
  (References: WIKIPATHWAYS:WP4718)
RID: 55284 (;Known transition omitted'):
  Reactants: long-chain fatty acid (annotations: CHEBI:CHEBI:15904)
  Products: fatty acyl-CoA (annotations: CHEBI:CHEBI:37554,REACTOME:REACT_5036.3)
  Modifiers: ACSL3 (formerSymbols: FACL3) (annotations: REFSEQ:NM_004457,ENTREZ:2181,UNIPROT:O95573,,HGNC_SYMBOL:ACSL3,HGNC:3570); ACSL1 (formerSymbols: FACL2) (annotations: ENTREZ:2180,HGNC:3569,REFSEQ:NM_001995,UNIPROT:P33121,HGNC_SYMBOL:ACSL1,); ACAS2; ACSL4 (formerSymbols: FACL4,MRX63,MRX68) (annotations: HGNC:3571,REFSEQ:NM_004458,ENTREZ:2182,HGNC_SYMBOL:ACSL4,UNIPROT:O60488,); ACSL5 (formerSymbols: FACL5) (annotations: ,REFSEQ:NM_016234,HGNC:16526,HGNC_SYMBOL:ACSL5,UNIPROT:Q9ULC5,ENTREZ:51703); ACSL6 (formerSymbols: FACL6) (annotations: ,HGNC:16496,UNIPROT:Q9UKU0,HGNC_SYMBOL:ACSL6,REFSEQ:NM_015256,ENTREZ:23305)
  (References: WIKIPATHWAYS:WP357)
RID: 55920 (;State transition'):
  Reactants: Malate (annotations: CHEBI:CHEBI:15595,CHEBI:CHEBI:30797)
  Products: Oxalacetate (annotations: CHEBI:CHEBI:16452)
  Modifiers: MDH1 (annotations: HGNC_SYMBOL:MDH1,UNIPROT:P40925,HGNC:6970,ENTREZ:4190,REFSEQ:NM_001316374,)
RID: 55992 (;Positive influence'):
  Reactants: NFE2L2 (annotations: UNIPROT:Q16236,,PUBMED:28416361,ENTREZ:4780,REFSEQ:NM_006164,HGNC:7782,HGNC_SYMBOL:NFE2L2)
  Products: PPARA (formerSymbols: PPAR) (annotations: HGNC_SYMBOL:PPARA,ENTREZ:5465,REFSEQ:NM_001001928,,PUBMED:26451809,UNIPROT:Q07869,HGNC:9232)
  Modifiers: None
RID: 55243 (PDmap:re465.0;State transition'):
  Reactants: acetate (annotations: CHEBI:CHEBI:30089,KEGG_COMPOUND:C00033)
  Products: acetyl-CoA (annotations: CHEBI:CHEBI:15351,WIKIPEDIA:Acetyl-CoA,HMDB:HMDB0001206,CHEMSPIDER:392413,PUBCHEM:444493,REACTOME:REACT_3839.1,CAS:72-89-9,KEGG_COMPOUND:C00024)
  Modifiers: ACSS1 (formerSymbols: ACAS2L) (annotations: HGNC_SYMBOL:ACSS1,,REFSEQ:NM_032501,ENTREZ:84532,UNIPROT:Q9NUB1,HGNC:16091)
  (References: KEGG_REACTION:R00235)
RID: 55493 (;Positive influence'):
  Reactants: PCK1 (annotations: ,PUBMED:28416361,HGNC:8724,UNIPROT:P35558,HGNC_SYMBOL:PCK1,REFSEQ:NM_002591,ENTREZ:5105)
  Products: Gluconeogenesis (annotations: GO:GO:0006094)
  Modifiers: None
RID: 56109 (;Positive influence'):
  Reactants: PPARG (annotations: HGNC:9236,REFSEQ:NM_005037,HGNC_SYMBOL:PPARG,UNIPROT:P37231,,ENTREZ:5468)
  Products: HSD17B10 (formerSymbols: HADH2,MRXS10) (annotations: HGNC_SYMBOL:HSD17B10,,UNIPROT:Q99714,REFSEQ:NM_004493,HGNC:4800,ENTREZ:3028)
  Modifiers: None
RID: 55735 (;State transition'):
  Reactants: mTORC1 (annotations: GO:GO:0031931)
  Products: mTORC1 (annotations: GO:GO:0031931)
  Modifiers: TSC (annotations: PUBMED:28416361)
RID: 55446 (PDmap:re464.0;State transition'):
  Reactants: acetaldehyde (annotations: WIKIPEDIA:Acetaldehyde,CHEBI:CHEBI:15343,HMDB:HMDB0000990,MESH_2012:D000079,CAS:75-07-0,CHEMSPIDER:172,KEGG_COMPOUND:C00084,CHEMBL_COMPOUND:CHEMBL170365,PUBCHEM:177)
  Products: acetate (annotations: CHEBI:CHEBI:30089,KEGG_COMPOUND:C00033)
  Modifiers: ALDH2 (annotations: HGNC_SYMBOL:ALDH2,ENTREZ:217,,REFSEQ:NM_000690,HGNC:404,UNIPROT:P05091)
  (References: KEGG_REACTION:R00710)
RID: 55358 (;State transition'):
  Reactants: glutathione (annotations: CHEMBL_COMPOUND:CHEMBL1543,CHEBI:CHEBI:16856,HMDB:HMDB0000125,KEGG_COMPOUND:C00051,WIKIPEDIA:Glutathione,CHEMSPIDER:111188,CAS:70-18-8,MESH_2012:D005978,PUBCHEM:124886); hydrogen peroxide (annotations: PUBCHEM:784,HMDB:HMDB0003125,KEGG_COMPOUND:C00027,MESH_2012:D006861,CHEBI:CHEBI:16240,WIKIPEDIA:Hydrogen peroxide,CAS:7722-84-1,CHEMBL_COMPOUND:CHEMBL71595,CHEMSPIDER:763)
  Products: glutathione disulfide (annotations: KEGG_COMPOUND:C00127,CHEBI:CHEBI:17858,HMDB:HMDB0003337,PUBCHEM:975,CAS:27025-41-8,WIKIPEDIA:Glutathione disulfide,CHEMBL_COMPOUND:CHEMBL1372,CHEMSPIDER:950); H2O (annotations: HMDB:HMDB0002111,CHEBI:CHEBI:15377,PUBCHEM:962,CHEMSPIDER:937,MESH_2012:D014867,WIKIPEDIA:Water,CAS:7732-18-5,CHEMBL_COMPOUND:CHEMBL1098659,KEGG_COMPOUND:C00001)
  Modifiers: PRDX6:GSTP1
  (References: REACTOME:REACT_264249)
RID: 55375 (;State transition'):
  Reactants: superoxide (annotations: HMDB:HMDB0002168,WIKIPEDIA:Superoxide,PUBCHEM:5359597,CHEMSPIDER:4514331,KEGG_COMPOUND:C00704,CHEBI:CHEBI:18421,CAS:11062-77-4); H+ (annotations: CHEBI:CHEBI:15378)
  Products: hydrogen peroxide (annotations: PUBCHEM:784,HMDB:HMDB0003125,KEGG_COMPOUND:C00027,MESH_2012:D006861,CHEBI:CHEBI:16240,WIKIPEDIA:Hydrogen peroxide,CAS:7722-84-1,CHEMBL_COMPOUND:CHEMBL71595,CHEMSPIDER:763); O2 (annotations: CHEBI:CHEBI:15379,KEGG_COMPOUND:C00007,HMDB:HMDB0001377,PUBCHEM:977,CHEMSPIDER:952,CAS:7782-44-7,WIKIPEDIA:Oxygen)
  Modifiers: SOD1:Zn2+:Cu2+
  (References: REACTOME:REACT_264249)
RID: 55730 (;State transition'):
  Reactants: PFKFB
  Products: PFKFB
  Modifiers: AKT1 (annotations: ENTREZ:207,HGNC:391,PUBMED:28416361,HGNC_SYMBOL:AKT1,REFSEQ:NM_005163,UNIPROT:P31749,)
RID: 55607 (;State transition'):
  Reactants: Glyceralaldehyde-3-Phosphate (annotations: CHEBI:CHEBI:17138)
  Products: Dihydroxyacetone-Phosphate (annotations: CHEBI:CHEBI:16108)
  Modifiers: TPI1 (annotations: HGNC_SYMBOL:TPI1,REFSEQ:NM_000365,HGNC:12009,ENTREZ:7167,UNIPROT:P60174,)
RID: 55212 (;Transcription'):
  Reactants: ACOT2 (annotations: REFSEQ:NM_006821,HGNC_SYMBOL:ACOT2,,ENTREZ:10965,HGNC:18431,UNIPROT:P49753)
  Products: ACOT2 (annotations: REFSEQ:NM_006821,HGNC_SYMBOL:ACOT2,,ENTREZ:10965,HGNC:18431,UNIPROT:P49753)
  Modifiers: SREBF2 (annotations: HGNC:11290,REFSEQ:NM_004599,UNIPROT:Q12772,,HGNC_SYMBOL:SREBF2,ENTREZ:6721)
  (References: WIKIPATHWAYS:WP4718)
RID: 55682 (;Positive influence'):
  Reactants: Prostaglandins
  Products: PPARG (annotations: HGNC:9236,REFSEQ:NM_005037,HGNC_SYMBOL:PPARG,UNIPROT:P37231,,ENTREZ:5468)
  Modifiers: None
RID: 55491 (;Unknown positive influence'):
  Reactants: AKT1 (annotations: ENTREZ:207,HGNC:391,PUBMED:28416361,HGNC_SYMBOL:AKT1,REFSEQ:NM_005163,UNIPROT:P31749,)
  Products: Glycogen Synthesis (annotations: GO:GO:0005978,PUBMED:28416361)
  Modifiers: None
RID: 55510 (;Positive influence'):
  Reactants: BAD (annotations: REFSEQ:NM_032989,UNIPROT:Q92934,ENTREZ:572,,HGNC_SYMBOL:BAD,HGNC:936)
  Products: Apoptosis (annotations: GO:GO:1900117,GO:GO:0097194)
  Modifiers: None
RID: 55132 (;Transport'):
  Reactants: Long-chain Fatty Acids (annotations: CHEBI:CHEBI:15904)
  Products: Long-chain Fatty Acids (annotations: CHEBI:CHEBI:15904)
  Modifiers: SLC27
  (References: PUBMED:12856180)
RID: 55315 (PDmap:re544.0;State transition'):
  Reactants: (2-trans,6-cis)-dodeca-2,6-dienoyl-CoA (annotations: CHEBI:CHEBI:28387,REACTOME:REACT_4665.1)
  Products: cis-dec-4-enoyl-CoA (annotations: PUBCHEM:6443609,REACTOME:REACT_4645.1,CHEBI:CHEBI:29140)
  Modifiers: ACADL (annotations: REFSEQ:NM_001608,,HGNC_SYMBOL:ACADL,HGNC:88,ENTREZ:33,UNIPROT:P28330); trifunctional Protein
  (References: REACTOME:REACT_440.2)
RID: 55247 (PDmap:re550.0;State transition'):
  Reactants: ACACB (annotations: UNIPROT:O00763,HGNC_SYMBOL:ACACB,HGNC:85,REFSEQ:NM_001093,ENTREZ:32,)
  Products: ACACB (annotations: UNIPROT:O00763,HGNC_SYMBOL:ACACB,HGNC:85,REFSEQ:NM_001093,ENTREZ:32,)
  Modifiers: AMPK (annotations: GO:GO:0031588)
  (References: REACTOME:REACT_11110.3|PUBMED:15060529)
RID: 55800 (;State transition'):
  Reactants: HMG-CoA (annotations: CHEBI:CHEBI:15467)
  Products: Acetoacetate (annotations: CHEBI:CHEBI:13705); Acetyl-CoA (annotations: CHEBI:CHEBI:15351,CHEBI:CHEBI:57288)
  Modifiers: HMGCL (annotations: HGNC:5005,REFSEQ:NM_000191,UNIPROT:P35914,HGNC_SYMBOL:HMGCL,ENTREZ:3155,)
RID: 55134 (;Transport'):
  Reactants: Cholesterol (annotations: CHEBI:CHEBI:16113,KEGG_COMPOUND:C00187)
  Products: Cholesterol (annotations: CHEBI:CHEBI:16113,KEGG_COMPOUND:C00187)
  Modifiers: VDAC1:STAR; TSPO (formerSymbols: BZRP) (annotations: HGNC:1158,HGNC_SYMBOL:TSPO,REFSEQ:NM_007311,,UNIPROT:P30536,ENTREZ:706,UNIPROT:B1AH88)
  (References: WIKIPATHWAYS:WP5304)
RID: 55089 (;State transition'):
  Reactants: Triacylglycerol
  Products: DAG
  Modifiers: PNPLA2 (annotations: ,ENTREZ:57104,REFSEQ:NM_020376,HGNC:30802,UNIPROT:Q96AD5,HGNC_SYMBOL:PNPLA2); LIPA (annotations: HGNC_SYMBOL:LIPA,ENTREZ:3988,,HGNC:6617,REFSEQ:NM_000235,UNIPROT:P38571)
RID: 55787 (;Positive influence'):
  Reactants: mTORC1 (annotations: GO:GO:0031931)
  Products: GCK (formerSymbols: MODY2) (annotations: ,ENTREZ:2645,HGNC_SYMBOL:GCK,PUBMED:28416361,REFSEQ:NM_000162,UNIPROT:P35557,HGNC:4195)
  Modifiers: None
RID: 55716 (;State transition'):
  Reactants: Phosphoenolpyruvate (annotations: CHEBI:CHEBI:18021,CHEBI:CHEBI:44897,CHEBI:CHEBI:58702)
  Products: Pyruvate (annotations: CHEBI:CHEBI:15361)
  Modifiers: PKLR (annotations: HGNC_SYMBOL:PKLR,REFSEQ:NM_000298,PUBMED:31284506,HGNC:9020,UNIPROT:P30613,ENTREZ:5313,)
RID: 55296 (PDmap:re530.0;State transition'):
  Reactants: hexanoyl-CoA (annotations: KEGG_COMPOUND:C05270,CHEBI:CHEBI:27540,CHEMSPIDER:389509,HMDB:HMDB0002845,CAS:5060-32-2,PUBCHEM:440611,REACTOME:REACT_5004.1)
  Products: trans-hex-2-enoyl-CoA (annotations: CAS:10018-93-6,PUBCHEM:5280765,KEGG_COMPOUND:C05271,CHEBI:CHEBI:28706,HMDB:HMDB0003944,CHEMSPIDER:4444331,REACTOME:REACT_2759.1)
  Modifiers: ACADS (annotations: HGNC:90,UNIPROT:P16219,HGNC_SYMBOL:ACADS,,ENTREZ:35,REFSEQ:NM_000017)
  (References: REACTOME:REACT_1742.2|PUBMED:13295225|PUBMED:3597357)
RID: 55182 (;State transition'):
  Reactants: NR1H2 (formerSymbols: UNR) (annotations: UNIPROT:P55055,ENTREZ:7376,REFSEQ:NM_001256647,HGNC:7965,,HGNC_SYMBOL:NR1H2)
  Products: NR1H2 (formerSymbols: UNR) (annotations: UNIPROT:P55055,ENTREZ:7376,REFSEQ:NM_001256647,HGNC:7965,,HGNC_SYMBOL:NR1H2)
  Modifiers: None
  (References: WIKIPATHWAYS:WP4718)
RID: 55578 (;State transition'):
  Reactants: CD36 (annotations: HGNC:1663,REFSEQ:NM_001001547,HGNC_SYMBOL:CD36,,ENTREZ:948,UNIPROT:P16671,PUBMED:18477307)
  Products: CD36 (annotations: HGNC:1663,REFSEQ:NM_001001547,HGNC_SYMBOL:CD36,,ENTREZ:948,UNIPROT:P16671,PUBMED:18477307)
  Modifiers: Long-chain Fatty Acids
  (References: PUBMED:18477307)
RID: 55479 (;Positive influence'):
  Reactants: SREBF1 (annotations: PUBMED:28416361,UNIPROT:P36956,REFSEQ:NM_004176,ENTREZ:6720,HGNC:11289,HGNC_SYMBOL:SREBF1,)
  Products: Lipogenesis (annotations: GO:GO:0008610)
  Modifiers: None
RID: 55696 (;Positive influence'):
  Reactants: PPARA (formerSymbols: PPAR) (annotations: HGNC_SYMBOL:PPARA,ENTREZ:5465,REFSEQ:NM_001001928,,PUBMED:26451809,UNIPROT:Q07869,HGNC:9232)
  Products: ACOX (annotations: PUBMED:26451809,PUBMED:18477307)
  Modifiers: None
  (References: PUBMED:8567672)
RID: 55903 (;Unknown positive influence'):
  Reactants: AKT1 (annotations: ENTREZ:207,HGNC:391,PUBMED:28416361,HGNC_SYMBOL:AKT1,REFSEQ:NM_005163,UNIPROT:P31749,)
  Products: Glycogen Synthesis (annotations: GO:GO:0005978,PUBMED:28416361)
  Modifiers: None
RID: 55746 (;Transport'):
  Reactants: FA =/< C12
  Products: FA =/< C12
  Modifiers: Diffusion (annotations: PUBMED:18477307)
RID: 55918 (;Positive influence'):
  Reactants: PPARA (formerSymbols: PPAR) (annotations: HGNC_SYMBOL:PPARA,ENTREZ:5465,REFSEQ:NM_001001928,,PUBMED:26451809,UNIPROT:Q07869,HGNC:9232)
  Products: FABP1 (annotations: REFSEQ:NM_001443,UNIPROT:P07148,,HGNC:3555,HGNC_SYMBOL:FABP1,ENTREZ:2168)
  Modifiers: None
RID: 55429 (;Physical stimulation'):
  Reactants: TFAM (formerSymbols: TCF6,TCF6L2) (annotations: REFSEQ:NM_003201,HGNC:11741,HGNC_SYMBOL:TFAM,UNIPROT:Q00059,,ENTREZ:7019)
  Products: mt DNA replication
  Modifiers: None
  (References: PUBMED:23149385|TAXONOMY:4891|DOI:10.1101/gad.316547.118)
RID: 56200 (;State transition'):
  Reactants: Oxalacetate (annotations: CHEBI:CHEBI:16452)
  Products: Phosphoenolpyruvate (annotations: CHEBI:CHEBI:18021,CHEBI:CHEBI:44897,CHEBI:CHEBI:58702)
  Modifiers: PCK2 (annotations: HGNC:8725,REFSEQ:NM_001018073,HGNC_SYMBOL:PCK2,ENTREZ:5106,,UNIPROT:Q16822); PCK1 (annotations: ,HGNC:8724,UNIPROT:P35558,HGNC_SYMBOL:PCK1,REFSEQ:NM_002591,ENTREZ:5105)
RID: 56087 (;Transport'):
  Reactants: Triacylglycerol (annotations: CHEBI:CHEBI:17855)
  Products: Lipid droplets
  Modifiers: None
RID: 55890 (;State transition'):
  Reactants: Glucose-1-Phosphate (annotations: CHEBI:CHEBI:29042)
  Products: UDP-Glucose (annotations: CHEBI:CHEBI:18066)
  Modifiers: UGP2 (formerSymbols: UGP1) (annotations: HGNC_SYMBOL:UGP2,ENTREZ:7360,UNIPROT:Q16851,HGNC:12527,,REFSEQ:NM_006759)
RID: 55769 (;State transition'):
  Reactants: Acetyl-CoA (annotations: CHEBI:CHEBI:15351,CHEBI:CHEBI:57288)
  Products: Malonyl-ACP (annotations: CHEBI:CHEBI:81869,CHEBI:CHEBI:81867,CHEBI:CHEBI:81868)
  Modifiers: ACAC
RID: 55452 (PDmap:re563.0;State transition'):
  Reactants: glycerone phosphate (annotations: HMDB:HMDB0001473,WIKIPEDIA:Dihydroxyacetone phosphate,CHEMSPIDER:648,PUBCHEM:668,CHEBI:CHEBI:16108,CAS:57-04-5,KEGG_COMPOUND:C00111)
  Products: sn-glycerol 3-phosphate (annotations: CHEMSPIDER:388308,KEGG_COMPOUND:C00093,WIKIPEDIA:Glycerol 3-phosphate,HMDB:HMDB0000126,REACTOME:REACT_4327.2,CHEBI:CHEBI:15978,PUBCHEM:439162,CAS:57-03-4)
  Modifiers: GPD1 (annotations: ,UNIPROT:P21695,HGNC:4455,HGNC_SYMBOL:GPD1,ENTREZ:2819,REFSEQ:NM_001257199)
  (References: REACTOME:REACT_1146.4|PUBMED:16460752)
RID: 55290 (PDmap:re549.0;State transition'):
  Reactants: acetyl-CoA (annotations: CHEBI:CHEBI:15351,WIKIPEDIA:Acetyl-CoA,HMDB:HMDB0001206,CHEMSPIDER:392413,PUBCHEM:444493,REACTOME:REACT_3839.1,CAS:72-89-9,KEGG_COMPOUND:C00024); hydrogencarbonate (annotations: CHEMBL_COMPOUND:CHEMBL363707,CAS:71-52-3,HMDB:HMDB0000595,REACTOME:REACT_4357.1,CHEMSPIDER:749,PUBCHEM:769,WIKIPEDIA:Bicarbonate,CHEBI:CHEBI:17544,KEGG_COMPOUND:C00288)
  Products: malonyl-CoA (annotations: REACTOME:REACT_3059.1,WIKIPEDIA:Malonyl-CoA,HMDB:HMDB0001175,CAS:524-14-1,CHEBI:CHEBI:15531,PUBCHEM:10663,KEGG_COMPOUND:C00083,CHEMSPIDER:10213)
  Modifiers: ACACB (annotations: UNIPROT:O00763,HGNC_SYMBOL:ACACB,HGNC:85,REFSEQ:NM_001093,ENTREZ:32,)
  (References: PUBMED:9099716|PUBMED:17223360|REACTOME:REACT_590.3|PUBMED:10677481)
RID: 55515 (;State transition'):
  Reactants: AKT1 (annotations: ENTREZ:207,HGNC:391,PUBMED:28416361,HGNC_SYMBOL:AKT1,REFSEQ:NM_005163,UNIPROT:P31749,)
  Products: AKT1 (annotations: ENTREZ:207,HGNC:391,PUBMED:28416361,HGNC_SYMBOL:AKT1,REFSEQ:NM_005163,UNIPROT:P31749,)
  Modifiers: PHLPP1 (formerSymbols: PHLPP,PLEKHE1) (annotations: HGNC:20610,,HGNC_SYMBOL:PHLPP1,REFSEQ:NM_194449,UNIPROT:O60346,ENTREZ:23239)
RID: 56132 (;State transition'):
  Reactants: Glyceraldehyde (annotations: CHEBI:CHEBI:5445,CHEBI:CHEBI:17378)
  Products: Glycerol (annotations: CHEBI:CHEBI:17754)
  Modifiers: None
RID: 56173 (;State transition'):
  Reactants: Fibulose-5-Phosphate
  Products: Xylulosse-5-Phosphate (annotations: CHEBI:CHEBI:16332)
  Modifiers: RPE (annotations: ,ENTREZ:6120,UNIPROT:Q96AT9,REFSEQ:NM_006916,HGNC_SYMBOL:RPE,HGNC:10293)
  (References: WIKIPATHWAYS:WP134)
RID: 55828 (;Positive influence'):
  Reactants: PYGL (annotations: ENTREZ:5836,REFSEQ:NM_002863,HGNC_SYMBOL:PYGL,HGNC:9725,,UNIPROT:P06737)
  Products: Glycogen breakdown
  Modifiers: None
RID: 55577 (;State transition'):
  Reactants: Glycerol-3-Phosphate (annotations: CHEBI:CHEBI:15978)
  Products: Dihydroxyacetone-Phosphate (annotations: CHEBI:CHEBI:16108)
  Modifiers: GPD2 (annotations: ENTREZ:2820,HGNC:4456,REFSEQ:NM_000408,,UNIPROT:P43304,HGNC_SYMBOL:GPD2)
RID: 55416 (;Transport'):
  Reactants: glutathione (annotations: CHEMBL_COMPOUND:CHEMBL1543,CHEBI:CHEBI:16856,HMDB:HMDB0000125,KEGG_COMPOUND:C00051,WIKIPEDIA:Glutathione,CHEMSPIDER:111188,CAS:70-18-8,MESH_2012:D005978,PUBCHEM:124886)
  Products: glutathione (annotations: CHEMBL_COMPOUND:CHEMBL1543,CHEBI:CHEBI:16856,HMDB:HMDB0000125,KEGG_COMPOUND:C00051,WIKIPEDIA:Glutathione,CHEMSPIDER:111188,CAS:70-18-8,MESH_2012:D005978,PUBCHEM:124886)
  Modifiers: SLC25A11 (formerSymbols: SLC20A4) (annotations: REFSEQ:NM_003562,HGNC:10981,ENTREZ:8402,UNIPROT:Q02978,HGNC_SYMBOL:SLC25A11,); SLC25A10 (formerSymbols: DIC) (annotations: ENTREZ:1468,UNIPROT:Q9UBX3,REFSEQ:NM_001270888,HGNC:10980,,HGNC_SYMBOL:SLC25A10)
  (References: PUBMED:25024695|PUBMED:23283974)
RID: 55540 (;State transition'):
  Reactants: PYGL (annotations: ENTREZ:5836,REFSEQ:NM_002863,HGNC_SYMBOL:PYGL,HGNC:9725,,UNIPROT:P06737)
  Products: PYGL (annotations: ENTREZ:5836,REFSEQ:NM_002863,HGNC_SYMBOL:PYGL,HGNC:9725,,UNIPROT:P06737)
  Modifiers: None
RID: 55572 (;Positive influence'):
  Reactants: FOXO1 (formerSymbols: FKHR,FOXO1A) (annotations: HGNC:3819,,REFSEQ:NM_002015,ENTREZ:2308,PUBMED:28416361,HGNC_SYMBOL:FOXO1,UNIPROT:Q12778)
  Products: GCK (formerSymbols: MODY2) (annotations: ,ENTREZ:2645,HGNC_SYMBOL:GCK,PUBMED:28416361,REFSEQ:NM_000162,UNIPROT:P35557,HGNC:4195)
  Modifiers: None
RID: 55156 (;Transcription'):
  Reactants: ABCA1 (formerSymbols: ABC1,HDLDT1) (annotations: REFSEQ:NM_005502,HGNC:29,HGNC_SYMBOL:ABCA1,,ENTREZ:19,UNIPROT:O95477)
  Products: ABCA1 (formerSymbols: ABC1,HDLDT1) (annotations: REFSEQ:NM_005502,HGNC:29,HGNC_SYMBOL:ABCA1,,ENTREZ:19,UNIPROT:O95477)
  Modifiers: SREBF1 (annotations: UNIPROT:P36956,REFSEQ:NM_004176,ENTREZ:6720,HGNC:11289,HGNC_SYMBOL:SREBF1,)
  (References: WIKIPATHWAYS:WP4718)
RID: 55656 (;State transition'):
  Reactants: 2-trans-4-cis-decadienoyl-CoA (annotations: CHEBI:CHEBI:29119)
  Products: 3-trans-decenoyl-CoA (annotations: CHEBI:CHEBI:29126)
  Modifiers: DECR1 (formerSymbols: DECR) (annotations: ENTREZ:1666,UNIPROT:Q16698,HGNC:2753,HGNC_SYMBOL:DECR1,REFSEQ:NM_001330575,)
RID: 55489 (;State transition'):
  Reactants: GSK3B (annotations: HGNC_SYMBOL:GSK3B,ENTREZ:2932,PUBMED:28416361,,HGNC:4617,UNIPROT:P49841,REFSEQ:NM_001146156)
  Products: GSK3B (annotations: HGNC_SYMBOL:GSK3B,ENTREZ:2932,PUBMED:28416361,,HGNC:4617,UNIPROT:P49841,REFSEQ:NM_001146156)
  Modifiers: AKT1 (annotations: ENTREZ:207,HGNC:391,PUBMED:28416361,HGNC_SYMBOL:AKT1,REFSEQ:NM_005163,UNIPROT:P31749,)
RID: 55474 (;Positive influence'):
  Reactants: mTORC1 (annotations: GO:GO:0031931)
  Products: Protein Synthesis
  Modifiers: None
RID: 56205 (;Transport'):
  Reactants: α-Ketogluatarate (annotations: CHEBI:CHEBI:30915)
  Products: α-Ketogluatarate (annotations: CHEBI:CHEBI:30915)
  Modifiers: GLAST1
RID: 56110 (;State transition'):
  Reactants: Malonyl-ACP (annotations: CHEBI:CHEBI:81869,CHEBI:CHEBI:81867,CHEBI:CHEBI:81868)
  Products: Acetyl-CoA (annotations: CHEBI:CHEBI:15351,CHEBI:CHEBI:57288)
  Modifiers: MLYCD (annotations: HGNC_SYMBOL:MLYCD,REFSEQ:NM_012213,ENTREZ:23417,,HGNC:7150,UNIPROT:O95822)
RID: 55461 (;State transition'):
  Reactants: IRS2 (annotations: UNIPROT:Q9Y4H2,HGNC:6126,ENTREZ:8660,HGNC_SYMBOL:IRS2,,REFSEQ:NM_003749)
  Products: IRS2 (annotations: UNIPROT:Q9Y4H2,HGNC:6126,ENTREZ:8660,HGNC_SYMBOL:IRS2,,REFSEQ:NM_003749)
  Modifiers: INSR:INS
RID: 55268 (PDmap:re550.0;State transition'):
  Reactants: ACACB (annotations: UNIPROT:O00763,HGNC_SYMBOL:ACACB,HGNC:85,REFSEQ:NM_001093,ENTREZ:32,)
  Products: ACACB (annotations: UNIPROT:O00763,HGNC_SYMBOL:ACACB,HGNC:85,REFSEQ:NM_001093,ENTREZ:32,)
  Modifiers: AMPK (annotations: GO:GO:0031588)
  (References: REACTOME:REACT_11110.3|PUBMED:15060529)
RID: 55123 (;Known transition omitted'):
  Reactants: Nascent HDL (annotations: GO:GO:0034364)
  Products: HDL (annotations: GO:GO:0034364)
  Modifiers: None
  (References: WIKIPATHWAYS:WP5304)
RID: 55370 (PDmap:re545.0;State transition'):
  Reactants: cis,cis-dodeca-3,6-dienoyl-CoA (annotations: CHEBI:CHEBI:28002,REACTOME:REACT_3487.1)
  Products: (2-trans,6-cis)-dodeca-2,6-dienoyl-CoA (annotations: CHEBI:CHEBI:28387,REACTOME:REACT_4665.1)
  Modifiers: ECI1 (formerSymbols: DCI) (annotations: ENTREZ:1632,HGNC_SYMBOL:ECI1,UNIPROT:P42126,,HGNC:2703,REFSEQ:NM_001178029)
  (References: REACTOME:REACT_588.2)
RID: 55970 (;Positive influence'):
  Reactants: Oxysterols (annotations: CHEBI:CHEBI:53030)
  Products: NR1H4 (annotations: ,ENTREZ:9971,HGNC:7967,UNIPROT:Q96RI1,REFSEQ:NM_005123,HGNC_SYMBOL:NR1H4)
  Modifiers: None
RID: 55223 (;State transition'):
  Reactants: DMAPP (annotations: CHEBI:CHEBI:57623)
  Products: GPP (annotations: CHEBI:CHEBI:17211)
  Modifiers: GGPS1 (annotations: ENTREZ:9453,UNIPROT:O95749,HGNC:4249,HGNC_SYMBOL:GGPS1,REFSEQ:NM_004837,); FDPS (annotations: REFSEQ:NM_002004,HGNC:3631,HGNC_SYMBOL:FDPS,UNIPROT:P14324,,ENTREZ:2224)
  (References: WIKIPATHWAYS:WP4718|DOI:10.1016/B978-0-12-824048-9.00005-5)
RID: 55537 (;Positive influence'):
  Reactants: PFKFB
  Products: Glycolysis
  Modifiers: None
RID: 55561 (;Positive influence'):
  Reactants: PKLR (annotations: HGNC_SYMBOL:PKLR,REFSEQ:NM_000298,PUBMED:31284506,HGNC:9020,UNIPROT:P30613,ENTREZ:5313,)
  Products: Glycolysis
  Modifiers: None
RID: 55755 (;Positive influence'):
  Reactants: Fatty Acids
  Products: PPARG (annotations: HGNC:9236,REFSEQ:NM_005037,HGNC_SYMBOL:PPARG,UNIPROT:P37231,,ENTREZ:5468)
  Modifiers: None
RID: 56190 (;State transition'):
  Reactants: Acetaldehyde (annotations: CHEBI:CHEBI:15343)
  Products: Acetyl-CoA (annotations: CHEBI:CHEBI:15351,CHEBI:CHEBI:57288)
  Modifiers: ACSS2 (formerSymbols: ACAS2) (annotations: ENTREZ:55902,HGNC_SYMBOL:ACSS2,,REFSEQ:NM_018677,HGNC:15814,UNIPROT:Q9NR19)
RID: 55097 (;Known transition omitted'):
  Reactants: LDL (annotations: GO:GO:0034362)
  Products: LDL (annotations: GO:GO:0034362)
  Modifiers: LDLR; SORT1 (annotations: ENTREZ:6272,,REFSEQ:NM_002959,UNIPROT:Q99523,HGNC:11186,HGNC_SYMBOL:SORT1); Endocytosis (annotations: GO:GO:0006897); APOB:LDLR:LDLRAP1
  (References: KEGG_PATHWAY:map04979)
RID: 55567 (;State transition'):
  Reactants: Succinate (annotations: CHEBI:CHEBI:30031)
  Products: Fumarate (annotations: CHEBI:CHEBI:29806)
  Modifiers: SDHA (formerSymbols: SDH2) (annotations: ,REFSEQ:NM_004168,ENTREZ:6389,HGNC_SYMBOL:SDHA,UNIPROT:P31040,HGNC:10680)
RID: 55530 (;Negative influence'):
  Reactants: PKLR (annotations: HGNC_SYMBOL:PKLR,REFSEQ:NM_000298,PUBMED:31284506,HGNC:9020,UNIPROT:P30613,ENTREZ:5313,)
  Products: Glycolysis
  Modifiers: None
RID: 56106 (;State transition'):
  Reactants: 2-Phosphoglycerate (annotations: CHEBI:CHEBI:24344)
  Products: Phosphoenolpyruvate (annotations: CHEBI:CHEBI:18021,CHEBI:CHEBI:44897,CHEBI:CHEBI:58702)
  Modifiers: ENO1 (formerSymbols: ENO1L1,MPB1) (annotations: HGNC_SYMBOL:ENO1,,REFSEQ:NM_001428,UNIPROT:P06733,ENTREZ:2023,HGNC:3350)
RID: 55525 (;Positive influence'):
  Reactants: PCK1 (annotations: ,PUBMED:28416361,HGNC:8724,UNIPROT:P35558,HGNC_SYMBOL:PCK1,REFSEQ:NM_002591,ENTREZ:5105)
  Products: Gluconeogenesis
  Modifiers: None
RID: 55760 (;Positive influence'):
  Reactants: PPARA (formerSymbols: PPAR) (annotations: HGNC_SYMBOL:PPARA,ENTREZ:5465,REFSEQ:NM_001001928,,PUBMED:26451809,UNIPROT:Q07869,HGNC:9232)
  Products: APOC3 (annotations: HGNC:610,UNIPROT:P02656,ENTREZ:345,REFSEQ:NM_000040,,HGNC_SYMBOL:APOC3)
  Modifiers: None
RID: 55939 (;Known transition omitted'):
  Reactants: Threonine (annotations: CHEBI:CHEBI:16857,CHEBI:CHEBI:26986)
  Products: Glycin (annotations: CHEBI:CHEBI:55443,CHEBI:CHEBI:15428)
  Modifiers: None
RID: 55955 (;State transition'):
  Reactants: AKT1 (annotations: ENTREZ:207,HGNC:391,PUBMED:28416361,HGNC_SYMBOL:AKT1,REFSEQ:NM_005163,UNIPROT:P31749,)
  Products: AKT1 (annotations: ENTREZ:207,HGNC:391,PUBMED:28416361,HGNC_SYMBOL:AKT1,REFSEQ:NM_005163,UNIPROT:P31749,)
  Modifiers: mTORC2 (annotations: GO:GO:0031932,PUBMED:28416361)
RID: 55499 (;State transition'):
  Reactants: AKT1 (annotations: ENTREZ:207,HGNC:391,PUBMED:28416361,HGNC_SYMBOL:AKT1,REFSEQ:NM_005163,UNIPROT:P31749,)
  Products: AKT1 (annotations: ENTREZ:207,HGNC:391,PUBMED:28416361,HGNC_SYMBOL:AKT1,REFSEQ:NM_005163,UNIPROT:P31749,)
  Modifiers: mTORC2 (annotations: GO:GO:0031932,PUBMED:28416361)
RID: 55437 (PDmap:re521.0;State transition'):
  Reactants: 3-oxolauroyl-CoA (annotations: REACTOME:REACT_4368.1,CAS:78303-19-2,KEGG_COMPOUND:C05263,PUBCHEM:440604,CHEMSPIDER:389502,CHEBI:CHEBI:27868,HMDB:HMDB0003937)
  Products: decanoyl-CoA (annotations: KEGG_COMPOUND:C05274,CAS:1264-57-9,HMDB:HMDB0006404,PUBCHEM:440615,REACTOME:REACT_2539.1,CHEBI:CHEBI:28493,CHEMSPIDER:389510)
  Modifiers: trifunctional Protein
  (References: REACTOME:REACT_1749.2|PUBMED:1550553)
RID: 56199 (;Positive influence'):
  Reactants: Fructose-2,6-Bisphosphate (annotations: CHEBI:CHEBI:28602)
  Products: PFKL (annotations: HGNC:8876,UNIPROT:P17858,PUBMED:31284506,REFSEQ:NM_001002021,,ENTREZ:5211,HGNC_SYMBOL:PFKL)
  Modifiers: None
RID: 56008 (;State transition'):
  Reactants: Lactate (annotations: CHEBI:CHEBI:24996)
  Products: Pyruvate (annotations: CHEBI:CHEBI:15361)
  Modifiers: LDHA (annotations: UNIPROT:P00338,REFSEQ:NM_005566,HGNC_SYMBOL:LDHA,HGNC:6535,,ENTREZ:3939)
RID: 55914 (;Positive influence'):
  Reactants: Branched-chain amino acids catabolism
  Products: Propionyl-CoA (annotations: CHEBI:CHEBI:15539)
  Modifiers: None
RID: 55139 (;State transition'):
  Reactants: 7-Dehydrodemosterol (annotations: CHEBI:CHEBI:27910)
  Products: Desmosterol (annotations: CHEBI:CHEBI:17737)
  Modifiers: DHCR7 (formerSymbols: SLOS) (annotations: HGNC:2860,REFSEQ:NM_001360,UNIPROT:Q9UBM7,HGNC_SYMBOL:DHCR7,ENTREZ:1717,)
  (References: WIKIPATHWAYS:WP4718|DOI:10.1016/B978-0-12-824048-9.00005-5)
RID: 55838 (;Positive influence'):
  Reactants: PPARGC1A (formerSymbols: PPARGC1) (annotations: UNIPROT:Q9UBK2,ENTREZ:10891,HGNC:9237,HGNC_SYMBOL:PPARGC1A,,REFSEQ:NM_013261)
  Products: HNF4A (formerSymbols: MODY,MODY1,TCF14) (annotations: ,HGNC:5024,ENTREZ:3172,UNIPROT:P41235,HGNC_SYMBOL:HNF4A,REFSEQ:NM_000457)
  Modifiers: None
RID: 55660 (;Known transition omitted'):
  Reactants: FOXA2 (formerSymbols: HNF3B) (annotations: ENTREZ:3170,HGNC_SYMBOL:FOXA2,UNIPROT:Q9Y261,REFSEQ:NM_021784,,HGNC:5022)
  Products: FOXA2 (formerSymbols: HNF3B) (annotations: PUBMED:19595610,ENTREZ:3170,HGNC_SYMBOL:FOXA2,UNIPROT:Q9Y261,REFSEQ:NM_021784,,HGNC:5022)
  Modifiers: None
RID: 55449 (;Transport'):
  Reactants: e-
  Products: e-
  Modifiers: ubiquinone (annotations: CHEMBL_COMPOUND:CHEMBL454801,HMDB:HMDB0002012,KEGG_COMPOUND:C00399,MESH_2012:D014451,CHEMSPIDER:4307,PUBCHEM:4462,CAS:727-81-1,WIKIPEDIA:Ubiquinone,CHEBI:CHEBI:16389); ubiquinone (annotations: CHEMBL_COMPOUND:CHEMBL454801,HMDB:HMDB0002012,KEGG_COMPOUND:C00399,MESH_2012:D014451,CHEMSPIDER:4307,PUBCHEM:4462,CAS:727-81-1,WIKIPEDIA:Ubiquinone,CHEBI:CHEBI:16389)
RID: 55111 (;Transport'):
  Reactants: Fatty acyl-CoA (annotations: CHEBI:CHEBI:37554)
  Products: Mitochondrial Beta-Oxidation (annotations: GO:GO:0006635,WIKIPATHWAYS:WP143)
  Modifiers: DBI (annotations: HGNC_SYMBOL:DBI,ENTREZ:1622,,UNIPROT:P07108,PUBMED:18477307,HGNC:2690,REFSEQ:NM_020548)
RID: 55904 (;Known transition omitted'):
  Reactants: Sedoheptulose-7-Phosphate (annotations: CHEBI:CHEBI:15721); Glyceralaldehyde-3-Phosphate (annotations: CHEBI:CHEBI:17138)
  Products: Erythrose-4-Phosphate (annotations: CHEBI:CHEBI:48153); Fructose-6-Phosphate (annotations: CHEBI:CHEBI:15946,CHEBI:CHEBI:16084)
  Modifiers: TALDO1 (annotations: ,REFSEQ:NM_006755,HGNC:11559,UNIPROT:P37837,HGNC_SYMBOL:TALDO1,ENTREZ:6888)
RID: 55967 (;Transport'):
  Reactants: Pyruvate (annotations: CHEBI:CHEBI:15361)
  Products: Pyruvate (annotations: CHEBI:CHEBI:15361)
  Modifiers: MPC (annotations: PUBMED:25748677)
RID: 55907 (;Positive influence'):
  Reactants: NR3C1 (formerSymbols: GRL) (annotations: HGNC_SYMBOL:NR3C1,REFSEQ:NM_000176,,HGNC:7978,ENTREZ:2908,PUBMED:26451809,UNIPROT:P04150)
  Products: NR1I3 (annotations: ENTREZ:9970,UNIPROT:Q14994,,HGNC:7969,PUBMED:26451809,REFSEQ:NM_001077469,HGNC_SYMBOL:NR1I3)
  Modifiers: None
RID: 55172 (;State transition'):
  Reactants: Cholesterol (annotations: CHEBI:CHEBI:16113,KEGG_COMPOUND:C00187)
  Products: Cholestenone (annotations: CHEBI:CHEBI:16175)
  Modifiers: None
  (References: WIKIPATHWAYS:WP4718)
RID: 56128 (;Positive influence'):
  Reactants: FOXO1 (formerSymbols: FKHR,FOXO1A) (annotations: HGNC:3819,,REFSEQ:NM_002015,ENTREZ:2308,PUBMED:28416361,HGNC_SYMBOL:FOXO1,UNIPROT:Q12778)
  Products: Cell Survival
  Modifiers: None
RID: 55218 (;Transcription'):
  Reactants: ELOVL5 (formerSymbols: SCA38) (annotations: REFSEQ:NM_021814,UNIPROT:Q9NYP7,HGNC_SYMBOL:ELOVL5,,ENTREZ:60481,HGNC:21308)
  Products: ELOVL5 (formerSymbols: SCA38) (annotations: REFSEQ:NM_021814,UNIPROT:Q9NYP7,HGNC_SYMBOL:ELOVL5,,ENTREZ:60481,HGNC:21308)
  Modifiers: SREBF2 (annotations: HGNC:11290,REFSEQ:NM_004599,UNIPROT:Q12772,,HGNC_SYMBOL:SREBF2,ENTREZ:6721)
  (References: WIKIPATHWAYS:WP4718)
RID: 55910 (;Positive influence'):
  Reactants: PPARA (formerSymbols: PPAR) (annotations: HGNC_SYMBOL:PPARA,ENTREZ:5465,REFSEQ:NM_001001928,,PUBMED:26451809,UNIPROT:Q07869,HGNC:9232)
  Products: PLTP (annotations: REFSEQ:NM_006227,,HGNC:9093,ENTREZ:5360,UNIPROT:P55058,HGNC_SYMBOL:PLTP)
  Modifiers: None
RID: 55092 (;State transition'):
  Reactants: LysoPhosphatidic Acid
  Products: Phosphatidic Acid
  Modifiers: AGPAT
RID: 55600 (;State transition'):
  Reactants: Acetyl-CoA (annotations: CHEBI:CHEBI:15351,CHEBI:CHEBI:57288)
  Products: Acetyl-ACP (annotations: CHEBI:CHEBI:2393)
  Modifiers: ACAT2 (annotations: ENTREZ:39,HGNC:94,HGNC_SYMBOL:ACAT2,REFSEQ:NM_005891,UNIPROT:Q9BWD1,)
RID: 56102 (;Positive influence'):
  Reactants: CD36 (annotations: HGNC:1663,REFSEQ:NM_001001547,HGNC_SYMBOL:CD36,PUBMED:26451809,ENTREZ:948,,UNIPROT:P16671,PUBMED:18477307)
  Products: Fatty Acid Transport (annotations: WIKIPATHWAYS:WP5061)
  Modifiers: None
RID: 56077 (;Positive influence'):
  Reactants: ACACA (formerSymbols: ACAC,ACC) (annotations: REFSEQ:NM_198836,UNIPROT:Q13085,HGNC_SYMBOL:ACACA,ENTREZ:31,HGNC:84,)
  Products: Fatty Acid Synthesis (annotations: GO:GO:0005835)
  Modifiers: None
RID: 56007 (;Positive influence'):
  Reactants: EHHADH (formerSymbols: ECHD) (annotations: ENTREZ:1962,UNIPROT:Q08426,,HGNC:3247,HGNC_SYMBOL:EHHADH,REFSEQ:NM_001166415)
  Products: Fatty Acid Metabolism (annotations: GO:GO:0009062)
  Modifiers: None
RID: 56193 (;State transition'):
  Reactants: 6-Phosphogluconate (annotations: CHEBI:CHEBI:48928)
  Products: Fibulose-5-Phosphate
  Modifiers: PGD (annotations: UNIPROT:P52209,HGNC_SYMBOL:PGD,REFSEQ:NM_002631,,HGNC:8891,ENTREZ:5226)
  (References: WIKIPATHWAYS:WP134)
RID: 55599 (;Positive influence'):
  Reactants: PPARA (formerSymbols: PPAR) (annotations: HGNC_SYMBOL:PPARA,ENTREZ:5465,REFSEQ:NM_001001928,,PUBMED:26451809,UNIPROT:Q07869,HGNC:9232)
  Products: EHHADH (formerSymbols: ECHD) (annotations: ENTREZ:1962,UNIPROT:Q08426,,HGNC:3247,HGNC_SYMBOL:EHHADH,REFSEQ:NM_001166415)
  Modifiers: None
RID: 55482 (;Negative influence'):
  Reactants: GSK3B (annotations: HGNC_SYMBOL:GSK3B,ENTREZ:2932,PUBMED:28416361,,HGNC:4617,UNIPROT:P49841,REFSEQ:NM_001146156)
  Products: Cell Proliferation (annotations: GO:GO:0072574)
  Modifiers: None
RID: 56209 (;State transition'):
  Reactants: 2-Phosphoglycerate (annotations: CHEBI:CHEBI:24344)
  Products: Phosphoenolpyruvate (annotations: CHEBI:CHEBI:18021,CHEBI:CHEBI:44897,CHEBI:CHEBI:58702)
  Modifiers: ENO1 (formerSymbols: ENO1-IT1,ENO1L1,MPB1) (annotations: HGNC_SYMBOL:ENO1,,REFSEQ:NM_001428,UNIPROT:P06733,ENTREZ:2023,HGNC:3350)
  (References: WIKIPATHWAYS:WP534)
RID: 55999 (;Negative influence'):
  Reactants: Fructose-2,6-Bisphosphate (annotations: CHEBI:CHEBI:28602)
  Products: FBP1 (formerSymbols: FBP) (annotations: HGNC_SYMBOL:FBP1,UNIPROT:P09467,REFSEQ:NM_000507,PUBMED:31284506,HGNC:3606,ENTREZ:2203,)
  Modifiers: None
RID: 55987 (;Known transition omitted'):
  Reactants: Phosphatidic Acid
  Products: Phospholipids
  Modifiers: None
RID: 55864 (;State transition'):
  Reactants: Mannose-6-Phosphate (annotations: CHEBI:CHEBI:17369)
  Products: Fructose-6-Phosphate (annotations: CHEBI:CHEBI:15946,CHEBI:CHEBI:16084)
  Modifiers: MPI (annotations: ENTREZ:4351,HGNC:7216,,REFSEQ:NM_001289155,HGNC_SYMBOL:MPI,UNIPROT:P34949)
RID: 55484 (;Positive influence'):
  Reactants: PI3K
  Products: PI3K cascade (annotations: GO:GO:0014065)
  Modifiers: None
RID: 56072 (;Transport'):
  Reactants: Fatty acyl-CoA
  Products: Mitochondrial Beta-Oxidation (annotations: WIKIPATHWAYS:WP143)
  Modifiers: None
RID: 56160 (;State transition'):
  Reactants: Mannose (annotations: CHEBI:CHEBI:37684)
  Products: Mannose-6-Phosphate (annotations: CHEBI:CHEBI:17369)
  Modifiers: HK1 (annotations: REFSEQ:NM_000188,,HGNC_SYMBOL:HK1,UNIPROT:P19367,HGNC:4922,ENTREZ:3098)
RID: 55164 (;State transition'):
  Reactants: FF-MAS (annotations: CHEBI:CHEBI:17813)
  Products: Dihydro-FF-MAS (annotations: CHEBI:CHEBI:78904)
  Modifiers: DHCR24 (formerSymbols: DCE) (annotations: REFSEQ:NM_014762,HGNC_SYMBOL:DHCR24,,ENTREZ:1718,UNIPROT:Q15392,HGNC:2859)
  (References: WIKIPATHWAYS:WP4718|DOI:10.1016/B978-0-12-824048-9.00005-5)
RID: 55667 (;Positive influence'):
  Reactants: FOXA2 (formerSymbols: HNF3B) (annotations: PUBMED:19595610,ENTREZ:3170,HGNC_SYMBOL:FOXA2,UNIPROT:Q9Y261,REFSEQ:NM_021784,,HGNC:5022)
  Products: CPT2 (formerSymbols: CPT1) (annotations: HGNC_SYMBOL:CPT2,PUBMED:19595610,HGNC:2330,REFSEQ:NM_000098,UNIPROT:P23786,,ENTREZ:1376)
  Modifiers: None
RID: 56165 (;State transition'):
  Reactants: Glycerol-3-Phosphate (annotations: CHEBI:CHEBI:15978)
  Products: Dihydroxyacetone-Phosphate (annotations: CHEBI:CHEBI:16108)
  Modifiers: GPD2 (annotations: ENTREZ:2820,HGNC:4456,REFSEQ:NM_000408,,UNIPROT:P43304,HGNC_SYMBOL:GPD2)
RID: 55779 (;Positive influence'):
  Reactants: ACC
  Products: Lipogenesis (annotations: GO:GO:0008610)
  Modifiers: None
RID: 55130 (;Known transition omitted'):
  Reactants: IDL (annotations: GO:GO:0034363)
  Products: LDL (annotations: GO:GO:0034362)
  Modifiers: None
  (References: WIKIPATHWAYS:WP5304)
RID: 55154 (;Known transition omitted'):
  Reactants: FADS1 (formerSymbols: LLCDL1) (annotations: HGNC:3574,,HGNC_SYMBOL:FADS1,UNIPROT:O60427,ENTREZ:3992,REFSEQ:NM_013402)
  Products: Fatty Acid Biosynthesis (annotations: WIKIPATHWAYS:WP4491,GO:GO:0006633)
  Modifiers: None
RID: 55718 (;State transition'):
  Reactants: GYS
  Products: GYS
  Modifiers: None
RID: 55554 (;State transition'):
  Reactants: FBP1 (formerSymbols: FBP) (annotations: HGNC_SYMBOL:FBP1,UNIPROT:P09467,REFSEQ:NM_000507,PUBMED:31284506,HGNC:3606,ENTREZ:2203,)
  Products: FBP1 (formerSymbols: FBP) (annotations: HGNC_SYMBOL:FBP1,UNIPROT:P09467,REFSEQ:NM_000507,PUBMED:31284506,HGNC:3606,ENTREZ:2203,)
  Modifiers: None
RID: 55690 (;Known transition omitted'):
  Reactants: NR1H3 (annotations: REFSEQ:NM_001130101,,HGNC:7966,ENTREZ:10062,UNIPROT:Q13133,HGNC_SYMBOL:NR1H3)
  Products: NR1H3 (annotations: REFSEQ:NM_001130101,,HGNC:7966,ENTREZ:10062,UNIPROT:Q13133,HGNC_SYMBOL:NR1H3)
  Modifiers: None
RID: 55681 (;Positive influence'):
  Reactants: PKA
  Products: Phosphorylase kinase (PHK)
  Modifiers: None
RID: 55160 (;State transition'):
  Reactants: Cholestadienol (annotations: CHEBI:CHEBI:145214)
  Products: Lathosterol (annotations: CHEBI:CHEBI:17168)
  Modifiers: DHCR24 (formerSymbols: DCE) (annotations: REFSEQ:NM_014762,HGNC_SYMBOL:DHCR24,,ENTREZ:1718,UNIPROT:Q15392,HGNC:2859)
  (References: DOI:10.1016/B978-0-12-824048-9.00005-5)
RID: 55523 (;State transition'):
  Reactants: cAMP
  Products: 5' AMP
  Modifiers: PDE (annotations: )
RID: 55771 (;Positive influence'):
  Reactants: Fructose-2,6-Bisphosphate (annotations: CHEBI:CHEBI:28602)
  Products: PFKL (annotations: HGNC:8876,UNIPROT:P17858,PUBMED:31284506,REFSEQ:NM_001002021,,ENTREZ:5211,HGNC_SYMBOL:PFKL)
  Modifiers: None
RID: 55590 (;Transport'):
  Reactants: Long-chain Fatty Acids
  Products: Long-chain Fatty Acids
  Modifiers: Diffusion (annotations: PUBMED:18477307)
  (References: PUBMED:18477307)
RID: 55283 (PDmap:re616.0;State transition'):
  Reactants: prostaglandin H2 (annotations: CHEBI:CHEBI:15554,WIKIPEDIA:Prostaglandin H2,PUBCHEM:445049,KEGG_COMPOUND:C00427,CAS:42935-17-1,CHEMSPIDER:392800,HMDB:HMDB0001381)
  Products: prostaglandin D2 (annotations: CHEBI:CHEBI:15555,KEGG_COMPOUND:C00696,CHEMSPIDER:395250,PUBCHEM:448457,HMDB:HMDB0001403,CAS:41598-07-6,WIKIPEDIA:Prostaglandin D2)
  Modifiers: PTGDS (annotations: HGNC_SYMBOL:PTGDS,REFSEQ:NM_000954,ENTREZ:5730,HGNC:9592,UNIPROT:P41222,)
  (References: PUBMED:11729303)
RID: 56154 (;State transition'):
  Reactants: PKLR (annotations: HGNC_SYMBOL:PKLR,REFSEQ:NM_000298,HGNC:9020,UNIPROT:P30613,ENTREZ:5313,)
  Products: PKLR (annotations: HGNC_SYMBOL:PKLR,REFSEQ:NM_000298,PUBMED:31284506,HGNC:9020,UNIPROT:P30613,ENTREZ:5313,)
  Modifiers: None
RID: 55534 (;State transition'):
  Reactants: ATP
  Products: cAMP
  Modifiers: ADCY
RID: 55846 (;Positive influence'):
  Reactants: NR1I3 (annotations: ENTREZ:9970,UNIPROT:Q14994,,HGNC:7969,REFSEQ:NM_001077469,HGNC_SYMBOL:NR1I3)
  Products: EHHADH (formerSymbols: ECHD) (annotations: ENTREZ:1962,UNIPROT:Q08426,,HGNC:3247,HGNC_SYMBOL:EHHADH,REFSEQ:NM_001166415)
  Modifiers: None
RID: 56065 (;Positive influence'):
  Reactants: PPARA (formerSymbols: PPAR) (annotations: HGNC_SYMBOL:PPARA,ENTREZ:5465,REFSEQ:NM_001001928,,PUBMED:26451809,UNIPROT:Q07869,HGNC:9232)
  Products: DBI (annotations: HGNC_SYMBOL:DBI,ENTREZ:1622,,UNIPROT:P07108,HGNC:2690,REFSEQ:NM_020548)
  Modifiers: None
RID: 56062 (;State transition'):
  Reactants: Butyrate (annotations: CHEBI:CHEBI:17968)
  Products: Butanoyl-CoA (annotations: CHEBI:CHEBI:22954)
  Modifiers: ACSM3 (formerSymbols: SAH) (annotations: REFSEQ:NM_005622,,HGNC:10522,ENTREZ:6296,HGNC_SYMBOL:ACSM3,UNIPROT:Q53FZ2)
RID: 55314 (;State transition'):
  Reactants: palmitoyl-CoA (annotations: REACTOME:REACT_11391.1,CHEMSPIDER:14902,PUBCHEM:15667,HMDB:HMDB0001338,KEGG_COMPOUND:C00154,CHEBI:CHEBI:15525,WIKIPEDIA:palmitoyl CoA,CAS:1763-10-6)
  Products: palmitate (annotations: HMDB:HMDB0000220,PUBCHEM:985,KEGG_COMPOUND:C00249,WIKIPEDIA:Palmitic acid,CHEBI:CHEBI:7896,CAS:57-10-3,CHEMBL_COMPOUND:CHEMBL82293,CHEMSPIDER:960,CHEBI:CHEBI:15756,REACTOME:REACT_3374.1)
  Modifiers: FASN (annotations: HGNC:3594,UNIPROT:P49327,REFSEQ:NM_004104,,ENTREZ:2194,HGNC_SYMBOL:FASN)
  (References: WIKIPATHWAYS:WP357)
RID: 55544 (;State transition'):
  Reactants: PFKL (annotations: HGNC:8876,UNIPROT:P17858,PUBMED:31284506,REFSEQ:NM_001002021,,ENTREZ:5211,HGNC_SYMBOL:PFKL)
  Products: PFKL (annotations: HGNC:8876,UNIPROT:P17858,PUBMED:31284506,REFSEQ:NM_001002021,,ENTREZ:5211,HGNC_SYMBOL:PFKL)
  Modifiers: None
RID: 55719 (;State transition'):
  Reactants: NR1H3 (annotations: REFSEQ:NM_001130101,,HGNC:7966,ENTREZ:10062,UNIPROT:Q13133,HGNC_SYMBOL:NR1H3)
  Products: NR1H3 (annotations: REFSEQ:NM_001130101,,HGNC:7966,ENTREZ:10062,UNIPROT:Q13133,HGNC_SYMBOL:NR1H3)
  Modifiers: None
RID: 56030 (;State transition'):
  Reactants: 2,3-Bisphosphoglycerate (annotations: CHEBI:CHEBI:19324)
  Products: 3-Phosphoglycerate (annotations: CHEBI:CHEBI:17050,CHEBI:CHEBI:17794,CHEBI:CHEBI:57998)
  Modifiers: None
RID: 55759 (;Known transition omitted'):
  Reactants: Trans,cis-Lauro-2,6-dienoyl-CoA (annotations: CHEBI:CHEBI:28387)
  Products: 4-cis-decenoyl-CoA; Acetyl-CoA (annotations: CHEBI:CHEBI:15351,CHEBI:CHEBI:57288)
  Modifiers: Mitochondrial trifunctional enzyme; ACADL (annotations: ,REFSEQ:NM_001608,HGNC_SYMBOL:ACADL,HGNC:88,ENTREZ:33,UNIPROT:P28330)
RID: 56183 (;State transition'):
  Reactants: Glucose-6-Phosphate (annotations: CHEBI:CHEBI:14314)
  Products: Glucose (annotations: CHEBI:CHEBI:17234)
  Modifiers: G6PC (annotations: PUBMED:28416361,)
RID: 55963 (;State transition'):
  Reactants: Fructose-6-Phosphate (annotations: CHEBI:CHEBI:15946,CHEBI:CHEBI:16084)
  Products: Fructose-2,6-Bisphosphate (annotations: CHEBI:CHEBI:28602)
  Modifiers: PFKFB1 (formerSymbols: PFRX) (annotations: ENTREZ:5207,REFSEQ:NM_001271804,UNIPROT:P16118,HGNC:8872,HGNC_SYMBOL:PFKFB1,)
RID: 55131 (;Heterodimer association'):
  Reactants: Long-chain Fatty Acids (annotations: CHEBI:CHEBI:15904); CD36 (annotations: HGNC:1663,REFSEQ:NM_001001547,HGNC_SYMBOL:CD36,,ENTREZ:948,UNIPROT:P16671,PUBMED:18477307)
  Products: CD36:LCFA
  Modifiers: None
  (References: PUBMED:12856180)
RID: 55313 (;State transition'):
  Reactants: O2 (annotations: CHEBI:CHEBI:15379,KEGG_COMPOUND:C00007,HMDB:HMDB0001377,PUBCHEM:977,CHEMSPIDER:952,CAS:7782-44-7,WIKIPEDIA:Oxygen)
  Products: superoxide (annotations: HMDB:HMDB0002168,WIKIPEDIA:Superoxide,PUBCHEM:5359597,CHEMSPIDER:4514331,KEGG_COMPOUND:C00704,CHEBI:CHEBI:18421,CAS:11062-77-4)
  Modifiers: complex III (annotations: GO:GO:0045275)
  (References: PUBMED:19427899|PUBMED:15262965)
RID: 56093 (;State transition'):
  Reactants: UDP-Galactose (annotations: CHEBI:CHEBI:67119)
  Products: UDP-Glucose (annotations: CHEBI:CHEBI:18066)
  Modifiers: GALE (annotations: HGNC_SYMBOL:GALE,UNIPROT:Q14376,HGNC:4116,ENTREZ:2582,REFSEQ:NM_000403,)
RID: 56130 (;State transition'):
  Reactants: PYGL
  Products: PYGL
  Modifiers: None
RID: 55736 (;Known transition omitted'):
  Reactants: MLXIPL (formerSymbols: WBSCR14) (annotations: ,HGNC:12744,HGNC_SYMBOL:MLXIPL,REFSEQ:NM_032951,ENTREZ:51085,UNIPROT:Q9NP71)
  Products: ChREBP (annotations: PUBMED:26451809)
  Modifiers: None
RID: 55732 (;Known transition omitted'):
  Reactants: Trans-Hexadec-2-enoyl-CoA (annotations: CHEBI:CHEBI:28935)
  Products: Myristoyl-CoA (annotations: CHEBI:CHEBI:15532); Acetyl-CoA (annotations: CHEBI:CHEBI:15351,CHEBI:CHEBI:57288)
  Modifiers: Mitochondrial trifunctional enzyme
RID: 55277 (PDmap:re522.0;State transition'):
  Reactants: decanoyl-CoA (annotations: KEGG_COMPOUND:C05274,CAS:1264-57-9,HMDB:HMDB0006404,PUBCHEM:440615,REACTOME:REACT_2539.1,CHEBI:CHEBI:28493,CHEMSPIDER:389510)
  Products: trans-dec-2-enoyl-CoA (annotations: CHEMSPIDER:4444334,CHEBI:CHEBI:10723,KEGG_COMPOUND:C05275,CAS:10018-95-8,REACTOME:REACT_3903.1,PUBCHEM:5280768,HMDB:HMDB0003948)
  Modifiers: ACADM (annotations: UNIPROT:P11310,HGNC_SYMBOL:ACADM,,HGNC:89,REFSEQ:NM_000016,ENTREZ:34)
  (References: REACTOME:REACT_1862.2|PUBMED:13295225|PUBMED:3597357)
RID: 55267 (;State transition'):
  Reactants: superoxide (annotations: HMDB:HMDB0002168,WIKIPEDIA:Superoxide,PUBCHEM:5359597,CHEMSPIDER:4514331,KEGG_COMPOUND:C00704,CHEBI:CHEBI:18421,CAS:11062-77-4); NO (annotations: HMDB:HMDB0003378,CAS:10102-43-9,WIKIPEDIA:Nitric oxide,KEGG_COMPOUND:C00533,CHEBI:CHEBI:16480,PUBCHEM:145068,MESH_2012:D009569,CHEMSPIDER:127983,CHEMBL_COMPOUND:CHEMBL1200689)
  Products: peroxynitrite (annotations: CHEBI:CHEBI:25941)
  Modifiers: None
  (References: REACTOME:REACT_264249)
RID: 55679 (;State transition'):
  Reactants: PIP2 (annotations: CHEBI:CHEBI:37328)
  Products: PIP3 (annotations: CHEBI:CHEBI:60169)
  Modifiers: PI3K (annotations: REFSEQ:NM_000188,,HGNC_SYMBOL:HK1,UNIPROT:P19367,HGNC:4922,ENTREZ:3098)
RID: 56092 (;State transition'):
  Reactants: Fumarate (annotations: CHEBI:CHEBI:29806)
  Products: Malate (annotations: CHEBI:CHEBI:15595,CHEBI:CHEBI:30797)
  Modifiers: FH (annotations: REFSEQ:NM_000143,,HGNC_SYMBOL:FH,ENTREZ:2271,HGNC:3700,UNIPROT:P07954)
RID: 55257 (;State transition'):
  Reactants: P4HB (formerSymbols: ERBA2L,PO4DB) (annotations: REFSEQ:NM_000918,HGNC_SYMBOL:P4HB,HGNC:8548,,UNIPROT:P07237,ENTREZ:5034); hydrogen peroxide (annotations: PUBCHEM:784,HMDB:HMDB0003125,KEGG_COMPOUND:C00027,MESH_2012:D006861,CHEBI:CHEBI:16240,WIKIPEDIA:Hydrogen peroxide,CAS:7722-84-1,CHEMBL_COMPOUND:CHEMBL71595,CHEMSPIDER:763)
  Products: P4HB (formerSymbols: ERBA2L,PO4DB) (annotations: REFSEQ:NM_000918,HGNC_SYMBOL:P4HB,HGNC:8548,,UNIPROT:P07237,ENTREZ:5034); H2O (annotations: HMDB:HMDB0002111,CHEBI:CHEBI:15377,PUBCHEM:962,CHEMSPIDER:937,MESH_2012:D014867,WIKIPEDIA:Water,CAS:7732-18-5,CHEMBL_COMPOUND:CHEMBL1098659,KEGG_COMPOUND:C00001)
  Modifiers: ERO1A:GPX7:GPX8
  (References: REACTOME:REACT_264249)
RID: 56207 (;State transition'):
  Reactants: PFKL (annotations: HGNC:8876,UNIPROT:P17858,PUBMED:31284506,REFSEQ:NM_001002021,,ENTREZ:5211,HGNC_SYMBOL:PFKL)
  Products: PFKL (annotations: HGNC:8876,UNIPROT:P17858,PUBMED:31284506,REFSEQ:NM_001002021,,ENTREZ:5211,HGNC_SYMBOL:PFKL)
  Modifiers: None
RID: 55784 (;Positive influence'):
  Reactants: GCK (formerSymbols: MODY2) (annotations: ,ENTREZ:2645,HGNC_SYMBOL:GCK,PUBMED:28416361,REFSEQ:NM_000162,UNIPROT:P35557,HGNC:4195)
  Products: Glycolysis (annotations: GO:GO:0061621)
  Modifiers: None
RID: 56023 (;State transition'):
  Reactants: 3-keto-very long FA-CoA
  Products: not so very long FA-CoA; Acetyl-CoA (annotations: CHEBI:CHEBI:15351)
  Modifiers: ACAA1 (annotations: HGNC_SYMBOL:ACAA1,,REFSEQ:NM_001607,HGNC:82,ENTREZ:30,UNIPROT:P09110); SCP2 (annotations: HGNC_SYMBOL:SCP2,ENTREZ:6342,REFSEQ:NM_002979,,UNIPROT:P22307,HGNC:10606)
RID: 56196 (;State transition'):
  Reactants: GYS
  Products: GYS
  Modifiers: GSK3B (annotations: HGNC_SYMBOL:GSK3B,ENTREZ:2932,PUBMED:28416361,,HGNC:4617,UNIPROT:P49841,REFSEQ:NM_001146156)
RID: 55878 (;State transition'):
  Reactants: Lathosterol (annotations: CHEBI:CHEBI:17168)
  Products: 7-Dehydrocholesterol (annotations: CHEBI:CHEBI:17759)
  Modifiers: SC5D (formerSymbols: SC5DL) (annotations: ENTREZ:6309,HGNC:10547,HGNC_SYMBOL:SC5D,REFSEQ:NM_001024956,,UNIPROT:O75845)
  (References: DOI:10.1016/B978-0-12-824048-9.00005-5)
RID: 55935 (;State transition'):
  Reactants: FOXO1 (formerSymbols: FKHR,FOXO1A) (annotations: HGNC:3819,,REFSEQ:NM_002015,ENTREZ:2308,PUBMED:28416361,HGNC_SYMBOL:FOXO1,UNIPROT:Q12778)
  Products: FOXO1 (formerSymbols: FKHR,FOXO1A) (annotations: HGNC:3819,,REFSEQ:NM_002015,ENTREZ:2308,PUBMED:28416361,HGNC_SYMBOL:FOXO1,UNIPROT:Q12778)
  Modifiers: AKT1 (annotations: ENTREZ:207,HGNC:391,PUBMED:28416361,HGNC_SYMBOL:AKT1,REFSEQ:NM_005163,UNIPROT:P31749,)
RID: 55689 (;State transition'):
  Reactants: HMG-CoA (annotations: CHEBI:CHEBI:11814)
  Products: Mevalonic acid (annotations: CHEBI:CHEBI:25351)
  Modifiers: HMGCR (annotations: ,REFSEQ:NM_000859,UNIPROT:P04035,HGNC:5006,ENTREZ:3156,HGNC_SYMBOL:HMGCR)
  (References: DOI:10.1016/B978-0-12-824048-9.00005-5)
RID: 55309 (;State transition'):
  Reactants:  ; NDUFB9 (annotations: ENTREZ:4715,REFSEQ:NM_005005,,HGNC:7704,HGNC_SYMBOL:NDUFB9,UNIPROT:Q9Y6M9); NDUFA1 (annotations: REFSEQ:NM_004541,,UNIPROT:O15239,HGNC_SYMBOL:NDUFA1,ENTREZ:4694,HGNC:7683); mtDNA encoded OXPHOS units (annotations: PUBMED:23149385,PUBMED:30030361)
  Products: complex I (annotations: GO:GO:0005747)
  Modifiers: OXPHOS factors (annotations: PUBMED:23149385,PUBMED:30030361)
  (References: PUBMED:23149385|TAXONOMY:10090|PUBMED:30030361)
RID: 55184 (;Translation'):
  Reactants: ACAT2 (annotations: ENTREZ:39,HGNC:94,HGNC_SYMBOL:ACAT2,REFSEQ:NM_005891,UNIPROT:Q9BWD1,)
  Products: ACAT2 (annotations: ENTREZ:39,HGNC:94,HGNC_SYMBOL:ACAT2,REFSEQ:NM_005891,UNIPROT:Q9BWD1,)
  Modifiers: None
RID: 55842 (;Positive influence'):
  Reactants: PLTP (annotations: REFSEQ:NM_006227,,HGNC:9093,ENTREZ:5360,UNIPROT:P55058,HGNC_SYMBOL:PLTP)
  Products: Apolipoprotein Metabolism
  Modifiers: None
RID: 55975 (;State transition'):
  Reactants: PKLR (annotations: HGNC_SYMBOL:PKLR,REFSEQ:NM_000298,PUBMED:31284506,HGNC:9020,UNIPROT:P30613,ENTREZ:5313,)
  Products: PKLR (annotations: HGNC_SYMBOL:PKLR,REFSEQ:NM_000298,HGNC:9020,UNIPROT:P30613,ENTREZ:5313,)
  Modifiers: PKA
RID: 55374 (;State transition'):
  Reactants: acetyl-CoA (annotations: CHEBI:CHEBI:15351,WIKIPEDIA:Acetyl-CoA,HMDB:HMDB0001206,CHEMSPIDER:392413,PUBCHEM:444493,REACTOME:REACT_3839.1,CAS:72-89-9,KEGG_COMPOUND:C00024); H2O (annotations: HMDB:HMDB0002111,CHEBI:CHEBI:15377,PUBCHEM:962,CHEMSPIDER:937,MESH_2012:D014867,WIKIPEDIA:Water,CAS:7732-18-5,CHEMBL_COMPOUND:CHEMBL1098659,KEGG_COMPOUND:C00001); oxaloacetate(2-) (annotations: PUBCHEM:970,CHEBI:CHEBI:30744,KEGG_COMPOUND:C00036,CAS:328-42-7,HMDB:HMDB0000223,CHEMSPIDER:945,REACTOME:REACT_5376.1,CHEBI:CHEBI:16452,WIKIPEDIA:Oxalacetic acid)
  Products: citrate(3-) (annotations: KEGG_COMPOUND:C00158,PUBCHEM:311,CHEBI:CHEBI:30769,CHEBI:CHEBI:16947,WIKIPEDIA:Citric acid,REACTOME:REACT_2769.1,CHEMBL_COMPOUND:CHEMBL1261,CHEMSPIDER:305,HMDB:HMDB0000094,CAS:77-92-9); coenzyme A (annotations: CHEBI:CHEBI:15346,REACTOME:REACT_3654.2)
  Modifiers: CS (annotations: HGNC_SYMBOL:CS,HGNC:2422,REFSEQ:NM_004077,,UNIPROT:O75390,ENTREZ:1431)
  (References: PUBMED:9809442|PUBMED:9792662|REACTOME:REACT_1282.5)
RID: 56104 (;Known transition omitted'):
  Reactants: Trans-Tetradec-2-enoyl-CoA (annotations: CHEBI:CHEBI:27721)
  Products: Lauroyl-CoA (annotations: CHEBI:CHEBI:15521); Acetyl-CoA (annotations: CHEBI:CHEBI:15351,CHEBI:CHEBI:57288)
  Modifiers: Mitochondrial trifunctional enzyme
RID: 55862 (;State transition'):
  Reactants: Acetoacetate (annotations: CHEBI:CHEBI:13705)
  Products: Acetone (annotations: CHEBI:CHEBI:15347)
  Modifiers: None
RID: 55335 (PDmap:re52.0;State transition'):
  Reactants: pyruvate dehydrogenase complex (annotations: REACTOME:REACT_5500.1,GO:GO:0005967); ATP (annotations: CHEBI:CHEBI:15422,PUBCHEM:5957,CAS:56-65-5,MESH_2012:D000255,CHEMBL_COMPOUND:CHEMBL14249,CHEMSPIDER:5742,WIKIPEDIA:Adenosine triphosphate,HMDB:HMDB0000538,KEGG_COMPOUND:C00002)
  Products: pyruvate dehydrogenase complex (annotations: REACTOME:REACT_5500.1,GO:GO:0005967); ADP (annotations: HMDB:HMDB0001341,WIKIPEDIA:ADP,CAS:58-64-0,KEGG_COMPOUND:C00008,PUBCHEM:6022,CHEBI:CHEBI:16761,CHEMBL_COMPOUND:CHEMBL14830,CHEMSPIDER:5800)
  Modifiers: pyruvate (annotations: REACTOME:REACT_3219.1,CHEBI:CHEBI:15361); NADH (annotations: REACTOME:REACT_2390.1,KEGG_COMPOUND:C00004,HMDB:HMDB0001487,CHEMSPIDER:903,WIKIPEDIA:NADH,CAS:58-68-4,CHEBI:CHEBI:16908,PUBCHEM:928,CHEMBL_COMPOUND:CHEMBL1628272,MESH_2012:D009243); acetyl-CoA (annotations: CHEBI:CHEBI:15351,WIKIPEDIA:Acetyl-CoA,HMDB:HMDB0001206,CHEMSPIDER:392413,PUBCHEM:444493,REACTOME:REACT_3839.1,CAS:72-89-9,KEGG_COMPOUND:C00024); PDK isoforms
  (References: PUBMED:12676647|PUBMED:9405293|PUBMED:11485553|PUBMED:8798399|PUBMED:11486000|PUBMED:15491150|PUBMED:7499431|REACTOME:REACT_12462.2)
RID: 55632 (;Positive influence'):
  Reactants: NR1I2 (annotations: ,HGNC_SYMBOL:NR1I2,HGNC:7968,REFSEQ:NM_003889,ENTREZ:8856,UNIPROT:O75469)
  Products: SCD (formerSymbols: SCDOS) (annotations: ,ENTREZ:6319,HGNC_SYMBOL:SCD,UNIPROT:O00767,HGNC:10571,REFSEQ:NM_005063,PUBMED:26451809)
  Modifiers: None
RID: 55503 (;State transition'):
  Reactants: mTORC1 (annotations: GO:GO:0031931)
  Products: mTORC1 (annotations: GO:GO:0031931)
  Modifiers: None
RID: 56025 (;State transition'):
  Reactants: ADCY
  Products: ADCY
  Modifiers: Gα
  (References: PUBMED:24692138)
RID: 55619 (;State transition'):
  Reactants: Palmitate
  Products: Palmitoyl-CoA (annotations: CHEBI:CHEBI:15525)
  Modifiers: ACSL1 (formerSymbols: FACL2) (annotations: ENTREZ:2180,HGNC:3569,REFSEQ:NM_001995,UNIPROT:P33121,PUBMED:18477307,HGNC_SYMBOL:ACSL1,)
RID: 55447 (PDmap:re524.0;State transition'):
  Reactants: (S)-3-hydroxydecanoyl-CoA (annotations: CHEBI:CHEBI:28325,CHEMSPIDER:17220838,REACTOME:REACT_3098.1,PUBCHEM:16061159,CAS:6245-70-1,KEGG_COMPOUND:C05264,HMDB:HMDB0003938)
  Products: 3-oxodecanoyl-CoA (annotations: CAS:50411-91-1,KEGG_COMPOUND:C05265,PUBCHEM:440606,REACTOME:REACT_5482.1,CHEBI:CHEBI:28528,HMDB:HMDB0003939,CHEMSPIDER:389504)
  Modifiers: HADH (formerSymbols: HADHSC) (annotations: HGNC_SYMBOL:HADH,REFSEQ:NM_005327,,HGNC:4799,ENTREZ:3033,UNIPROT:Q16836)
  (References: PUBMED:8687463|REACTOME:REACT_2187.2)
RID: 55710 (;Transport'):
  Reactants: Mitochondrial Beta-Oxidation (annotations: WIKIPATHWAYS:WP143)
  Products: Linoleoyl-CoA (annotations: CHEBI:CHEBI:15530)
  Modifiers: None
RID: 56184 (;State transition'):
  Reactants: Glyceralaldehyde-3-Phosphate (annotations: CHEBI:CHEBI:17138)
  Products: Dihydroxyacetone-Phosphate (annotations: CHEBI:CHEBI:16108)
  Modifiers: TPI1 (annotations: HGNC_SYMBOL:TPI1,REFSEQ:NM_000365,HGNC:12009,ENTREZ:7167,UNIPROT:P60174,)
  (References: WIKIPATHWAYS:WP534)
RID: 55384 (;State transition'):
  Reactants: mt DNA (annotations: GO:GO:0000262)
  Products: damaged mt DNA
  Modifiers: mt DNA damage
  (References: PUBMED:23149385)
RID: 55356 (PDmap:re548.0;State transition'):
  Reactants: acetyl-CoA (annotations: CHEBI:CHEBI:15351,WIKIPEDIA:Acetyl-CoA,HMDB:HMDB0001206,CHEMSPIDER:392413,PUBCHEM:444493,REACTOME:REACT_3839.1,CAS:72-89-9,KEGG_COMPOUND:C00024); hydrogencarbonate (annotations: CHEMBL_COMPOUND:CHEMBL363707,CAS:71-52-3,HMDB:HMDB0000595,REACTOME:REACT_4357.1,CHEMSPIDER:749,PUBCHEM:769,WIKIPEDIA:Bicarbonate,CHEBI:CHEBI:17544,KEGG_COMPOUND:C00288)
  Products: malonyl-CoA (annotations: REACTOME:REACT_3059.1,WIKIPEDIA:Malonyl-CoA,HMDB:HMDB0001175,CAS:524-14-1,CHEBI:CHEBI:15531,PUBCHEM:10663,KEGG_COMPOUND:C00083,CHEMSPIDER:10213)
  Modifiers: ACACA (formerSymbols: ACAC,ACC) (annotations: REFSEQ:NM_198836,UNIPROT:Q13085,HGNC_SYMBOL:ACACA,ENTREZ:31,HGNC:84,)
  (References: PUBMED:18455495|PUBMED:7732023|PUBMED:16854592|REACTOME:REACT_11201.2)
RID: 55434 (PDmap:re586.0;State transition'):
  Reactants: ACADL (annotations: REFSEQ:NM_001608,,HGNC_SYMBOL:ACADL,HGNC:88,ENTREZ:33,UNIPROT:P28330)
  Products: ACADL (annotations: REFSEQ:NM_001608,,HGNC_SYMBOL:ACADL,HGNC:88,ENTREZ:33,UNIPROT:P28330)
  Modifiers: SIRT3 (annotations: ENTREZ:23410,HGNC_SYMBOL:SIRT3,UNIPROT:Q9NTG7,HGNC:14931,REFSEQ:NM_001017524,)
  (References: PUBMED:20203611|PUBMED:21658599)
RID: 56090 (;State transition'):
  Reactants: Acetyl-CoA (annotations: CHEBI:CHEBI:15351,CHEBI:CHEBI:57288)
  Products: Acetoacetyl-CoA (annotations: CHEBI:CHEBI:15345,CHEBI:CHEBI:57286)
  Modifiers: ACAT
RID: 55764 (;Positive influence'):
  Reactants: AHR (annotations: HGNC:348,HGNC_SYMBOL:AHR,,UNIPROT:P35869,REFSEQ:NM_001621,ENTREZ:196)
  Products: NFE2L2 (annotations: UNIPROT:Q16236,,ENTREZ:4780,REFSEQ:NM_006164,HGNC:7782,HGNC_SYMBOL:NFE2L2)
  Modifiers: None
RID: 55706 (;Positive influence'):
  Reactants: RXRA (annotations: UNIPROT:P19793,,HGNC:10477,REFSEQ:NM_002957,ENTREZ:6256,HGNC_SYMBOL:RXRA)
  Products: NR1H3 (annotations: REFSEQ:NM_001130101,,HGNC:7966,ENTREZ:10062,UNIPROT:Q13133,HGNC_SYMBOL:NR1H3)
  Modifiers: None
RID: 55376 (PDmap:re577.0;State transition'):
  Reactants: hydrogen peroxide (annotations: PUBCHEM:784,HMDB:HMDB0003125,KEGG_COMPOUND:C00027,MESH_2012:D006861,CHEBI:CHEBI:16240,WIKIPEDIA:Hydrogen peroxide,CAS:7722-84-1,CHEMBL_COMPOUND:CHEMBL71595,CHEMSPIDER:763)
  Products: H2O (annotations: HMDB:HMDB0002111,CHEBI:CHEBI:15377,PUBCHEM:962,CHEMSPIDER:937,MESH_2012:D014867,WIKIPEDIA:Water,CAS:7732-18-5,CHEMBL_COMPOUND:CHEMBL1098659,KEGG_COMPOUND:C00001); O2 (annotations: CHEBI:CHEBI:15379,KEGG_COMPOUND:C00007,HMDB:HMDB0001377,PUBCHEM:977,CHEMSPIDER:952,CAS:7782-44-7,WIKIPEDIA:Oxygen)
  Modifiers: CAT (annotations: REFSEQ:NM_001752,ENTREZ:847,,HGNC_SYMBOL:CAT,HGNC:1516,UNIPROT:P04040)
  (References: PUBMED:19427899|REACTOME:REACT_264249)
RID: 55665 (;Positive influence'):
  Reactants: RXRA (annotations: UNIPROT:P19793,,HGNC:10477,REFSEQ:NM_002957,ENTREZ:6256,HGNC_SYMBOL:RXRA)
  Products: PPARA (formerSymbols: PPAR) (annotations: HGNC_SYMBOL:PPARA,ENTREZ:5465,REFSEQ:NM_001001928,,PUBMED:26451809,UNIPROT:Q07869,HGNC:9232)
  Modifiers: None
RID: 55658 (;State transition'):
  Reactants: Zymostenol (annotations: CHEBI:CHEBI:16608)
  Products: Lathosterol (annotations: CHEBI:CHEBI:17168)
  Modifiers: EBP (formerSymbols: CDPX2) (annotations: ENTREZ:10682,REFSEQ:NM_006579,HGNC:3133,UNIPROT:Q15125,HGNC_SYMBOL:EBP,)
  (References: DOI:10.1016/B978-0-12-824048-9.00005-5)
RID: 56027 (;Known transition omitted'):
  Reactants: (2E)-very long FA-CoA (annotations: CHEBI:CHEBI:143004)
  Products: 3-keto-very long FA-CoA
  Modifiers: HSD17B4 (annotations: UNIPROT:P51659,HGNC:5213,ENTREZ:3295,HGNC_SYMBOL:HSD17B4,REFSEQ:NM_000414,)
RID: 55302 (PDmap:re54.0;State transition'):
  Reactants: isocitric acid (annotations: CHEBI:CHEBI:30887,KEGG_COMPOUND:C00311,CHEMBL_COMPOUND:CHEMBL539669,CHEMSPIDER:1161,WIKIPEDIA:Isocitric acid,CAS:320-77-4,PUBCHEM:1198,HMDB:HMDB0000193); NAD(+) (annotations: KEGG_COMPOUND:C00003,CAS:53-84-9,PUBCHEM:5893,CHEMSPIDER:5682,REACTOME:REACT_4970.1,CHEBI:CHEBI:15846,HMDB:HMDB0000902,WIKIPEDIA:NAD)
  Products: 2-oxoglutaric acid (annotations: KEGG_COMPOUND:C00026,REACTOME:REACT_3871.1,CHEBI:CHEBI:30915,CAS:328-50-7,MESH_2012:C029743,PUBCHEM:51,CHEMSPIDER:50,HMDB:HMDB0000208,WIKIPEDIA:Alpha-Ketoglutaric_acid); NADH (annotations: REACTOME:REACT_2390.1,KEGG_COMPOUND:C00004,HMDB:HMDB0001487,CHEMSPIDER:903,WIKIPEDIA:NADH,CAS:58-68-4,CHEBI:CHEBI:16908,PUBCHEM:928,CHEMBL_COMPOUND:CHEMBL1628272,MESH_2012:D009243); CO2 (annotations: CHEMSPIDER:274,CHEBI:CHEBI:16526,MESH_2012:D002245,CHEMBL_COMPOUND:CHEMBL1231871,PUBCHEM:280,WIKIPEDIA:Carbon Dioxide,HMDB:HMDB0001967,KEGG_COMPOUND:C00011,CAS:124-38-9); H+ (annotations: CHEBI:CHEBI:15378)
  Modifiers: isocitrate dehydrogenase 3 (annotations: GO:GO:0005962); Ca2+ (annotations: CHEBI:CHEBI:29108); ADP (annotations: HMDB:HMDB0001341,WIKIPEDIA:ADP,CAS:58-64-0,KEGG_COMPOUND:C00008,PUBCHEM:6022,CHEBI:CHEBI:16761,CHEMBL_COMPOUND:CHEMBL14830,CHEMSPIDER:5800)
  (References: REACTOME:REACT_1068.5|PUBMED:20144582|PUBMED:20435888|PUBMED:14555658|PUBMED:19413950|PUBMED:17432878|PUBMED:16737955)
RID: 55546 (;Heterodimer association'):
  Reactants: GCG (annotations: HGNC_SYMBOL:GCG,,REFSEQ:NM_002054,PUBMED:24692138,HGNC:4191,UNIPROT:P01275,ENTREZ:2641); GCGR
  Products: GCGR:GCG
  Modifiers: None
RID: 56076 (;State transition'):
  Reactants: 7-Dehydrodemosterol (annotations: CHEBI:CHEBI:27910)
  Products: Desmosterol (annotations: CHEBI:CHEBI:17737)
  Modifiers: DHCR7 (formerSymbols: SLOS) (annotations: HGNC:2860,REFSEQ:NM_001360,UNIPROT:Q9UBM7,HGNC_SYMBOL:DHCR7,ENTREZ:1717,)
  (References: DOI:10.1016/B978-0-12-824048-9.00005-5)
RID: 55652 (;State transition'):
  Reactants: Fatty acyl-ACP; Malonyl-ACP (annotations: CHEBI:CHEBI:81869,CHEBI:CHEBI:81867,CHEBI:CHEBI:81868)
  Products: Beta-ketoacyl-ACP
  Modifiers: OXSM (annotations: HGNC:26063,HGNC_SYMBOL:OXSM,REFSEQ:NM_017897,ENTREZ:54995,UNIPROT:Q9NWU1,)
RID: 55871 (;Positive influence'):
  Reactants: CYP4A11 (formerSymbols: CYP4A2) (annotations: ENTREZ:1579,HGNC:2642,UNIPROT:Q02928,REFSEQ:NM_000778,HGNC_SYMBOL:CYP4A11,)
  Products: Microsomal Omega-Oxidation (annotations: WIKIPATHWAYS:WP206)
  Modifiers: None
RID: 55831 (;Positive influence'):
  Reactants: NR1I2 (annotations: ,HGNC_SYMBOL:NR1I2,HGNC:7968,REFSEQ:NM_003889,ENTREZ:8856,UNIPROT:O75469)
  Products: FOXO1 (formerSymbols: FKHR,FOXO1A) (annotations: HGNC:3819,,REFSEQ:NM_002015,ENTREZ:2308,HGNC_SYMBOL:FOXO1,UNIPROT:Q12778)
  Modifiers: None
RID: 56177 (;State transition'):
  Reactants: Dihydroxyacetone-Phosphate (annotations: CHEBI:CHEBI:16108)
  Products: Glycerol-3-Phosphate (annotations: CHEBI:CHEBI:15978)
  Modifiers: GPD1 (annotations: ,UNIPROT:P21695,HGNC:4455,HGNC_SYMBOL:GPD1,ENTREZ:2819,REFSEQ:NM_001257199)
RID: 56011 (;Positive influence'):
  Reactants: AKT1 (annotations: ENTREZ:207,HGNC:391,PUBMED:28416361,HGNC_SYMBOL:AKT1,REFSEQ:NM_005163,UNIPROT:P31749,)
  Products: CREB1 (annotations: REFSEQ:NM_134442,HGNC:2345,ENTREZ:1385,HGNC_SYMBOL:CREB1,UNIPROT:P16220,)
  Modifiers: None
RID: 55232 (;Transcription'):
  Reactants: ELOVL4 (formerSymbols: SCA34,STGD2,STGD3) (annotations: ,HGNC_SYMBOL:ELOVL4,UNIPROT:Q9GZR5,HGNC:14415,ENTREZ:6785,REFSEQ:NM_022726)
  Products: ELOVL4 (formerSymbols: SCA34,STGD2,STGD3) (annotations: ,HGNC_SYMBOL:ELOVL4,UNIPROT:Q9GZR5,HGNC:14415,ENTREZ:6785,REFSEQ:NM_022726)
  Modifiers: SREBF2 (annotations: HGNC:11290,REFSEQ:NM_004599,UNIPROT:Q12772,,HGNC_SYMBOL:SREBF2,ENTREZ:6721)
  (References: WIKIPATHWAYS:WP4718)
RID: 55148 (;State transition'):
  Reactants: HMGCR (annotations: ,REFSEQ:NM_000859,UNIPROT:P04035,HGNC:5006,ENTREZ:3156,HGNC_SYMBOL:HMGCR)
  Products:  
  Modifiers: 24,25-Dihydrolanosterol (annotations: CHEBI:CHEBI:28113)
  (References: DOI:10.1016/B978-0-12-824048-9.00005-5)
RID: 55203 (;Known transition omitted'):
  Reactants: ELOVL2 (annotations: UNIPROT:Q9NXB9,ENTREZ:54898,,HGNC_SYMBOL:ELOVL2,REFSEQ:NM_017770,HGNC:14416)
  Products: Fatty Acid Biosynthesis (annotations: WIKIPATHWAYS:WP4491,GO:GO:0006633)
  Modifiers: None
RID: 56206 (;State transition'):
  Reactants: Glycin (annotations: CHEBI:CHEBI:55443,CHEBI:CHEBI:15428); Methylene-FH4 (annotations: CHEBI:CHEBI:20502)
  Products: Serine (annotations: CHEBI:CHEBI:17822,CHEBI:CHEBI:17115); FH4 (annotations: CHEBI:CHEBI:20506)
  Modifiers: SHMT1 (annotations: ENTREZ:6470,UNIPROT:P34896,REFSEQ:NM_004169,,HGNC:10850,HGNC_SYMBOL:SHMT1); SHMT2 (formerSymbols: SHMT) (annotations: REFSEQ:NM_005412,HGNC:10852,UNIPROT:P34897,ENTREZ:6472,,HGNC_SYMBOL:SHMT2)
RID: 55087 (;State transition'):
  Reactants: Glycerol-3-P
  Products: LysoPhosphatidic Acid
  Modifiers: GPAT2 (annotations: ENTREZ:150763,HGNC_SYMBOL:GPAT2,,REFSEQ:NM_207328,UNIPROT:Q6NUI2,HGNC:27168)
RID: 56145 (;State transition'):
  Reactants: Glucose-6-Phosphate (annotations: CHEBI:CHEBI:14314)
  Products: 6-Phosphogluconolactone (annotations: CHEBI:CHEBI:16938)
  Modifiers: G6PD (annotations: UNIPROT:P11413,HGNC:4057,ENTREZ:2539,HGNC_SYMBOL:G6PD,,REFSEQ:NM_000402)
  (References: WIKIPATHWAYS:WP134)
RID: 55610 (;Negative influence'):
  Reactants: NR1I2 (annotations: ,HGNC_SYMBOL:NR1I2,HGNC:7968,REFSEQ:NM_003889,ENTREZ:8856,UNIPROT:O75469)
  Products: PPARGC1A (formerSymbols: PPARGC1) (annotations: UNIPROT:Q9UBK2,ENTREZ:10891,HGNC:9237,HGNC_SYMBOL:PPARGC1A,,REFSEQ:NM_013261)
  Modifiers: None
RID: 55868 (;Positive influence'):
  Reactants: NR1I2 (annotations: ,HGNC_SYMBOL:NR1I2,HGNC:7968,REFSEQ:NM_003889,ENTREZ:8856,UNIPROT:O75469)
  Products: CD36 (annotations: HGNC:1663,REFSEQ:NM_001001547,HGNC_SYMBOL:CD36,PUBMED:26451809,ENTREZ:948,,UNIPROT:P16671,PUBMED:18477307)
  Modifiers: None
RID: 55239 (;State transition'):
  Reactants: malonyl-CoA (annotations: REACTOME:REACT_3059.1,WIKIPEDIA:Malonyl-CoA,HMDB:HMDB0001175,CAS:524-14-1,CHEBI:CHEBI:15531,PUBCHEM:10663,KEGG_COMPOUND:C00083,CHEMSPIDER:10213)
  Products: malonyl-ACP (annotations: CHEBI:CHEBI:17330)
  Modifiers: FASN (annotations: HGNC:3594,UNIPROT:P49327,REFSEQ:NM_004104,,ENTREZ:2194,HGNC_SYMBOL:FASN)
  (References: WIKIPATHWAYS:WP357)
RID: 55723 (;State transition'):
  Reactants: GYS
  Products: GYS
  Modifiers: PKA
RID: 55093 (;Transport'):
  Reactants: Cholesterol ester (annotations: CHEBI:CHEBI:17002)
  Products: Cholesterol ester (annotations: CHEBI:CHEBI:17002)
  Modifiers: APOE:LRP1
  (References: WIKIPATHWAYS:WP5304)
RID: 55128 (;Transport'):
  Reactants: VLDL (annotations: GO:GO:0034361)
  Products: VLDL (annotations: GO:GO:0034361)
  Modifiers: SORT1 (annotations: ENTREZ:6272,,REFSEQ:NM_002959,UNIPROT:Q99523,HGNC:11186,HGNC_SYMBOL:SORT1)
  (References: WIKIPATHWAYS:WP5304)
RID: 56066 (;Known transition omitted'):
  Reactants: Dihydro-T-MAS (annotations: CHEBI:CHEBI:87044)
  Products: Zymostenol (annotations: CHEBI:CHEBI:16608)
  Modifiers: MSMO1 (formerSymbols: SC4MOL) (annotations: REFSEQ:NM_006745,ENTREZ:6307,,HGNC:10545,UNIPROT:Q15800,HGNC_SYMBOL:MSMO1); NSDHL (annotations: ENTREZ:50814,HGNC:13398,HGNC_SYMBOL:NSDHL,REFSEQ:NM_015922,UNIPROT:Q15738,); HSD17B7 (annotations: ENTREZ:51478,UNIPROT:P56937,HGNC:5215,HGNC_SYMBOL:HSD17B7,REFSEQ:NM_016371,)
  (References: DOI:10.1016/B978-0-12-824048-9.00005-5)
RID: 55272 (;Known transition omitted'):
  Reactants: acetyl-ACP (annotations: CHEBI:CHEBI:17093)
  Products: acetoacetyl-ACP
  Modifiers: FASN (annotations: HGNC:3594,UNIPROT:P49327,REFSEQ:NM_004104,,ENTREZ:2194,HGNC_SYMBOL:FASN)
  (References: WIKIPATHWAYS:WP357)
RID: 55986 (;Known transition omitted'):
  Reactants: HDL
  Products: VLDL
  Modifiers: None
RID: 55941 (;Transport'):
  Reactants: Urea (annotations: CHEBI:CHEBI:16199)
  Products: Urea (annotations: CHEBI:CHEBI:16199)
  Modifiers: AQP9 (annotations: HGNC:643,HGNC_SYMBOL:AQP9,UNIPROT:O43315,REFSEQ:NM_020980,PUBMED:19096781,ENTREZ:366,)
  (References: PUBMED:19096781)
RID: 56180 (;Transport'):
  Reactants: Aspartate (annotations: CHEBI:CHEBI:29995,CHEBI:CHEBI:72314)
  Products: Aspartate (annotations: CHEBI:CHEBI:29995,CHEBI:CHEBI:72314)
  Modifiers: DIC
RID: 55749 (;State transition'):
  Reactants: Fructose (annotations: CHEBI:CHEBI:28645,CHEBI:CHEBI:28757)
  Products: Fructose-1-Phosphate (annotations: CHEBI:CHEBI:18105)
  Modifiers: KHK (annotations: REFSEQ:NM_000221,HGNC_SYMBOL:KHK,HGNC:6315,ENTREZ:3795,UNIPROT:P50053,)
RID: 56139 (;State transition'):
  Reactants: Fructose (annotations: CHEBI:CHEBI:28645,CHEBI:CHEBI:28757)
  Products: Fructose-1-Phosphate (annotations: CHEBI:CHEBI:18105)
  Modifiers: KHK (annotations: REFSEQ:NM_000221,HGNC_SYMBOL:KHK,HGNC:6315,ENTREZ:3795,UNIPROT:P50053,)
RID: 55147 (;Transcription'):
  Reactants: FADS1 (formerSymbols: LLCDL1) (annotations: HGNC:3574,,HGNC_SYMBOL:FADS1,UNIPROT:O60427,ENTREZ:3992,REFSEQ:NM_013402)
  Products: FADS1 (formerSymbols: LLCDL1) (annotations: HGNC:3574,,HGNC_SYMBOL:FADS1,UNIPROT:O60427,ENTREZ:3992,REFSEQ:NM_013402)
  Modifiers: SREBF2 (annotations: HGNC:11290,REFSEQ:NM_004599,UNIPROT:Q12772,,HGNC_SYMBOL:SREBF2,ENTREZ:6721)
  (References: WIKIPATHWAYS:WP4718)
RID: 55899 (;State transition'):
  Reactants: AKT1 (annotations: ENTREZ:207,HGNC:391,PUBMED:28416361,HGNC_SYMBOL:AKT1,REFSEQ:NM_005163,UNIPROT:P31749,)
  Products: AKT1 (annotations: ENTREZ:207,HGNC:391,PUBMED:28416361,HGNC_SYMBOL:AKT1,REFSEQ:NM_005163,UNIPROT:P31749,)
  Modifiers: PHLPP1 (formerSymbols: PHLPP,PLEKHE1) (annotations: HGNC:20610,,HGNC_SYMBOL:PHLPP1,REFSEQ:NM_194449,UNIPROT:O60346,ENTREZ:23239)
RID: 55211 (;State transition'):
  Reactants: Presqualene diphosphate (annotations: CHEBI:CHEBI:15442)
  Products: Presqualene monophosphate  (annotations: CHEBI:CHEBI:134117)
  Modifiers: PLPP6 (formerSymbols: PPAPDC2) (annotations: HGNC_SYMBOL:PLPP6,ENTREZ:403313,,HGNC:23682,UNIPROT:Q8IY26,REFSEQ:NM_203453)
  (References: DOI:10.3180/R-HSA-191273.7)
RID: 55747 (;Negative influence'):
  Reactants: GSK3B (annotations: HGNC_SYMBOL:GSK3B,ENTREZ:2932,PUBMED:28416361,,HGNC:4617,UNIPROT:P49841,REFSEQ:NM_001146156)
  Products: Glycogen Synthesis (annotations: GO:GO:0005978,PUBMED:28416361)
  Modifiers: None
RID: 55185 (;Known transition omitted'):
  Reactants: 7-Dehydrocholesterol (annotations: CHEBI:CHEBI:17759)
  Products: Vitamin D (Calciferol metabolism) (annotations: GO:GO:0042368)
  Modifiers: None
RID: 55616 (;Positive influence'):
  Reactants: IRS2 (annotations: UNIPROT:Q9Y4H2,HGNC:6126,ENTREZ:8660,HGNC_SYMBOL:IRS2,REFSEQ:NM_003749,)
  Products: Insulin signaling (annotations: GO:GO:0008286)
  Modifiers: None
RID: 56171 (;State transition'):
  Reactants: 1,3-Bisphosphoglycerate (annotations: CHEBI:CHEBI:89363)
  Products: 2,3-Bisphosphoglycerate (annotations: CHEBI:CHEBI:19324)
  Modifiers: BPGM (annotations: ENTREZ:669,HGNC_SYMBOL:BPGM,REFSEQ:NM_001724,,HGNC:1093,UNIPROT:P07738)
RID: 55726 (;Known transition omitted'):
  Reactants: T-MAS (annotations: CHEBI:CHEBI:18364)
  Products: Zymosterol (annotations: CHEBI:CHEBI:18252)
  Modifiers: MSMO1 (formerSymbols: SC4MOL) (annotations: REFSEQ:NM_006745,ENTREZ:6307,,HGNC:10545,UNIPROT:Q15800,HGNC_SYMBOL:MSMO1); NSDHL (annotations: ENTREZ:50814,HGNC:13398,HGNC_SYMBOL:NSDHL,REFSEQ:NM_015922,UNIPROT:Q15738,); HSD17B7 (annotations: ENTREZ:51478,UNIPROT:P56937,HGNC:5215,HGNC_SYMBOL:HSD17B7,REFSEQ:NM_016371,)
  (References: DOI:10.1016/B978-0-12-824048-9.00005-5)
RID: 55702 (;Positive influence'):
  Reactants: CREB1 (annotations: REFSEQ:NM_134442,HGNC:2345,ENTREZ:1385,HGNC_SYMBOL:CREB1,UNIPROT:P16220,)
  Products: G6PC (annotations: PUBMED:28416361,)
  Modifiers: None
RID: 55305 (;State transition'):
  Reactants: hC TXN:hC TXN; NADPH (annotations: KEGG_COMPOUND:C00005,HMDB:HMDB0000221,CHEMSPIDER:17215925,CHEMBL_COMPOUND:CHEMBL213053,CHEBI:CHEBI:16474,CAS:53-57-6,WIKIPEDIA:NADPH,PUBCHEM:22833512); H+ (annotations: CHEBI:CHEBI:15378)
  Products: TXN (annotations: ENTREZ:7295,UNIPROT:P10599,HGNC:12435,,REFSEQ:NM_001244938,HGNC_SYMBOL:TXN); NADP+ (annotations: CHEBI:CHEBI:18009,WIKIPEDIA:NADP,KEGG_COMPOUND:C00006,CAS:53-59-8,PUBCHEM:5886,CHEMBL_COMPOUND:CHEMBL213053,HMDB:HMDB0000217,CHEMSPIDER:5675,REACTOME:REACT_4609.3)
  Modifiers: TXNRD1:FAD
  (References: REACTOME:REACT_264249)
RID: 55551 (;State transition'):
  Reactants: ACC
  Products: ACC
  Modifiers: None
RID: 56055 (;State transition'):
  Reactants: IRS2 (formerSymbols: ECHD) (annotations: UNIPROT:Q9Y4H2,HGNC:6126,ENTREZ:8660,HGNC_SYMBOL:IRS2,,REFSEQ:NM_003749)
  Products:  
  Modifiers: None
RID: 55869 (;Positive influence'):
  Reactants: PPARA (formerSymbols: PPAR) (annotations: HGNC_SYMBOL:PPARA,ENTREZ:5465,REFSEQ:NM_001001928,,PUBMED:26451809,UNIPROT:Q07869,HGNC:9232)
  Products: APOA4 (annotations: HGNC_SYMBOL:APOA4,REFSEQ:NM_000482,HGNC:602,ENTREZ:337,,UNIPROT:P06727)
  Modifiers: None
RID: 55526 (;State transition'):
  Reactants: PKLR (annotations: HGNC_SYMBOL:PKLR,REFSEQ:NM_000298,PUBMED:31284506,HGNC:9020,UNIPROT:P30613,ENTREZ:5313,)
  Products: PKLR (annotations: HGNC_SYMBOL:PKLR,REFSEQ:NM_000298,PUBMED:31284506,HGNC:9020,UNIPROT:P30613,ENTREZ:5313,)
  Modifiers: None
RID: 55740 (;State transition'):
  Reactants: Hydroxyacyl-CoA (annotations: CHEBI:CHEBI:65260)
  Products: Ketoacyl-CoA (annotations: CHEBI:CHEBI:57347)
  Modifiers: HADH (formerSymbols: HADHSC) (annotations: HGNC_SYMBOL:HADH,REFSEQ:NM_005327,,HGNC:4799,ENTREZ:3033,UNIPROT:Q16836)
RID: 55178 (;State transition'):
  Reactants: Cholesterol (annotations: CHEBI:CHEBI:16113,KEGG_COMPOUND:C00187)
  Products: 24S-hydroxycholesterol (annotations: CHEBI:CHEBI:34310)
  Modifiers: CYP46A1 (formerSymbols: CYP46) (annotations: REFSEQ:NM_006668,ENTREZ:10858,HGNC:2641,HGNC_SYMBOL:CYP46A1,UNIPROT:Q9Y6A2,)
  (References: WIKIPATHWAYS:WP4718)
RID: 56081 (;State transition'):
  Reactants: Lauroyl-CoA (annotations: CHEBI:CHEBI:15521)
  Products: 2-trans-Dodecenoyl-CoA (annotations: CHEBI:CHEBI:15471)
  Modifiers: ACADL (annotations: ,REFSEQ:NM_001608,HGNC_SYMBOL:ACADL,HGNC:88,ENTREZ:33,UNIPROT:P28330)
RID: 55417 (PDmap:re561.0;State transition'):
  Reactants: 3-hydroxyoctadecanoyl-CoA (annotations: REACTOME:REACT_22804.1,CHEBI:CHEBI:50583)
  Products: trans-2-octadecenoyl-CoA (annotations: CHEBI:CHEBI:50570,REACTOME:REACT_22862.1)
  Modifiers: 3-hydroxyacyl-CoA dehydratase activity (annotations: GO:GO:0018812)
  (References: PUBMED:16564093|PUBMED:4379659|RHEA:39155)
RID: 55655 (;Transport'):
  Reactants: Long-chain Fatty Acids
  Products: Long-chain Fatty Acids
  Modifiers: FABP
  (References: WIKIPATHWAYS:WP5061)
RID: 55208 (;State transition'):
  Reactants: FAPP (annotations: CHEBI:CHEBI:50277)
  Products: Presqualene diphosphate (annotations: CHEBI:CHEBI:15442)
  Modifiers: FDFT1
  (References: DOI:10.3180/R-HSA-191273.7|WIKIPATHWAYS:WP4718|DOI:10.1016/B978-0-12-824048-9.00005-5)
RID: 56095 (;State transition'):
  Reactants: FBP1 (formerSymbols: FBP) (annotations: HGNC_SYMBOL:FBP1,UNIPROT:P09467,REFSEQ:NM_000507,PUBMED:31284506,HGNC:3606,ENTREZ:2203,)
  Products: FBP1 (formerSymbols: FBP) (annotations: HGNC_SYMBOL:FBP1,UNIPROT:P09467,REFSEQ:NM_000507,PUBMED:31284506,HGNC:3606,ENTREZ:2203,)
  Modifiers: None
RID: 56040 (;Positive influence'):
  Reactants: CREB1 (annotations: REFSEQ:NM_134442,HGNC:2345,ENTREZ:1385,HGNC_SYMBOL:CREB1,UNIPROT:P16220,)
  Products: Cell Survival
  Modifiers: None
RID: 55209 (;Transcription'):
  Reactants: FADS2 (formerSymbols: LLCDL2) (annotations: ,HGNC:3575,HGNC_SYMBOL:FADS2,REFSEQ:NM_004265,UNIPROT:O95864,ENTREZ:9415)
  Products: FADS2 (formerSymbols: LLCDL2) (annotations: ,HGNC:3575,HGNC_SYMBOL:FADS2,REFSEQ:NM_004265,UNIPROT:O95864,ENTREZ:9415)
  Modifiers: SREBF2 (annotations: HGNC:11290,REFSEQ:NM_004599,UNIPROT:Q12772,,HGNC_SYMBOL:SREBF2,ENTREZ:6721)
  (References: WIKIPATHWAYS:WP4718)
RID: 56047 (;State transition'):
  Reactants: ADP (annotations: CHEBI:CHEBI:16761)
  Products: ATP (annotations: CHEBI:CHEBI:15422)
  Modifiers: ATP synthase
RID: 55454 (;State transition'):
  Reactants: trans-delta2-enoyl-CoA
  Products: Acyl-CoA (annotations: CHEBI:CHEBI:17984)
  Modifiers: MECR (annotations: ENTREZ:51102,,HGNC:19691,HGNC_SYMBOL:MECR,REFSEQ:NM_016011,UNIPROT:Q9BV79); PECR (annotations: ENTREZ:55825,UNIPROT:Q9BY49,HGNC_SYMBOL:PECR,REFSEQ:NM_018441,HGNC:18281,); DECR1 (formerSymbols: DECR) (annotations: ENTREZ:1666,UNIPROT:Q16698,HGNC:2753,HGNC_SYMBOL:DECR1,REFSEQ:NM_001330575,)
  (References: WIKIPATHWAYS:WP357)
RID: 55786 (;Positive influence'):
  Reactants: Complex I
  Products: Ubiquinone (annotations: CHEBI:CHEBI:16389)
  Modifiers: None
RID: 55321 (;Transport'):
  Reactants: pyruvate (annotations: REACTOME:REACT_3219.1,CHEBI:CHEBI:15361); H+ (annotations: CHEBI:CHEBI:15378)
  Products: pyruvate (annotations: REACTOME:REACT_3219.1,CHEBI:CHEBI:15361); H+ (annotations: CHEBI:CHEBI:15378)
  Modifiers: mitochondrial pyruvate carrier
  (References: REACTOME:REACT_14833.4|PUBMED:11945601|PUBMED:27928028)
RID: 55856 (;State transition'):
  Reactants: PFKL (annotations: HGNC:8876,UNIPROT:P17858,PUBMED:31284506,REFSEQ:NM_001002021,,ENTREZ:5211,HGNC_SYMBOL:PFKL)
  Products: PFKL (annotations: HGNC:8876,UNIPROT:P17858,PUBMED:31284506,REFSEQ:NM_001002021,,ENTREZ:5211,HGNC_SYMBOL:PFKL)
  Modifiers: PKA
RID: 55275 (;State transition'):
  Reactants: Acyl-CoA (annotations: CHEBI:CHEBI:17984)
  Products: long-chain fatty acid (annotations: CHEBI:CHEBI:15904)
  Modifiers: SCD (formerSymbols: SCDOS) (annotations: ,ENTREZ:6319,HGNC_SYMBOL:SCD,UNIPROT:O00767,HGNC:10571,REFSEQ:NM_005063)
  (References: WIKIPATHWAYS:WP357)
RID: 55191 (;Transcription'):
  Reactants: ACOT1 (annotations: UNIPROT:Q86TX2,REFSEQ:NM_001037161,ENTREZ:641371,HGNC:33128,,HGNC_SYMBOL:ACOT1)
  Products: ACOT1 (annotations: UNIPROT:Q86TX2,REFSEQ:NM_001037161,ENTREZ:641371,HGNC:33128,,HGNC_SYMBOL:ACOT1)
  Modifiers: SREBF2 (annotations: HGNC:11290,REFSEQ:NM_004599,UNIPROT:Q12772,,HGNC_SYMBOL:SREBF2,ENTREZ:6721)
  (References: WIKIPATHWAYS:WP4718)
RID: 55152 (;State transition'):
  Reactants: Cholesterol (annotations: CHEBI:CHEBI:16113,KEGG_COMPOUND:C00187)
  Products: 7alpha-hydroxycholesterol (annotations: CHEBI:CHEBI:17500)
  Modifiers: CP7A1
  (References: WIKIPATHWAYS:WP4718)
RID: 56101 (;State transition'):
  Reactants: GPP (annotations: CHEBI:CHEBI:17211)
  Products: FAPP (annotations: CHEBI:CHEBI:50277)
  Modifiers: GGPS1 (annotations: ENTREZ:9453,UNIPROT:O95749,HGNC:4249,HGNC_SYMBOL:GGPS1,REFSEQ:NM_004837,); FDPS (annotations: REFSEQ:NM_002004,HGNC:3631,HGNC_SYMBOL:FDPS,UNIPROT:P14324,,ENTREZ:2224)
  (References: DOI:10.1016/B978-0-12-824048-9.00005-5)
RID: 55166 (;Known transition omitted'):
  Reactants: ABCA1 (formerSymbols: ABC1,HDLDT1) (annotations: REFSEQ:NM_005502,HGNC:29,HGNC_SYMBOL:ABCA1,,ENTREZ:19,UNIPROT:O95477)
  Products: Sterol Eflux (annotations: GO:GO:0035382)
  Modifiers: None
  (References: WIKIPATHWAYS:WP4718)
RID: 55390 (;State transition'):
  Reactants: hydrogen peroxide (annotations: PUBCHEM:784,HMDB:HMDB0003125,KEGG_COMPOUND:C00027,MESH_2012:D006861,CHEBI:CHEBI:16240,WIKIPEDIA:Hydrogen peroxide,CAS:7722-84-1,CHEMBL_COMPOUND:CHEMBL71595,CHEMSPIDER:763); glutathione (annotations: CHEMBL_COMPOUND:CHEMBL1543,CHEBI:CHEBI:16856,HMDB:HMDB0000125,KEGG_COMPOUND:C00051,WIKIPEDIA:Glutathione,CHEMSPIDER:111188,CAS:70-18-8,MESH_2012:D005978,PUBCHEM:124886)
  Products: H2O (annotations: HMDB:HMDB0002111,CHEBI:CHEBI:15377,PUBCHEM:962,CHEMSPIDER:937,MESH_2012:D014867,WIKIPEDIA:Water,CAS:7732-18-5,CHEMBL_COMPOUND:CHEMBL1098659,KEGG_COMPOUND:C00001); glutathione disulfide (annotations: KEGG_COMPOUND:C00127,CHEBI:CHEBI:17858,HMDB:HMDB0003337,PUBCHEM:975,CAS:27025-41-8,WIKIPEDIA:Glutathione disulfide,CHEMBL_COMPOUND:CHEMBL1372,CHEMSPIDER:950)
  Modifiers: GPX3 (annotations: REFSEQ:NM_001329790,ENTREZ:2878,HGNC:4555,HGNC_SYMBOL:GPX3,UNIPROT:P22352,)
  (References: REACTOME:REACT_264249)
RID: 55909 (;Positive influence'):
  Reactants: ACADM  (annotations: UNIPROT:P11310,HGNC_SYMBOL:ACADM,,HGNC:89,REFSEQ:NM_000016,ENTREZ:34)
  Products: Mitochondrial Beta-Oxidation (annotations: WIKIPATHWAYS:WP143)
  Modifiers: None
RID: 56043 (;Known transition omitted'):
  Reactants: Chylomicron
  Products: Chylomicron remnant
  Modifiers: None
RID: 55364 (PDmap:re580.0;State transition'):
  Reactants: hydrogen peroxide (annotations: PUBCHEM:784,HMDB:HMDB0003125,KEGG_COMPOUND:C00027,MESH_2012:D006861,CHEBI:CHEBI:16240,WIKIPEDIA:Hydrogen peroxide,CAS:7722-84-1,CHEMBL_COMPOUND:CHEMBL71595,CHEMSPIDER:763); glutathione (annotations: CHEMBL_COMPOUND:CHEMBL1543,CHEBI:CHEBI:16856,HMDB:HMDB0000125,KEGG_COMPOUND:C00051,WIKIPEDIA:Glutathione,CHEMSPIDER:111188,CAS:70-18-8,MESH_2012:D005978,PUBCHEM:124886)
  Products: H2O (annotations: HMDB:HMDB0002111,CHEBI:CHEBI:15377,PUBCHEM:962,CHEMSPIDER:937,MESH_2012:D014867,WIKIPEDIA:Water,CAS:7732-18-5,CHEMBL_COMPOUND:CHEMBL1098659,KEGG_COMPOUND:C00001); glutathione disulfide (annotations: KEGG_COMPOUND:C00127,CHEBI:CHEBI:17858,HMDB:HMDB0003337,PUBCHEM:975,CAS:27025-41-8,WIKIPEDIA:Glutathione disulfide,CHEMBL_COMPOUND:CHEMBL1372,CHEMSPIDER:950)
  Modifiers: GPX1 (annotations: ENTREZ:2876,HGNC:4553,,UNIPROT:P07203,HGNC_SYMBOL:GPX1,REFSEQ:NM_000581); GPX4 (annotations: ,ENTREZ:2879,HGNC:4556,HGNC_SYMBOL:GPX4,REFSEQ:NM_002085,UNIPROT:P36969)
  (References: PUBMED:19427899)
RID: 55115 (;Transport'):
  Reactants: Cholesterol (annotations: CHEBI:CHEBI:16113,KEGG_COMPOUND:C00187)
  Products: Cholesterol (annotations: CHEBI:CHEBI:16113,KEGG_COMPOUND:C00187)
  Modifiers: None
RID: 55194 (;State transition'):
  Reactants: 7-Dehydrodemosterol (annotations: CHEBI:CHEBI:27910)
  Products: 7-Dehydrocholesterol (annotations: CHEBI:CHEBI:17759)
  Modifiers: DHCR24 (formerSymbols: DCE) (annotations: REFSEQ:NM_014762,HGNC_SYMBOL:DHCR24,,ENTREZ:1718,UNIPROT:Q15392,HGNC:2859)
  (References: DOI:10.1016/B978-0-12-824048-9.00005-5)
RID: 55391 (PDmap:re559.0;State transition'):
  Reactants: palmitoyl-CoA (annotations: REACTOME:REACT_11391.1,CHEMSPIDER:14902,PUBCHEM:15667,HMDB:HMDB0001338,KEGG_COMPOUND:C00154,CHEBI:CHEBI:15525,WIKIPEDIA:palmitoyl CoA,CAS:1763-10-6); malonyl-CoA (annotations: REACTOME:REACT_3059.1,WIKIPEDIA:Malonyl-CoA,HMDB:HMDB0001175,CAS:524-14-1,CHEBI:CHEBI:15531,PUBCHEM:10663,KEGG_COMPOUND:C00083,CHEMSPIDER:10213)
  Products: 3-oxooctadecanoyl-CoA (annotations: CHEBI:CHEBI:50571,REACTOME:REACT_22457.1)
  Modifiers: ELOVL6 (annotations: ENTREZ:79071,HGNC_SYMBOL:ELOVL6,,REFSEQ:NM_024090,UNIPROT:Q9H5J4,HGNC:15829); ELOVL3 (annotations: UNIPROT:Q9HB03,HGNC:18047,ENTREZ:83401,HGNC_SYMBOL:ELOVL3,REFSEQ:NM_152310,); ELOVL7 (annotations: HGNC_SYMBOL:ELOVL7,HGNC:26292,UNIPROT:A1L3X0,ENTREZ:79993,REFSEQ:NM_001104558,)
  (References: PUBMED:16564093|PUBMED:17583696|PUBMED:11567032|REACTOME:REACT_22270.1|PUBMED:12032166|PUBMED:19505953)
RID: 55980 (;Transport'):
  Reactants: H+ (annotations: CHEBI:CHEBI:15378)
  Products: H+ (annotations: CHEBI:CHEBI:15378)
  Modifiers: ATP synthase
RID: 55409 (PDmap:re548.0;State transition'):
  Reactants: acetyl-CoA (annotations: CHEBI:CHEBI:15351,WIKIPEDIA:Acetyl-CoA,HMDB:HMDB0001206,CHEMSPIDER:392413,PUBCHEM:444493,REACTOME:REACT_3839.1,CAS:72-89-9,KEGG_COMPOUND:C00024); hydrogencarbonate (annotations: CHEMBL_COMPOUND:CHEMBL363707,CAS:71-52-3,HMDB:HMDB0000595,REACTOME:REACT_4357.1,CHEMSPIDER:749,PUBCHEM:769,WIKIPEDIA:Bicarbonate,CHEBI:CHEBI:17544,KEGG_COMPOUND:C00288)
  Products: malonyl-CoA (annotations: REACTOME:REACT_3059.1,WIKIPEDIA:Malonyl-CoA,HMDB:HMDB0001175,CAS:524-14-1,CHEBI:CHEBI:15531,PUBCHEM:10663,KEGG_COMPOUND:C00083,CHEMSPIDER:10213)
  Modifiers: ACACA (formerSymbols: ACAC,ACC) (annotations: REFSEQ:NM_198836,UNIPROT:Q13085,HGNC_SYMBOL:ACACA,ENTREZ:31,HGNC:84,)
  (References: PUBMED:18455495|PUBMED:7732023|PUBMED:16854592|REACTOME:REACT_11201.2)
RID: 55494 (;Positive influence'):
  Reactants: AKT1 (annotations: ENTREZ:207,HGNC:391,PUBMED:28416361,HGNC_SYMBOL:AKT1,REFSEQ:NM_005163,UNIPROT:P31749,)
  Products: CDKN1B (annotations: ENTREZ:1027,,,UNIPROT:P46527,HGNC:1785,REFSEQ:NM_004064,HGNC_SYMBOL:CDKN1B)
  Modifiers: None
RID: 55520 (;Positive influence'):
  Reactants: PYGL (annotations: ENTREZ:5836,REFSEQ:NM_002863,HGNC_SYMBOL:PYGL,HGNC:9725,,UNIPROT:P06737)
  Products: Glycogen breakdown
  Modifiers: None
RID: 56163 (;Known transition omitted'):
  Reactants: Xylulosse-5-Phosphate (annotations: CHEBI:CHEBI:16332); Ribose-5-Phosphate (annotations: CHEBI:CHEBI:78679)
  Products: Glyceralaldehyde-3-Phosphate (annotations: CHEBI:CHEBI:17138); Sedoheptulose-7-Phosphate (annotations: CHEBI:CHEBI:15721)
  Modifiers: TKT (annotations: ENTREZ:7086,HGNC:11834,HGNC_SYMBOL:TKT,REFSEQ:NM_001064,,UNIPROT:P29401)
  (References: WIKIPATHWAYS:WP134)
RID: 55911 (;Positive influence'):
  Reactants: 7-Dehydrocholesterol (annotations: CHEBI:CHEBI:17759)
  Products: Vitamin D (Calciferol metabolism) (annotations: GO:GO:0042368)
  Modifiers: None
  (References: DOI:10.1016/B978-0-12-824048-9.00005-5)
RID: 56074 (;State transition'):
  Reactants: Malate (annotations: CHEBI:CHEBI:15595,CHEBI:CHEBI:30797)
  Products: Pyruvate (annotations: CHEBI:CHEBI:15361)
  Modifiers: ME
RID: 55199 (;State transition'):
  Reactants: Zymosterol (annotations: CHEBI:CHEBI:18252)
  Products: Zymostenol (annotations: CHEBI:CHEBI:16608)
  Modifiers: DHCR24 (formerSymbols: DCE) (annotations: REFSEQ:NM_014762,HGNC_SYMBOL:DHCR24,,ENTREZ:1718,UNIPROT:Q15392,HGNC:2859)
  (References: DOI:10.1016/B978-0-12-824048-9.00005-5)
RID: 55295 (PDmap:re549.0;State transition'):
  Reactants: acetyl-CoA (annotations: CHEBI:CHEBI:15351,WIKIPEDIA:Acetyl-CoA,HMDB:HMDB0001206,CHEMSPIDER:392413,PUBCHEM:444493,REACTOME:REACT_3839.1,CAS:72-89-9,KEGG_COMPOUND:C00024); hydrogencarbonate (annotations: CHEMBL_COMPOUND:CHEMBL363707,CAS:71-52-3,HMDB:HMDB0000595,REACTOME:REACT_4357.1,CHEMSPIDER:749,PUBCHEM:769,WIKIPEDIA:Bicarbonate,CHEBI:CHEBI:17544,KEGG_COMPOUND:C00288)
  Products: malonyl-CoA (annotations: REACTOME:REACT_3059.1,WIKIPEDIA:Malonyl-CoA,HMDB:HMDB0001175,CAS:524-14-1,CHEBI:CHEBI:15531,PUBCHEM:10663,KEGG_COMPOUND:C00083,CHEMSPIDER:10213)
  Modifiers: ACACB (annotations: UNIPROT:O00763,HGNC_SYMBOL:ACACB,HGNC:85,REFSEQ:NM_001093,ENTREZ:32,)
  (References: PUBMED:9099716|PUBMED:17223360|REACTOME:REACT_590.3|PUBMED:10677481)
RID: 55183 (;State transition'):
  Reactants: HMG-CoA (annotations: CHEBI:CHEBI:11814)
  Products: Mevalonic acid (annotations: CHEBI:CHEBI:25351)
  Modifiers: HMGCR (annotations: ,REFSEQ:NM_000859,UNIPROT:P04035,HGNC:5006,ENTREZ:3156,HGNC_SYMBOL:HMGCR)
  (References: WIKIPATHWAYS:WP4718|DOI:10.1016/B978-0-12-824048-9.00005-5)
RID: 55327 (PDmap:re514.0;State transition'):
  Reactants: myristoyl-CoA (annotations: CHEBI:CHEBI:15532,REACTOME:REACT_2294.1,HMDB:HMDB0001521,KEGG_COMPOUND:C02593,CHEMSPIDER:58623,CAS:3130-72-1,PUBCHEM:65113)
  Products: trans-tetradec-2-enoyl-CoA (annotations: CHEBI:CHEBI:27721,KEGG_COMPOUND:C05273,CHEMSPIDER:4444333,CAS:38795-33-4,REACTOME:REACT_3421.1,HMDB:HMDB0003946,PUBCHEM:5280767)
  Modifiers: ACADL (annotations: REFSEQ:NM_001608,,HGNC_SYMBOL:ACADL,HGNC:88,ENTREZ:33,UNIPROT:P28330)
  (References: PUBMED:1540149|REACTOME:REACT_1912.2|PUBMED:13295225)
RID: 55233 (;State transition'):
  Reactants: Zymosterol (annotations: CHEBI:CHEBI:18252)
  Products: Cholestadienol (annotations: CHEBI:CHEBI:145214)
  Modifiers: EBP (formerSymbols: CDPX2) (annotations: ENTREZ:10682,REFSEQ:NM_006579,HGNC:3133,UNIPROT:Q15125,HGNC_SYMBOL:EBP,)
  (References: WIKIPATHWAYS:WP4718|DOI:10.1016/B978-0-12-824048-9.00005-5)
RID: 56085 (;State transition'):
  Reactants: GYS
  Products: GYS
  Modifiers: None
RID: 55281 (;Transport'):
  Reactants: glutathione (annotations: CHEMBL_COMPOUND:CHEMBL1543,CHEBI:CHEBI:16856,HMDB:HMDB0000125,KEGG_COMPOUND:C00051,WIKIPEDIA:Glutathione,CHEMSPIDER:111188,CAS:70-18-8,MESH_2012:D005978,PUBCHEM:124886)
  Products: glutathione (annotations: CHEMBL_COMPOUND:CHEMBL1543,CHEBI:CHEBI:16856,HMDB:HMDB0000125,KEGG_COMPOUND:C00051,WIKIPEDIA:Glutathione,CHEMSPIDER:111188,CAS:70-18-8,MESH_2012:D005978,PUBCHEM:124886)
  Modifiers: None
  (References: PUBMED:23283974)
RID: 55401 (PDmap:re583.0;State transition'):
  Reactants: hydroxyl (annotations: CHEBI:CHEBI:29191); Fe2+ (annotations: CHEBI:CHEBI:29033)
  Products: hydroxide (annotations: PUBCHEM:961,CHEBI:CHEBI:16234,KEGG_COMPOUND:C01328,HMDB:HMDB0001039,CHEMSPIDER:936,CAS:14280-30-9,WIKIPEDIA:Hydroxide,MESH_2012:C031356); Fe3+ (annotations: CHEBI:CHEBI:29034)
  Modifiers: None
  (References: PUBMED:2172697)
RID: 55326 (;State transition'):
  Reactants: NDUFA9 (formerSymbols: NDUFS2L) (annotations: UNIPROT:Q16795,ENTREZ:4704,REFSEQ:NM_005002,,HGNC:7693,HGNC_SYMBOL:NDUFA9)
  Products: NDUFA9 (formerSymbols: NDUFS2L) (annotations: UNIPROT:Q16795,ENTREZ:4704,REFSEQ:NM_005002,,HGNC:7693,HGNC_SYMBOL:NDUFA9)
  Modifiers: SIRT3 (annotations: ENTREZ:23410,HGNC_SYMBOL:SIRT3,UNIPROT:Q9NTG7,HGNC:14931,REFSEQ:NM_001017524,)
  (References: PUBMED:18794531|PUBMED:21658599|PUBMED:24652937)
RID: 55712 (;Known transition omitted'):
  Reactants: Oxalacetate (annotations: CHEBI:CHEBI:16452); Glutamate (annotations: CHEBI:CHEBI:29987,CHEBI:CHEBI:14321,CHEBI:CHEBI:16015,CHEBI:CHEBI:18237)
  Products: Aspartate (annotations: CHEBI:CHEBI:29995,CHEBI:CHEBI:72314); α-Ketogluatarate (annotations: CHEBI:CHEBI:30915)
  Modifiers: GOT2 (annotations: HGNC:4433,,HGNC_SYMBOL:GOT2,ENTREZ:2806,REFSEQ:NM_002080,UNIPROT:P00505)
RID: 55441 (PDmap:re547.0;State transition'):
  Reactants: citrate(3-) (annotations: KEGG_COMPOUND:C00158,PUBCHEM:311,CHEBI:CHEBI:30769,CHEBI:CHEBI:16947,WIKIPEDIA:Citric acid,REACTOME:REACT_2769.1,CHEMBL_COMPOUND:CHEMBL1261,CHEMSPIDER:305,HMDB:HMDB0000094,CAS:77-92-9)
  Products: acetyl-CoA (annotations: CHEBI:CHEBI:15351,WIKIPEDIA:Acetyl-CoA,HMDB:HMDB0001206,CHEMSPIDER:392413,PUBCHEM:444493,REACTOME:REACT_3839.1,CAS:72-89-9,KEGG_COMPOUND:C00024); oxaloacetate(2-) (annotations: PUBCHEM:970,CHEBI:CHEBI:30744,KEGG_COMPOUND:C00036,CAS:328-42-7,HMDB:HMDB0000223,CHEMSPIDER:945,REACTOME:REACT_5376.1,CHEBI:CHEBI:16452,WIKIPEDIA:Oxalacetic acid)
  Modifiers: ACLY (annotations: HGNC:115,REFSEQ:NM_001096,,ENTREZ:47,HGNC_SYMBOL:ACLY,UNIPROT:P53396)
  (References: PUBMED:1371749|REACTOME:REACT_1141.2)
RID: 55297 (PDmap:re239.0;Positive influence'):
  Reactants: H+ (annotations: CHEBI:CHEBI:15378)
  Products: H+ (annotations: CHEBI:CHEBI:15378)
  Modifiers: None
  (References: PUBMED:19427899)
RID: 55351 (PDmap:re576.0;State transition'):
  Reactants: superoxide (annotations: HMDB:HMDB0002168,WIKIPEDIA:Superoxide,PUBCHEM:5359597,CHEMSPIDER:4514331,KEGG_COMPOUND:C00704,CHEBI:CHEBI:18421,CAS:11062-77-4); H+ (annotations: CHEBI:CHEBI:15378)
  Products: hydrogen peroxide (annotations: PUBCHEM:784,HMDB:HMDB0003125,KEGG_COMPOUND:C00027,MESH_2012:D006861,CHEBI:CHEBI:16240,WIKIPEDIA:Hydrogen peroxide,CAS:7722-84-1,CHEMBL_COMPOUND:CHEMBL71595,CHEMSPIDER:763)
  Modifiers: None
  (References: PUBMED:19427899)
RID: 55685 (;Positive influence'):
  Reactants: PPARA (formerSymbols: PPAR) (annotations: HGNC_SYMBOL:PPARA,ENTREZ:5465,REFSEQ:NM_001001928,,PUBMED:26451809,UNIPROT:Q07869,HGNC:9232)
  Products: HADH (formerSymbols: HADHSC) (annotations: HGNC_SYMBOL:HADH,REFSEQ:NM_005327,,HGNC:4799,ENTREZ:3033,UNIPROT:Q16836)
  Modifiers: None
RID: 55603 (;Positive influence'):
  Reactants: FOXO1 (formerSymbols: FKHR,FOXO1A) (annotations: HGNC:3819,,REFSEQ:NM_002015,ENTREZ:2308,PUBMED:28416361,HGNC_SYMBOL:FOXO1,UNIPROT:Q12778)
  Products: PCK1 (annotations: ,PUBMED:28416361,HGNC:8724,UNIPROT:P35558,HGNC_SYMBOL:PCK1,REFSEQ:NM_002591,ENTREZ:5105)
  Modifiers: None
RID: 55306 (PDmap:re364.0;State transition'):
  Reactants: O2 (annotations: CHEBI:CHEBI:15379,KEGG_COMPOUND:C00007,HMDB:HMDB0001377,PUBCHEM:977,CHEMSPIDER:952,CAS:7782-44-7,WIKIPEDIA:Oxygen); CYCS (annotations: HGNC:19986,UNIPROT:P99999,ENTREZ:54205,HGNC_SYMBOL:CYCS,,REFSEQ:NM_018947); H+ (annotations: CHEBI:CHEBI:15378); e-
  Products: H2O (annotations: HMDB:HMDB0002111,CHEBI:CHEBI:15377,PUBCHEM:962,CHEMSPIDER:937,MESH_2012:D014867,WIKIPEDIA:Water,CAS:7732-18-5,CHEMBL_COMPOUND:CHEMBL1098659,KEGG_COMPOUND:C00001); CYCS (annotations: HGNC:19986,UNIPROT:P99999,ENTREZ:54205,HGNC_SYMBOL:CYCS,,REFSEQ:NM_018947); H+ (annotations: CHEBI:CHEBI:15378)
  Modifiers: complex IV (annotations: GO:GO:0045277)
  (References: PUBMED:16199211)
RID: 55121 (;Transport'):
  Reactants: Long-chain Fatty Acids (annotations: CHEBI:CHEBI:15904)
  Products: Peroxisomal Beta-Oxidation (annotations: GO:GO:0006635,WIKIPATHWAYS:WP1941)
  Modifiers: FABP
RID: 55705 (;Heterodimer association'):
  Reactants: PPARGC1A (formerSymbols: PPARGC1) (annotations: UNIPROT:Q9UBK2,ENTREZ:10891,HGNC:9237,HGNC_SYMBOL:PPARGC1A,,REFSEQ:NM_013261); PPARG (annotations: HGNC:9236,REFSEQ:NM_005037,HGNC_SYMBOL:PPARG,UNIPROT:P37231,,ENTREZ:5468)
  Products: PPARG:PPARGC1A
  Modifiers: None
RID: 55234 (;Unknown negative influence'):
  Reactants: Cholesterol (annotations: CHEBI:CHEBI:16113,KEGG_COMPOUND:C00187)
  Products: DHCR24 (formerSymbols: DCE) (annotations: REFSEQ:NM_014762,HGNC_SYMBOL:DHCR24,,ENTREZ:1718,UNIPROT:Q15392,HGNC:2859)
  Modifiers: None
RID: 55400 (;State transition'):
  Reactants: NADH (annotations: REACTOME:REACT_2390.1,KEGG_COMPOUND:C00004,HMDB:HMDB0001487,CHEMSPIDER:903,WIKIPEDIA:NADH,CAS:58-68-4,CHEBI:CHEBI:16908,PUBCHEM:928,CHEMBL_COMPOUND:CHEMBL1628272,MESH_2012:D009243)
  Products: NAD(+) (annotations: KEGG_COMPOUND:C00003,CAS:53-84-9,PUBCHEM:5893,CHEMSPIDER:5682,REACTOME:REACT_4970.1,CHEBI:CHEBI:15846,HMDB:HMDB0000902,WIKIPEDIA:NAD)
  Modifiers: malate-aspartate shuttle (annotations: GO:GO:0043490)
  (References: PUBMED:23986233|PUBMED:25809592|PUBMED:23216354|PUBMED:16368075)
RID: 55398 (PDmap:re380.0;State transition'):
  Reactants: pyruvate (annotations: REACTOME:REACT_3219.1,CHEBI:CHEBI:15361); coenzyme A (annotations: CHEBI:CHEBI:15346,REACTOME:REACT_3654.2); NAD(+) (annotations: KEGG_COMPOUND:C00003,CAS:53-84-9,PUBCHEM:5893,CHEMSPIDER:5682,REACTOME:REACT_4970.1,CHEBI:CHEBI:15846,HMDB:HMDB0000902,WIKIPEDIA:NAD)
  Products: acetyl-CoA (annotations: CHEBI:CHEBI:15351,WIKIPEDIA:Acetyl-CoA,HMDB:HMDB0001206,CHEMSPIDER:392413,PUBCHEM:444493,REACTOME:REACT_3839.1,CAS:72-89-9,KEGG_COMPOUND:C00024); NADH (annotations: REACTOME:REACT_2390.1,KEGG_COMPOUND:C00004,HMDB:HMDB0001487,CHEMSPIDER:903,WIKIPEDIA:NADH,CAS:58-68-4,CHEBI:CHEBI:16908,PUBCHEM:928,CHEMBL_COMPOUND:CHEMBL1628272,MESH_2012:D009243); CO2 (annotations: CHEMSPIDER:274,CHEBI:CHEBI:16526,MESH_2012:D002245,CHEMBL_COMPOUND:CHEMBL1231871,PUBCHEM:280,WIKIPEDIA:Carbon Dioxide,HMDB:HMDB0001967,KEGG_COMPOUND:C00011,CAS:124-38-9); H+ (annotations: CHEBI:CHEBI:15378)
  Modifiers: pyruvate dehydrogenase complex (annotations: REACTOME:REACT_5500.1,GO:GO:0005967)
  (References: PUBMED:11752427|PUBMED:15946682|PUBMED:10679936|PUBMED:15138885|PUBMED:2188967|PUBMED:16049940|REACTOME:REACT_983.3)
RID: 55950 (;State transition'):
  Reactants: Fatty Omega-aldoacid
  Products: Fatty Dicarboxilic Acid
  Modifiers: ALDH
  (References: WIKIPATHWAYS:WP206)
RID: 55260 (;Trigger'):
  Reactants: Mt replication (annotations: DOI:10.1155/2010/737385,DOI:10.1042/EBC20170103,GO:GO:0006264)
  Products: mt DNA replication
  Modifiers: None
  (References: PUBMED:23149385|TAXONOMY:10090|DOI:10.1101/gad.316547.118)
RID: 55460 (;State transition'):
  Reactants: superoxide (annotations: HMDB:HMDB0002168,WIKIPEDIA:Superoxide,PUBCHEM:5359597,CHEMSPIDER:4514331,KEGG_COMPOUND:C00704,CHEBI:CHEBI:18421,CAS:11062-77-4); H+ (annotations: CHEBI:CHEBI:15378)
  Products: O2 (annotations: CHEBI:CHEBI:15379,KEGG_COMPOUND:C00007,HMDB:HMDB0001377,PUBCHEM:977,CHEMSPIDER:952,CAS:7782-44-7,WIKIPEDIA:Oxygen); hydrogen peroxide (annotations: PUBCHEM:784,HMDB:HMDB0003125,KEGG_COMPOUND:C00027,MESH_2012:D006861,CHEBI:CHEBI:16240,WIKIPEDIA:Hydrogen peroxide,CAS:7722-84-1,CHEMBL_COMPOUND:CHEMBL71595,CHEMSPIDER:763)
  Modifiers: SOD3:Cu2+:Zn2+
  (References: REACTOME:REACT_264249)
RID: 55217 (;Known transition omitted'):
  Reactants: HMGCS2 (annotations: UNIPROT:P54868,HGNC:5008,HGNC_SYMBOL:HMGCS2,ENTREZ:3158,,REFSEQ:NM_005518)
  Products: Ketogenesis (annotations: WIKIPATHWAYS:WP5175)
  Modifiers: None
RID: 56147 (;Known transition omitted'):
  Reactants: Xylulosse-5-Phosphate (annotations: CHEBI:CHEBI:16332); Erythrose-4-Phosphate (annotations: CHEBI:CHEBI:48153)
  Products: Fructose-6-Phosphate (annotations: CHEBI:CHEBI:15946,CHEBI:CHEBI:16084); Glyceralaldehyde-3-Phosphate (annotations: CHEBI:CHEBI:17138)
  Modifiers: TKT (annotations: ENTREZ:7086,HGNC:11834,HGNC_SYMBOL:TKT,REFSEQ:NM_001064,,UNIPROT:P29401)
  (References: WIKIPATHWAYS:WP134)
RID: 55254 (PDmap:re518.0;State transition'):
  Reactants: lauroyl-CoA (annotations: CHEBI:CHEBI:15521,KEGG_COMPOUND:C01832,CHEMSPIDER:145018,CAS:6244-92-4,REACTOME:REACT_2800.1,HMDB:HMDB0003571,PUBCHEM:165436)
  Products: trans-dodec-2-enoyl-CoA (annotations: CHEBI:CHEBI:15471,REACTOME:REACT_5571.1)
  Modifiers: ACADL (annotations: REFSEQ:NM_001608,,HGNC_SYMBOL:ACADL,HGNC:88,ENTREZ:33,UNIPROT:P28330)
  (References: PUBMED:1540149|REACTOME:REACT_1177.2|PUBMED:13295225)
RID: 55368 (;Transport'):
  Reactants: fatty acyl-CoA (annotations: CHEBI:CHEBI:37554,REACTOME:REACT_5036.3)
  Products: fatty acyl-CoA (annotations: CHEBI:CHEBI:37554,REACTOME:REACT_5036.3)
  Modifiers: None
  (References: WIKIPATHWAYS:WP357)
RID: 55420 (;Positive influence'):
  Reactants: H+ (annotations: CHEBI:CHEBI:15378)
  Products: mitochondrial depolarization (annotations: GO:GO:0051882)
  Modifiers: None
  (References: PUBMED:15738989)
RID: 55101 (;Known transition omitted'):
  Reactants: Cholesterol (annotations: CHEBI:CHEBI:16113,KEGG_COMPOUND:C00187); NPC2 (annotations: ,REFSEQ:NM_006432,HGNC_SYMBOL:NPC2,UNIPROT:P61916,HGNC:14537,ENTREZ:10577)
  Products: Cholesterol (annotations: CHEBI:CHEBI:16113,KEGG_COMPOUND:C00187)
  Modifiers: STARD3:VDAC1; TSPO (formerSymbols: BZRP) (annotations: HGNC:1158,HGNC_SYMBOL:TSPO,REFSEQ:NM_007311,,UNIPROT:P30536,ENTREZ:706,UNIPROT:B1AH88)
  (References: WIKIPATHWAYS:WP5304)
RID: 55991 (;State transition'):
  Reactants: α-Ketogluatarate (annotations: CHEBI:CHEBI:30915)
  Products: Succinyl-CoA (annotations: CHEBI:CHEBI:15380,CHEBI:CHEBI:57292); NADH (annotations: CHEBI:CHEBI:16908)
  Modifiers: OGDH (annotations: ENTREZ:4967,REFSEQ:NM_001003941,UNIPROT:Q02218,HGNC_SYMBOL:OGDH,HGNC:8124,)
RID: 55320 (PDmap:re237.0;Positive influence'):
  Reactants: H+ (annotations: CHEBI:CHEBI:15378)
  Products: H+ (annotations: CHEBI:CHEBI:15378)
  Modifiers: None
  (References: PUBMED:19427899)
RID: 55371 (;State transition'):
  Reactants: O2 (annotations: CHEBI:CHEBI:15379,KEGG_COMPOUND:C00007,HMDB:HMDB0001377,PUBCHEM:977,CHEMSPIDER:952,CAS:7782-44-7,WIKIPEDIA:Oxygen)
  Products: superoxide (annotations: HMDB:HMDB0002168,WIKIPEDIA:Superoxide,PUBCHEM:5359597,CHEMSPIDER:4514331,KEGG_COMPOUND:C00704,CHEBI:CHEBI:18421,CAS:11062-77-4)
  Modifiers: None
  (References: PUBMED:19427899|PUBMED:15262965)
RID: 55629 (;Positive influence'):
  Reactants: PPARGC1A (formerSymbols: PPARGC1) (annotations: UNIPROT:Q9UBK2,ENTREZ:10891,HGNC:9237,HGNC_SYMBOL:PPARGC1A,,REFSEQ:NM_013261)
  Products: FOXO1 (formerSymbols: FKHR,FOXO1A) (annotations: HGNC:3819,,REFSEQ:NM_002015,ENTREZ:2308,PUBMED:28416361,HGNC_SYMBOL:FOXO1,UNIPROT:Q12778)
  Modifiers: None
RID: 56118 (;State transition'):
  Reactants: NR1H3 (annotations: REFSEQ:NM_001130101,,HGNC:7966,ENTREZ:10062,UNIPROT:Q13133,HGNC_SYMBOL:NR1H3)
  Products: NR1H3 (annotations: REFSEQ:NM_001130101,,HGNC:7966,ENTREZ:10062,UNIPROT:Q13133,HGNC_SYMBOL:NR1H3)
  Modifiers: Desmosterol (annotations: CHEBI:CHEBI:17737)
  (References: DOI:10.1016/B978-0-12-824048-9.00005-5)
RID: 55476 (;Positive influence'):
  Reactants: CDKN1B (annotations: ENTREZ:1027,,,UNIPROT:P46527,HGNC:1785,REFSEQ:NM_004064,HGNC_SYMBOL:CDKN1B)
  Products: Cell Proliferation (annotations: GO:GO:0072574)
  Modifiers: None
RID: 55402 (;Positive influence'):
  Reactants: Ca2+ (annotations: CHEBI:CHEBI:29108)
  Products: SLC25A12 (annotations: ,HGNC_SYMBOL:SLC25A12,HGNC:10982,REFSEQ:NM_003705,ENTREZ:8604,UNIPROT:O75746)
  Modifiers: None
  (References: PUBMED:22443365|PUBMED:25809592)
RID: 55168 (;State transition'):
  Reactants: SQOX (annotations: CHEBI:CHEBI:78662)
  Products: LNSOL (annotations: CHEBI:CHEBI:16521)
  Modifiers: LSS (annotations: HGNC_SYMBOL:LSS,,REFSEQ:NM_001001438,UNIPROT:P48449,ENTREZ:4047,HGNC:6708)
  (References: WIKIPATHWAYS:WP4718|DOI:10.1016/B978-0-12-824048-9.00005-5)
RID: 55756 (;Transport'):
  Reactants: AKT1 (annotations: ENTREZ:207,HGNC:391,PUBMED:28416361,HGNC_SYMBOL:AKT1,REFSEQ:NM_005163,UNIPROT:P31749,)
  Products: AKT1 (annotations: ENTREZ:207,HGNC:391,PUBMED:28416361,HGNC_SYMBOL:AKT1,REFSEQ:NM_005163,UNIPROT:P31749,)
  Modifiers: None
RID: 56142 (;Transport'):
  Reactants: Fructose-6-Phosphate (annotations: CHEBI:CHEBI:15946,CHEBI:CHEBI:16084)
  Products: Fructose-6-Phosphate (annotations: CHEBI:CHEBI:15946,CHEBI:CHEBI:16084)
  Modifiers: None
RID: 56006 (;State transition'):
  Reactants: 1,3-Bisphosphoglycerate (annotations: CHEBI:CHEBI:89363)
  Products: 3-Phosphoglycerate (annotations: CHEBI:CHEBI:17050,CHEBI:CHEBI:17794,CHEBI:CHEBI:57998)
  Modifiers: PGK1 (annotations: ,UNIPROT:P00558,HGNC:8896,HGNC_SYMBOL:PGK1,ENTREZ:5230,REFSEQ:NM_000291)
RID: 55659 (;State transition'):
  Reactants: FAPP (annotations: CHEBI:CHEBI:50277)
  Products: SQNE (annotations: CHEBI:CHEBI:15440)
  Modifiers: FDFT1 (annotations: HGNC_SYMBOL:FDFT1,REFSEQ:NM_001287742,,UNIPROT:P37268,ENTREZ:2222,HGNC:3629)
  (References: DOI:10.1016/B978-0-12-824048-9.00005-5)
RID: 55096 (;Transport'):
  Reactants: Cholesterol ester (annotations: CHEBI:CHEBI:17002)
  Products: Cholesterol ester (annotations: CHEBI:CHEBI:17002)
  Modifiers: MTTP (formerSymbols: MTP) (annotations: HGNC:7467,REFSEQ:NM_000253,ENTREZ:4547,HGNC_SYMBOL:MTTP,,WIKIPATHWAYS:WP430,UNIPROT:P55157,PUBMED:18477307)
  (References: PUBMED:18477307)
RID: 56215 (;Known transition omitted'):
  Reactants: Sedoheptulose-7-Phosphate (annotations: CHEBI:CHEBI:15721); Glyceralaldehyde-3-Phosphate (annotations: CHEBI:CHEBI:17138)
  Products: Erythrose-4-Phosphate (annotations: CHEBI:CHEBI:48153); Fructose-6-Phosphate (annotations: CHEBI:CHEBI:15946,CHEBI:CHEBI:16084)
  Modifiers: TALDO1 (annotations: ,REFSEQ:NM_006755,HGNC:11559,UNIPROT:P37837,HGNC_SYMBOL:TALDO1,ENTREZ:6888)
  (References: WIKIPATHWAYS:WP134)
RID: 55141 (;State transition'):
  Reactants: Zymostenol (annotations: CHEBI:CHEBI:16608)
  Products: Lathosterol (annotations: CHEBI:CHEBI:17168)
  Modifiers: EBP (formerSymbols: CDPX2) (annotations: ENTREZ:10682,REFSEQ:NM_006579,HGNC:3133,UNIPROT:Q15125,HGNC_SYMBOL:EBP,)
  (References: WIKIPATHWAYS:WP4718|DOI:10.1016/B978-0-12-824048-9.00005-5)
RID: 56019 (;State transition'):
  Reactants: Glucose-6-Phosphate (annotations: CHEBI:CHEBI:14314)
  Products: Glucose-1-Phosphate (annotations: CHEBI:CHEBI:29042)
  Modifiers: PGM1 (annotations: ,HGNC:8905,HGNC_SYMBOL:PGM1,REFSEQ:NM_002633,UNIPROT:P36871,ENTREZ:5236)
RID: 55971 (;Known transition omitted'):
  Reactants: Chylomicron
  Products: Nascent HDL
  Modifiers: None
RID: 56203 (;State transition'):
  Reactants: Phosphoenolpyruvate (annotations: CHEBI:CHEBI:18021,CHEBI:CHEBI:44897,CHEBI:CHEBI:58702)
  Products: Pyruvate (annotations: CHEBI:CHEBI:15361)
  Modifiers: PKLR (annotations: HGNC_SYMBOL:PKLR,REFSEQ:NM_000298,PUBMED:31284506,HGNC:9020,UNIPROT:P30613,ENTREZ:5313,)
  (References: WIKIPATHWAYS:WP534)
RID: 55964 (;Positive influence'):
  Reactants: ACOX1 (annotations: UNIPROT:Q15067,HGNC:119,,ENTREZ:51,HGNC_SYMBOL:ACOX1,REFSEQ:NM_001185039)
  Products: Fatty Acid Metabolism (annotations: GO:GO:0009062)
  Modifiers: None
RID: 56141 (;State transition'):
  Reactants: PFKL (annotations: HGNC:8876,UNIPROT:P17858,PUBMED:31284506,REFSEQ:NM_001002021,,ENTREZ:5211,HGNC_SYMBOL:PFKL)
  Products: PFKL (annotations: HGNC:8876,UNIPROT:P17858,PUBMED:31284506,REFSEQ:NM_001002021,,ENTREZ:5211,HGNC_SYMBOL:PFKL)
  Modifiers: None
RID: 55475 (;Negative influence'):
  Reactants: AMPK (annotations: GO:GO:0031588)
  Products: mTORC1 (annotations: GO:GO:0031931)
  Modifiers: None
  (References: PUBMED:22539004|PUBMED:23361334)
RID: 55539 (;State transition'):
  Reactants: PYGL (annotations: ENTREZ:5836,REFSEQ:NM_002863,HGNC_SYMBOL:PYGL,HGNC:9725,,UNIPROT:P06737)
  Products: PYGL (annotations: ENTREZ:5836,REFSEQ:NM_002863,HGNC_SYMBOL:PYGL,HGNC:9725,,UNIPROT:P06737)
  Modifiers: Phosphorylase kinase (PHK)
RID: 55608 (;State transition'):
  Reactants: PKLR (annotations: HGNC_SYMBOL:PKLR,REFSEQ:NM_000298,PUBMED:31284506,HGNC:9020,UNIPROT:P30613,ENTREZ:5313,)
  Products: PKLR (annotations: HGNC_SYMBOL:PKLR,REFSEQ:NM_000298,HGNC:9020,UNIPROT:P30613,ENTREZ:5313,)
  Modifiers: None
RID: 55405 (PDmap:re475.0;State transition'):
  Reactants: GLUD1 (formerSymbols: GLUD) (annotations: ENTREZ:2746,HGNC:4335,UNIPROT:P00367,,REFSEQ:NM_005271,HGNC_SYMBOL:GLUD1)
  Products: GLUD1 (formerSymbols: GLUD) (annotations: ENTREZ:2746,HGNC:4335,UNIPROT:P00367,,REFSEQ:NM_005271,HGNC_SYMBOL:GLUD1)
  Modifiers: SIRT3 (annotations: ENTREZ:23410,HGNC_SYMBOL:SIRT3,UNIPROT:Q9NTG7,HGNC:14931,REFSEQ:NM_001017524,)
  (References: PUBMED:18680753)
RID: 55280 (;State transition'):
  Reactants: TIM9-TIM10 complex (annotations: GO:GO:0042719)
  Products: TIM9-TIM10 complex (annotations: GO:GO:0042719)
  Modifiers: None
  (References: DOI:10.1101/2020.03.22.002386)
RID: 55688 (;State transition'):
  Reactants: Crotonoyl-CoA (annotations: CHEBI:CHEBI:15473,CHEBI:CHEBI:57332)
  Products: (S)-3-hydroxybutanoyl-CoA (annotations: CHEBI:CHEBI:15453,CHEBI:CHEBI:37050,CHEBI:CHEBI:57316)
  Modifiers: ECHS1 (annotations: HGNC_SYMBOL:ECHS1,,ENTREZ:1892,UNIPROT:P30084,HGNC:3151,REFSEQ:NM_004092)
RID: 55675 (;Positive influence'):
  Reactants: AKT1 (annotations: ENTREZ:207,HGNC:391,PUBMED:28416361,HGNC_SYMBOL:AKT1,REFSEQ:NM_005163,UNIPROT:P31749,)
  Products: CDKN1A (formerSymbols: CDKN1) (annotations: REFSEQ:NM_078467,UNIPROT:P38936,HGNC_SYMBOL:CDKN1A,,HGNC:1784,ENTREZ:1026)
  Modifiers: None
RID: 55574 (;State transition'):
  Reactants: PYGL (annotations: ENTREZ:5836,REFSEQ:NM_002863,HGNC_SYMBOL:PYGL,HGNC:9725,,UNIPROT:P06737)
  Products: PYGL (annotations: ENTREZ:5836,REFSEQ:NM_002863,HGNC_SYMBOL:PYGL,HGNC:9725,,UNIPROT:P06737)
  Modifiers: Phosphorylase kinase (PHK)
RID: 55565 (;Negative influence'):
  Reactants: AMPK (annotations: GO:GO:0031588)
  Products: mTORC1 (annotations: GO:GO:0031931)
  Modifiers: None
RID: 55307 (PDmap:re473.0;State transition'):
  Reactants: L-glutamate(2-) (annotations: CHEBI:CHEBI:29988); H2O (annotations: HMDB:HMDB0002111,CHEBI:CHEBI:15377,PUBCHEM:962,CHEMSPIDER:937,MESH_2012:D014867,WIKIPEDIA:Water,CAS:7732-18-5,CHEMBL_COMPOUND:CHEMBL1098659,KEGG_COMPOUND:C00001); NAD(+) (annotations: KEGG_COMPOUND:C00003,CAS:53-84-9,PUBCHEM:5893,CHEMSPIDER:5682,REACTOME:REACT_4970.1,CHEBI:CHEBI:15846,HMDB:HMDB0000902,WIKIPEDIA:NAD)
  Products: 2-oxoglutaric acid (annotations: KEGG_COMPOUND:C00026,REACTOME:REACT_3871.1,CHEBI:CHEBI:30915,CAS:328-50-7,MESH_2012:C029743,PUBCHEM:51,CHEMSPIDER:50,HMDB:HMDB0000208,WIKIPEDIA:Alpha-Ketoglutaric_acid); H+ (annotations: CHEBI:CHEBI:15378); NADH (annotations: REACTOME:REACT_2390.1,KEGG_COMPOUND:C00004,HMDB:HMDB0001487,CHEMSPIDER:903,WIKIPEDIA:NADH,CAS:58-68-4,CHEBI:CHEBI:16908,PUBCHEM:928,CHEMBL_COMPOUND:CHEMBL1628272,MESH_2012:D009243); ammonium (annotations: CHEBI:CHEBI:28938)
  Modifiers: GLUD1 (formerSymbols: GLUD) (annotations: ENTREZ:2746,HGNC:4335,UNIPROT:P00367,,REFSEQ:NM_005271,HGNC_SYMBOL:GLUD1)
  (References: REACTOME:REACT_710.4)
RID: 55411 (;State transition'):
  Reactants: O2 (annotations: CHEBI:CHEBI:15379,KEGG_COMPOUND:C00007,HMDB:HMDB0001377,PUBCHEM:977,CHEMSPIDER:952,CAS:7782-44-7,WIKIPEDIA:Oxygen); NADPH (annotations: KEGG_COMPOUND:C00005,HMDB:HMDB0000221,CHEMSPIDER:17215925,CHEMBL_COMPOUND:CHEMBL213053,CHEBI:CHEBI:16474,CAS:53-57-6,WIKIPEDIA:NADPH,PUBCHEM:22833512)
  Products: superoxide (annotations: HMDB:HMDB0002168,WIKIPEDIA:Superoxide,PUBCHEM:5359597,CHEMSPIDER:4514331,KEGG_COMPOUND:C00704,CHEBI:CHEBI:18421,CAS:11062-77-4); NADP+ (annotations: CHEBI:CHEBI:18009,WIKIPEDIA:NADP,KEGG_COMPOUND:C00006,CAS:53-59-8,PUBCHEM:5886,CHEMBL_COMPOUND:CHEMBL213053,HMDB:HMDB0000217,CHEMSPIDER:5675,REACTOME:REACT_4609.3); H+ (annotations: CHEBI:CHEBI:15378)
  Modifiers: NOX4:NOX5
  (References: REACTOME:REACT_264249)
RID: 55700 (;Transport'):
  Reactants: Glycerol (annotations: CHEBI:CHEBI:17754)
  Products: Glycerol (annotations: CHEBI:CHEBI:17754)
  Modifiers: AQP9 (annotations: HGNC:643,HGNC_SYMBOL:AQP9,UNIPROT:O43315,REFSEQ:NM_020980,PUBMED:19096781,ENTREZ:366,)
  (References: PUBMED:19096781)
RID: 55672 (;Negative influence'):
  Reactants: PKLR (annotations: HGNC_SYMBOL:PKLR,REFSEQ:NM_000298,HGNC:9020,UNIPROT:P30613,ENTREZ:5313,)
  Products: Glycolysis (annotations: GO:GO:0061621)
  Modifiers: None
RID: 55135 (;Heterodimer association'):
  Reactants: Long-chain Fatty Acids (annotations: CHEBI:CHEBI:15904); Fatty acid binding protein (annotations: PUBMED:18477307)
  Products: FABP:LCFA
  Modifiers: None
  (References: WIKIPATHWAYS:WP5061|PUBMED:12856180)
RID: 55082 (;State transition'):
  Reactants: DHA-P
  Products: Glycerol-3-P
  Modifiers: GPD1 (annotations: ,UNIPROT:P21695,HGNC:4455,HGNC_SYMBOL:GPD1,ENTREZ:2819,REFSEQ:NM_001257199); GPD2 (annotations: ENTREZ:2820,HGNC:4456,REFSEQ:NM_000408,,UNIPROT:P43304,HGNC_SYMBOL:GPD2)
RID: 56185 (;State transition'):
  Reactants: Aspartate (annotations: CHEBI:CHEBI:29995,CHEBI:CHEBI:72314); α-Ketogluatarate (annotations: CHEBI:CHEBI:30915)
  Products: Oxalacetate (annotations: CHEBI:CHEBI:16452); Glutamate (annotations: CHEBI:CHEBI:29987,CHEBI:CHEBI:14321,CHEBI:CHEBI:16015,CHEBI:CHEBI:18237)
  Modifiers: GOT1
RID: 55109 (;Transport'):
  Reactants: Long-chain Fatty Acids (annotations: CHEBI:CHEBI:15904)
  Products: Microsomal Omega-Oxidation (annotations: WIKIPATHWAYS:WP206,GO:GO:0010430)
  Modifiers: FABP
RID: 55958 (;Positive influence'):
  Reactants: G6PC (annotations: PUBMED:28416361,)
  Products: Gluconeogenesis (annotations: GO:GO:0006094)
  Modifiers: None
RID: 55202 (;State transition'):
  Reactants: FF-MAS (annotations: CHEBI:CHEBI:17813)
  Products: T-MAS (annotations: CHEBI:CHEBI:18364)
  Modifiers: TM7SF2 (annotations: ,HGNC:11863,REFSEQ:NM_003273,UNIPROT:O76062,ENTREZ:7108,HGNC_SYMBOL:TM7SF2); LBR (annotations: HGNC_SYMBOL:LBR,UNIPROT:Q14739,REFSEQ:NM_002296,HGNC:6518,ENTREZ:3930,)
  (References: WIKIPATHWAYS:WP4718|DOI:10.1016/B978-0-12-824048-9.00005-5)
RID: 55571 (;State transition'):
  Reactants: GYS
  Products: GYS
  Modifiers: GSK3B (annotations: HGNC_SYMBOL:GSK3B,ENTREZ:2932,PUBMED:28416361,,HGNC:4617,UNIPROT:P49841,REFSEQ:NM_001146156)
RID: 55215 (;Positive influence'):
  Reactants: Cholesterol (annotations: CHEBI:CHEBI:16113,KEGG_COMPOUND:C00187)
  Products: Bile (annotations: GO:GO:0006699)
  Modifiers: None
RID: 55678 (;Transport'):
  Reactants: α-Ketogluatarate (annotations: CHEBI:CHEBI:30915)
  Products: α-Ketogluatarate (annotations: CHEBI:CHEBI:30915)
  Modifiers: GLAST1
RID: 55596 (;Heterodimer association'):
  Reactants: INS (formerSymbols: IDDM1,IDDM2) (annotations: HGNC_SYMBOL:INS,PUBMED:28416361,HGNC:6081,PUBMED:24692138,REFSEQ:NM_000207,ENTREZ:3630,,UNIPROT:P01308); INSR (annotations: REFSEQ:NM_000188,,HGNC_SYMBOL:HK1,UNIPROT:P19367,,PUBMED:28416361,HGNC:4922,ENTREZ:3098)
  Products: INSR:INS (annotations: REFSEQ:NM_000189,HGNC_SYMBOL:HK2,UNIPROT:P52789,ENTREZ:3099,HGNC:4923,)
  Modifiers: None
RID: 55570 (;Positive influence'):
  Reactants: NR1H4 (annotations: ,ENTREZ:9971,HGNC:7967,UNIPROT:Q96RI1,REFSEQ:NM_005123,HGNC_SYMBOL:NR1H4)
  Products: PPARA (formerSymbols: PPAR) (annotations: HGNC_SYMBOL:PPARA,ENTREZ:5465,REFSEQ:NM_001001928,,PUBMED:26451809,UNIPROT:Q07869,HGNC:9232)
  Modifiers: None
RID: 55157 (;Transcription'):
  Reactants: ACSL1 (formerSymbols: FACL2) (annotations: ENTREZ:2180,HGNC:3569,REFSEQ:NM_001995,UNIPROT:P33121,HGNC_SYMBOL:ACSL1,)
  Products: ACSL1 (formerSymbols: FACL2) (annotations: ENTREZ:2180,HGNC:3569,REFSEQ:NM_001995,UNIPROT:P33121,HGNC_SYMBOL:ACSL1,)
  Modifiers: SREBF2 (annotations: HGNC:11290,REFSEQ:NM_004599,UNIPROT:Q12772,,HGNC_SYMBOL:SREBF2,ENTREZ:6721)
  (References: WIKIPATHWAYS:WP4718)
RID: 55516 (;Positive influence'):
  Reactants: mTORC1 (annotations: GO:GO:0031931)
  Products: Cell Growth (annotations: GO:GO:0016049)
  Modifiers: None
RID: 55436 (;State transition'):
  Reactants:  ; ACAD9 (annotations: ENTREZ:28976,REFSEQ:NM_014049,EC:1.3.8.-,,HGNC:21497,HGNC_SYMBOL:ACAD9,UNIPROT:Q9H845); ECSIT (annotations: UNIPROT:Q9BQ95,,HGNC:29548,HGNC_SYMBOL:ECSIT,REFSEQ:NM_016581,ENTREZ:51295); NDUFAF7 (formerSymbols: C2orf56) (annotations: ,HGNC_SYMBOL:NDUFAF7,EC:2.1.1.320,HGNC:28816,ENTREZ:55471,UNIPROT:Q7L592,REFSEQ:NM_144736)
  Products: OXPHOS factors (annotations: PUBMED:23149385,PUBMED:30030361)
  Modifiers: None
  (References: PUBMED:23149385|TAXONOMY:10090|PUBMED:30030361)
RID: 55114 (;Known transition omitted'):
  Reactants: HDL (annotations: GO:GO:0034364)
  Products: VLDL (annotations: GO:GO:0034361)
  Modifiers: None
  (References: WIKIPATHWAYS:WP5304)
RID: 55352 (;State transition'):
  Reactants: palmitoyl-CoA (annotations: REACTOME:REACT_11391.1,CHEMSPIDER:14902,PUBCHEM:15667,HMDB:HMDB0001338,KEGG_COMPOUND:C00154,CHEBI:CHEBI:15525,WIKIPEDIA:palmitoyl CoA,CAS:1763-10-6); carnitine (annotations: CHEBI:CHEBI:17126,REACTOME:REACT_11423.1)
  Products: L-palmitoylcarnitine (annotations: PUBCHEM:11953816,CHEBI:CHEBI:17490,HMDB:HMDB0000222,CAS:2364-67-2,REACTOME:REACT_11789.2,KEGG_COMPOUND:C02990,CHEMSPIDER:10128117)
  Modifiers: CPT1A (formerSymbols: CPT1) (annotations: UNIPROT:P50416,HGNC_SYMBOL:CPT1A,HGNC:2328,ENTREZ:1374,REFSEQ:NM_001876,); CPT1B (annotations: UNIPROT:Q92523,,REFSEQ:NM_152246,HGNC_SYMBOL:CPT1B,HGNC:2329,ENTREZ:1375); malonyl-CoA (annotations: REACTOME:REACT_3059.1,WIKIPEDIA:Malonyl-CoA,HMDB:HMDB0001175,CAS:524-14-1,CHEBI:CHEBI:15531,PUBCHEM:10663,KEGG_COMPOUND:C00083,CHEMSPIDER:10213)
  (References: REACTOME:REACT_11185.4)
RID: 56003 (;State transition'):
  Reactants: Fibulose-5-Phosphate
  Products: Ribose-5-Phosphate (annotations: CHEBI:CHEBI:78679)
  Modifiers: RPIA (annotations: ,REFSEQ:NM_144563,HGNC:10297,HGNC_SYMBOL:RPIA,ENTREZ:22934,UNIPROT:P49247)
RID: 55357 (;Transport'):
  Reactants: e-
  Products: e-
  Modifiers: CYCS (annotations: HGNC:19986,UNIPROT:P99999,ENTREZ:54205,HGNC_SYMBOL:CYCS,,REFSEQ:NM_018947)
RID: 55729 (;Positive influence'):
  Reactants: AHR (annotations: HGNC:348,HGNC_SYMBOL:AHR,,UNIPROT:P35869,REFSEQ:NM_001621,ENTREZ:196)
  Products: LDLR (annotations: HGNC_SYMBOL:LDLR,HGNC:6547,,ENTREZ:3949,REFSEQ:NM_000527,UNIPROT:P01130)
  Modifiers: None
RID: 56188 (;State transition'):
  Reactants: PYGL
  Products: PYGL
  Modifiers: None
RID: 56150 (;State transition'):
  Reactants: UDP-Galactose (annotations: CHEBI:CHEBI:67119)
  Products: UDP-Glucose (annotations: CHEBI:CHEBI:18066)
  Modifiers: GALE (annotations: HGNC_SYMBOL:GALE,UNIPROT:Q14376,HGNC:4116,ENTREZ:2582,REFSEQ:NM_000403,)
RID: 55459 (PDmap:re357.0;State transition'):
  Reactants: (5-hydroxyindol-3-yl)acetaldehyde (annotations: REACTOME:REACT_17970.1,CHEBI:CHEBI:50157,HMDB:HMDB0004073,KEGG_COMPOUND:C05634,CAS:1892-21-3,PUBCHEM:74688,CHEMSPIDER:67261)
  Products: (5-hydroxyindol-3-yl)acetic acid (annotations: REACTOME:REACT_17511.1,CAS:54-16-0,KEGG_COMPOUND:C05635,PUBCHEM:1826,WIKIPEDIA:5-Hydroxyindoleacetic acid,HMDB:HMDB0000763,CHEMSPIDER:1760,CHEBI:CHEBI:27823,CHEMBL_COMPOUND:CHEMBL395915)
  Modifiers: ALDH2 (annotations: HGNC_SYMBOL:ALDH2,ENTREZ:217,,REFSEQ:NM_000690,HGNC:404,UNIPROT:P05091)
  (References: REACTOME:REACT_15407.2|PUBMED:17010132|PUBMED:8778744)
RID: 56029 (;Positive influence'):
  Reactants: Fatty Acids
  Products: HNF4A (formerSymbols: MODY,MODY1,TCF14) (annotations: ,HGNC:5024,ENTREZ:3172,UNIPROT:P41235,HGNC_SYMBOL:HNF4A,REFSEQ:NM_000457)
  Modifiers: None
RID: 55790 (;Negative influence'):
  Reactants: NR1I3 (annotations: ENTREZ:9970,UNIPROT:Q14994,,HGNC:7969,REFSEQ:NM_001077469,HGNC_SYMBOL:NR1I3)
  Products: FOXA2 (formerSymbols: HNF3B) (annotations: ENTREZ:3170,HGNC_SYMBOL:FOXA2,UNIPROT:Q9Y261,REFSEQ:NM_021784,,HGNC:5022)
  Modifiers: None
RID: 55228 (;State transition'):
  Reactants: NR1H3 (annotations: REFSEQ:NM_001130101,,HGNC:7966,ENTREZ:10062,UNIPROT:Q13133,HGNC_SYMBOL:NR1H3)
  Products: NR1H3 (annotations: REFSEQ:NM_001130101,,HGNC:7966,ENTREZ:10062,UNIPROT:Q13133,HGNC_SYMBOL:NR1H3)
  Modifiers: Desmosterol (annotations: CHEBI:CHEBI:17737); 25-hydroxycholesterol
  (References: WIKIPATHWAYS:WP4718|DOI:10.1016/B978-0-12-824048-9.00005-5)
RID: 55808 (;Positive influence'):
  Reactants: HSD17B10 (formerSymbols: HADH2,MRXS10) (annotations: HGNC_SYMBOL:HSD17B10,,UNIPROT:Q99714,REFSEQ:NM_004493,HGNC:4800,ENTREZ:3028)
  Products: Mitochondrial Beta-Oxidation (annotations: WIKIPATHWAYS:WP143)
  Modifiers: None
RID: 55744 (;Positive influence'):
  Reactants: G6PC (annotations: PUBMED:28416361,)
  Products: Gluconeogenesis (annotations: GO:GO:0006094)
  Modifiers: None
RID: 55470 (;Positive influence'):
  Reactants: FOXO1 (formerSymbols: FKHR,FOXO1A) (annotations: HGNC:3819,,REFSEQ:NM_002015,ENTREZ:2308,PUBMED:28416361,HGNC_SYMBOL:FOXO1,UNIPROT:Q12778)
  Products: PCK1 (annotations: ,PUBMED:28416361,HGNC:8724,UNIPROT:P35558,HGNC_SYMBOL:PCK1,REFSEQ:NM_002591,ENTREZ:5105)
  Modifiers: None
RID: 55455 (;State transition'):
  Reactants: peroxynitrite (annotations: CHEBI:CHEBI:25941); TXN (annotations: ENTREZ:7295,UNIPROT:P10599,HGNC:12435,,REFSEQ:NM_001244938,HGNC_SYMBOL:TXN)
  Products: nitrite (annotations: CAS:14797-65-0,HMDB:HMDB0002786,WIKIPEDIA:Nitrite,PUBCHEM:946,CHEMSPIDER:921,KEGG_COMPOUND:C00088,CHEBI:CHEBI:16301); H2O (annotations: HMDB:HMDB0002111,CHEBI:CHEBI:15377,PUBCHEM:962,CHEMSPIDER:937,MESH_2012:D014867,WIKIPEDIA:Water,CAS:7732-18-5,CHEMBL_COMPOUND:CHEMBL1098659,KEGG_COMPOUND:C00001); TXN (annotations: ENTREZ:7295,UNIPROT:P10599,HGNC:12435,,REFSEQ:NM_001244938,HGNC_SYMBOL:TXN)
  Modifiers: PRDX5 (annotations: UNIPROT:P30044,REFSEQ:NM_181651,,HGNC_SYMBOL:PRDX5,HGNC:9355,ENTREZ:25824)
  (References: REACTOME:REACT_264249)
RID: 55328 (PDmap:re569.0;State transition'):
  Reactants: 1,2-diacyl-sn-glycerol 3-phosphate (annotations: REACTOME:REACT_3539.3,CHEBI:CHEBI:29089)
  Products: 1,2-diacyl-sn-glycerol (annotations: CHEBI:CHEBI:17815,REACTOME:REACT_4481.3)
  Modifiers: LPIN1 (annotations: UNIPROT:Q14693,,ENTREZ:23175,REFSEQ:NM_145693,HGNC_SYMBOL:LPIN1,HGNC:13345); LPIN2 (annotations: HGNC:14450,ENTREZ:9663,HGNC_SYMBOL:LPIN2,UNIPROT:Q92539,REFSEQ:NM_014646,); LPIN3 (formerSymbols: LIPN3L) (annotations: HGNC:14451,UNIPROT:Q9BQK8,ENTREZ:64900,,REFSEQ:NM_022896,HGNC_SYMBOL:LPIN3)
  (References: PUBMED:18694939|PUBMED:17158099|REACTOME:REACT_395.3)
RID: 55713 (;Known transition omitted'):
  Reactants: VLDL
  Products: IDL
  Modifiers: None
RID: 55711 (;Positive influence'):
  Reactants: PPARA (formerSymbols: PPAR) (annotations: HGNC_SYMBOL:PPARA,ENTREZ:5465,REFSEQ:NM_001001928,,PUBMED:26451809,UNIPROT:Q07869,HGNC:9232)
  Products: CPT1A (formerSymbols: CPT1) (annotations: UNIPROT:P50416,PUBMED:19595610,HGNC_SYMBOL:CPT1A,HGNC:2328,ENTREZ:1374,REFSEQ:NM_001876,)
  Modifiers: None
RID: 55198 (;State transition'):
  Reactants: LNSOL (annotations: CHEBI:CHEBI:16521)
  Products: FF-MAS (annotations: CHEBI:CHEBI:17813)
  Modifiers: CYP51A1 (formerSymbols: CYP51) (annotations: UNIPROT:Q16850,,HGNC_SYMBOL:CYP51A1,ENTREZ:1595,HGNC:2649,REFSEQ:NM_000786)
  (References: WIKIPATHWAYS:WP4718|DOI:10.1016/B978-0-12-824048-9.00005-5)
RID: 55338 (PDmap:re535.0;State transition'):
  Reactants: crotonoyl-CoA (annotations: KEGG_COMPOUND:C00877,REACTOME:REACT_5111.1,CHEBI:CHEBI:15473,HMDB:HMDB0002009,PUBCHEM:5280381,CAS:102680-35-3,CHEMSPIDER:4444072,WIKIPEDIA:Crotonyl-coenzyme A)
  Products: (S)-3-hydroxybutanoyl-CoA (annotations: CHEBI:CHEBI:15453,REACTOME:REACT_4099.1)
  Modifiers: ECHS1 (annotations: HGNC_SYMBOL:ECHS1,,ENTREZ:1892,UNIPROT:P30084,HGNC:3151,REFSEQ:NM_004092)
  (References: REACTOME:REACT_386.2|PUBMED:13295248)
RID: 55733 (;Positive influence'):
  Reactants: PPARG (annotations: HGNC:9236,REFSEQ:NM_005037,HGNC_SYMBOL:PPARG,UNIPROT:P37231,,ENTREZ:5468)
  Products: CD36 (annotations: HGNC:1663,REFSEQ:NM_001001547,HGNC_SYMBOL:CD36,PUBMED:26451809,ENTREZ:948,,UNIPROT:P16671,PUBMED:18477307)
  Modifiers: None
RID: 56155 (;State transition'):
  Reactants: Glycerol (annotations: CHEBI:CHEBI:17754)
  Products: Glycerol-3-Phosphate (annotations: CHEBI:CHEBI:15978)
  Modifiers: GK (annotations: ENTREZ:2710,HGNC:4289,REFSEQ:NM_000167,UNIPROT:P32189,HGNC_SYMBOL:GK,)
RID: 55727 (;Positive influence'):
  Reactants: CREB1 (annotations: REFSEQ:NM_134442,HGNC:2345,ENTREZ:1385,HGNC_SYMBOL:CREB1,UNIPROT:P16220,)
  Products: PPARGC1A (formerSymbols: PPARGC1) (annotations: UNIPROT:Q9UBK2,ENTREZ:10891,HGNC:9237,HGNC_SYMBOL:PPARGC1A,,REFSEQ:NM_013261)
  Modifiers: None
RID: 55669 (;Known transition omitted'):
  Reactants: FOXO1 (formerSymbols: FKHR,FOXO1A) (annotations: HGNC:3819,,REFSEQ:NM_002015,ENTREZ:2308,HGNC_SYMBOL:FOXO1,UNIPROT:Q12778)
  Products: FOXO1 (formerSymbols: FKHR,FOXO1A) (annotations: HGNC:3819,,REFSEQ:NM_002015,ENTREZ:2308,PUBMED:28416361,HGNC_SYMBOL:FOXO1,UNIPROT:Q12778)
  Modifiers: None
RID: 55221 (;Known transition omitted'):
  Reactants: 27-hydroxycholesterol (annotations: CHEBI:CHEBI:17703)
  Products: Bile (annotations: GO:GO:0006699)
  Modifiers: None
RID: 56063 (;Known transition omitted'):
  Reactants: 3-Phospho-Hydroxy-Pyruvate (annotations: CHEBI:CHEBI:18110); Glutamate (annotations: CHEBI:CHEBI:29987,CHEBI:CHEBI:14321,CHEBI:CHEBI:16015,CHEBI:CHEBI:18237)
  Products: 3-Phosphoserine (annotations: CHEBI:CHEBI:15811); α-Ketogluatarate (annotations: CHEBI:CHEBI:30915)
  Modifiers: PSAT1 (annotations: REFSEQ:NM_021154,HGNC:19129,UNIPROT:Q9Y617,,ENTREZ:29968,HGNC_SYMBOL:PSAT1)
RID: 55206 (;State transition'):
  Reactants: Desmosterol (annotations: CHEBI:CHEBI:17737)
  Products: Cholesterol (annotations: CHEBI:CHEBI:16113,KEGG_COMPOUND:C00187)
  Modifiers: DHCR24 (formerSymbols: DCE) (annotations: REFSEQ:NM_014762,HGNC_SYMBOL:DHCR24,,ENTREZ:1718,UNIPROT:Q15392,HGNC:2859)
  (References: WIKIPATHWAYS:WP4718|DOI:10.1016/B978-0-12-824048-9.00005-5)
RID: 55983 (;State transition'):
  Reactants: (S)-Hydroxydecanoyl-CoA (annotations: CHEBI:CHEBI:28325)
  Products: 3-Oxodecanoyl-CoA  (annotations: CHEBI:CHEBI:28528,CHEBI:CHEBI:62548)
  Modifiers: HADH (formerSymbols: HADHSC) (annotations: HGNC_SYMBOL:HADH,REFSEQ:NM_005327,,HGNC:4799,ENTREZ:3033,UNIPROT:Q16836)
RID: 55517 (;Positive influence'):
  Reactants: G6PC (annotations: PUBMED:28416361,)
  Products: Gluconeogenesis (annotations: GO:GO:0006094)
  Modifiers: None
RID: 55560 (;Heterodimer association'):
  Reactants: PPARGC1A (formerSymbols: PPARGC1) (annotations: UNIPROT:Q9UBK2,ENTREZ:10891,HGNC:9237,HGNC_SYMBOL:PPARGC1A,,REFSEQ:NM_013261); PPARG (annotations: HGNC:9236,REFSEQ:NM_005037,HGNC_SYMBOL:PPARG,UNIPROT:P37231,,ENTREZ:5468)
  Products: PPARG:PPARGC1A
  Modifiers: None
RID: 55841 (;Positive influence'):
  Reactants: AKT1 (annotations: ENTREZ:207,HGNC:391,PUBMED:28416361,HGNC_SYMBOL:AKT1,REFSEQ:NM_005163,UNIPROT:P31749,)
  Products: RPS6KB2 (annotations: REFSEQ:NM_003952,HGNC:10437,ENTREZ:6199,,UNIPROT:Q9UBS0,HGNC_SYMBOL:RPS6KB2)
  Modifiers: None
RID: 55850 (;Transport'):
  Reactants: Glucose (annotations: CHEBI:CHEBI:42758,CHEBI:CHEBI:4167,CHEBI:CHEBI:17234)
  Products: Glucose (annotations: CHEBI:CHEBI:42758,CHEBI:CHEBI:4167,CHEBI:CHEBI:17234)
  Modifiers: SLC2A2 (formerSymbols: GLUT2) (annotations: HGNC_SYMBOL:SLC2A2,HGNC:11006,UNIPROT:P11168,REFSEQ:NM_000340,ENTREZ:6514,PUBMED:32591906,)
  (References: PUBMED:32591906)
RID: 55379 (;Known transition omitted'):
  Reactants: SOD3:Cu2+:Zn2+
  Products: SOD3:Cu2+:Zn2+
  Modifiers: None
  (References: REACTOME:REACT_264249)
RID: 55251 (PDmap:re361.0;State transition'):
  Reactants: ADP (annotations: HMDB:HMDB0001341,WIKIPEDIA:ADP,CAS:58-64-0,KEGG_COMPOUND:C00008,PUBCHEM:6022,CHEBI:CHEBI:16761,CHEMBL_COMPOUND:CHEMBL14830,CHEMSPIDER:5800); H+ (annotations: CHEBI:CHEBI:15378); Pi (annotations: CHEBI:CHEBI:18367)
  Products: ATP (annotations: CHEBI:CHEBI:15422,PUBCHEM:5957,CAS:56-65-5,MESH_2012:D000255,CHEMBL_COMPOUND:CHEMBL14249,CHEMSPIDER:5742,WIKIPEDIA:Adenosine triphosphate,HMDB:HMDB0000538,KEGG_COMPOUND:C00002); H+ (annotations: CHEBI:CHEBI:15378)
  Modifiers: ATP synthase (complex V) (annotations: GO:GO:0005753)
  (References: PUBMED:19427899|PUBMED:15734681)
RID: 55832 (;State transition'):
  Reactants: (R)-methylmalonyl-CoA (annotations: CHEBI:CHEBI:15465,CHEBI:CHEBI:57326)
  Products: Succinyl-CoA (annotations: CHEBI:CHEBI:15380,CHEBI:CHEBI:57292)
  Modifiers: MMAA:MMUT
RID: 55465 (;Heterodimer association'):
  Reactants: INS (formerSymbols: IDDM1,IDDM2) (annotations: HGNC_SYMBOL:INS,PUBMED:28416361,HGNC:6081,PUBMED:24692138,REFSEQ:NM_000207,ENTREZ:3630,,UNIPROT:P01308); INSR (annotations: ,HGNC:6091,UNIPROT:P06213,PUBMED:28416361,HGNC_SYMBOL:INSR,REFSEQ:NM_000208,ENTREZ:3643)
  Products: INSR:INS
  Modifiers: None
RID: 55205 (;Known transition omitted'):
  Reactants: MYLIP (annotations: REFSEQ:NM_013262,ENTREZ:29116,UNIPROT:Q8WY64,HGNC:21155,HGNC_SYMBOL:MYLIP,)
  Products: LDLR degradation (annotations: GO:GO:0032803)
  Modifiers: None
  (References: WIKIPATHWAYS:WP4718)
RID: 55642 (;State transition'):
  Reactants: AKT1 (annotations: ENTREZ:207,HGNC:391,PUBMED:28416361,HGNC_SYMBOL:AKT1,REFSEQ:NM_005163,UNIPROT:P31749,)
  Products: AKT1 (annotations: ENTREZ:207,HGNC:391,PUBMED:28416361,HGNC_SYMBOL:AKT1,REFSEQ:NM_005163,UNIPROT:P31749,)
  Modifiers: None
RID: 55472 (;Positive influence'):
  Reactants: RPS6KB2 (annotations: REFSEQ:NM_003952,HGNC:10437,ENTREZ:6199,,UNIPROT:Q9UBS0,HGNC_SYMBOL:RPS6KB2)
  Products: Cell Growth (annotations: GO:GO:0016049)
  Modifiers: None
RID: 55406 (PDmap:re377.0;State transition'):
  Reactants: pyruvate dehydrogenase complex (annotations: REACTOME:REACT_5500.1,GO:GO:0005967); H2O (annotations: HMDB:HMDB0002111,CHEBI:CHEBI:15377,PUBCHEM:962,CHEMSPIDER:937,MESH_2012:D014867,WIKIPEDIA:Water,CAS:7732-18-5,CHEMBL_COMPOUND:CHEMBL1098659,KEGG_COMPOUND:C00001)
  Products: pyruvate dehydrogenase complex (annotations: REACTOME:REACT_5500.1,GO:GO:0005967); phosphate(3-) (annotations: WIKIPEDIA:Phosphate,PUBCHEM:1061,CAS:14265-44-2,KEGG_COMPOUND:C00009,CHEMSPIDER:1032,CHEBI:CHEBI:18367,REACTOME:REACT_5781.1,HMDB:HMDB0001429)
  Modifiers: PDP1:PDPR; Ca2+ (annotations: CHEBI:CHEBI:29108); Mg2+ (annotations: REACTOME:REACT_5401.1,CHEBI:CHEBI:18420)
  (References: PUBMED:9395502|PUBMED:15855260|PUBMED:12676647|PUBMED:20144582|REACTOME:REACT_12543.2|PUBMED:17532339|PUBMED:9651365|PUBMED:2479373)
RID: 55252 (;State transition'):
  Reactants: acetyl-CoA (annotations: CHEBI:CHEBI:15351,WIKIPEDIA:Acetyl-CoA,HMDB:HMDB0001206,CHEMSPIDER:392413,PUBCHEM:444493,REACTOME:REACT_3839.1,CAS:72-89-9,KEGG_COMPOUND:C00024)
  Products: acetyl-ACP (annotations: CHEBI:CHEBI:17093)
  Modifiers: FASN (annotations: HGNC:3594,UNIPROT:P49327,REFSEQ:NM_004104,,ENTREZ:2194,HGNC_SYMBOL:FASN)
  (References: WIKIPATHWAYS:WP357)
RID: 55715 (;State transition'):
  Reactants: Aconitate (annotations: CHEBI:CHEBI:22210)
  Products: Isocitrate (annotations: CHEBI:CHEBI:16087)
  Modifiers: ACO
RID: 55926 (;Positive influence'):
  Reactants: G6PC (annotations: PUBMED:28416361,)
  Products: Gluconeogenesis (annotations: GO:GO:0006094)
  Modifiers: None
RID: 55709 (;Positive influence'):
  Reactants: CDKN1B (annotations: ENTREZ:1027,,,UNIPROT:P46527,HGNC:1785,REFSEQ:NM_004064,HGNC_SYMBOL:CDKN1B)
  Products: Cell Proliferation (annotations: GO:GO:0072574)
  Modifiers: None
RID: 55528 (;Positive influence'):
  Reactants: G6PC (annotations: PUBMED:28416361,)
  Products: Gluconeogenesis
  Modifiers: None
RID: 55095 (;Transport'):
  Reactants: Triacylglycerol (annotations: CHEBI:CHEBI:17855)
  Products: Triacylglycerol (annotations: CHEBI:CHEBI:17855)
  Modifiers: MTTP (formerSymbols: MTP) (annotations: HGNC:7467,REFSEQ:NM_000253,ENTREZ:4547,HGNC_SYMBOL:MTTP,,WIKIPATHWAYS:WP430,UNIPROT:P55157,PUBMED:18477307)
  (References: PUBMED:18477307)
RID: 56028 (;Known transition omitted'):
  Reactants: PPARG (annotations: HGNC:9236,REFSEQ:NM_005037,HGNC_SYMBOL:PPARG,UNIPROT:P37231,ENTREZ:5468,)
  Products: PPARG (annotations: HGNC:9236,REFSEQ:NM_005037,HGNC_SYMBOL:PPARG,UNIPROT:P37231,,ENTREZ:5468)
  Modifiers: None
RID: 55084 (;State transition'):
  Reactants: DAG
  Products: Triacylglycerol
  Modifiers: DGAT
RID: 55323 (;Unknown transition'):
  Reactants: butyryl-ACP (annotations: CHEBI:CHEBI:3247)
  Products: palmitoyl-CoA (annotations: REACTOME:REACT_11391.1,CHEMSPIDER:14902,PUBCHEM:15667,HMDB:HMDB0001338,KEGG_COMPOUND:C00154,CHEBI:CHEBI:15525,WIKIPEDIA:palmitoyl CoA,CAS:1763-10-6)
  Modifiers: None
  (References: WIKIPATHWAYS:WP357)
RID: 55960 (;State transition'):
  Reactants: T-MAS (annotations: CHEBI:CHEBI:18364)
  Products: Dihydro-T-MAS (annotations: CHEBI:CHEBI:87044)
  Modifiers: DHCR24 (formerSymbols: DCE) (annotations: REFSEQ:NM_014762,HGNC_SYMBOL:DHCR24,,ENTREZ:1718,UNIPROT:Q15392,HGNC:2859)
  (References: DOI:10.1016/B978-0-12-824048-9.00005-5)
RID: 56038 (;Positive influence'):
  Reactants: AHR (annotations: HGNC:348,HGNC_SYMBOL:AHR,,UNIPROT:P35869,REFSEQ:NM_001621,ENTREZ:196)
  Products: CD36 (annotations: HGNC:1663,REFSEQ:NM_001001547,HGNC_SYMBOL:CD36,PUBMED:26451809,ENTREZ:948,,UNIPROT:P16671,PUBMED:18477307)
  Modifiers: None
RID: 55502 (;State transition'):
  Reactants: AKT1 (annotations: ENTREZ:207,HGNC:391,PUBMED:28416361,HGNC_SYMBOL:AKT1,REFSEQ:NM_005163,UNIPROT:P31749,)
  Products: AKT1 (annotations: ENTREZ:207,HGNC:391,PUBMED:28416361,HGNC_SYMBOL:AKT1,REFSEQ:NM_005163,UNIPROT:P31749,)
  Modifiers: None
RID: 55242 (PDmap:re469.0;State transition'):
  Reactants: (3S)-3-hydroxy-3-methylglutaryl-CoA (annotations: KEGG_COMPOUND:C00356,CHEBI:CHEBI:15467,HMDB:HMDB0001375,CAS:1553-55-5,WIKIPEDIA:3-hydroxy-3-methylglutaryl-CoA,PUBCHEM:439218,CHEMSPIDER:388357)
  Products: acetoacetate (annotations: CAS:541-50-4,CHEBI:CHEBI:15344,CHEMBL_COMPOUND:CHEMBL1230762,WIKIPEDIA:Acetoacetic acid,PUBCHEM:96,REACTOME:REACT_5224.1,CHEMSPIDER:94,HMDB:HMDB0000060,KEGG_COMPOUND:C00164); acetyl-CoA (annotations: CHEBI:CHEBI:15351,WIKIPEDIA:Acetyl-CoA,HMDB:HMDB0001206,CHEMSPIDER:392413,PUBCHEM:444493,REACTOME:REACT_3839.1,CAS:72-89-9,KEGG_COMPOUND:C00024)
  Modifiers: HMGCL (annotations: HGNC:5005,REFSEQ:NM_000191,UNIPROT:P35914,HGNC_SYMBOL:HMGCL,ENTREZ:3155,)
  (References: REACTOME:REACT_2103.4|KEGG_REACTION:R01360)
RID: 55149 (;State transition'):
  Reactants: SQNE (annotations: CHEBI:CHEBI:15440)
  Products: SQOX (annotations: CHEBI:CHEBI:78662)
  Modifiers: SQLE (annotations: HGNC:11279,,UNIPROT:Q14534,HGNC_SYMBOL:SQLE,ENTREZ:6713,REFSEQ:NM_003129)
  (References: WIKIPATHWAYS:WP4718|DOI:10.1016/B978-0-12-824048-9.00005-5)
RID: 55592 (;State transition'):
  Reactants: Aspartate (annotations: CHEBI:CHEBI:29995,CHEBI:CHEBI:72314); α-Ketogluatarate (annotations: CHEBI:CHEBI:30915)
  Products: Oxalacetate (annotations: CHEBI:CHEBI:16452); Glutamate (annotations: CHEBI:CHEBI:29987,CHEBI:CHEBI:14321,CHEBI:CHEBI:16015,CHEBI:CHEBI:18237)
  Modifiers: GOT1 (annotations: UNIPROT:P17174,REFSEQ:NM_002079,HGNC:4432,ENTREZ:2805,HGNC_SYMBOL:GOT1,)
RID: 55486 (;State transition'):
  Reactants: IRS2 (annotations: UNIPROT:Q9Y4H2,HGNC:6126,ENTREZ:8660,HGNC_SYMBOL:IRS2,,REFSEQ:NM_003749)
  Products:  
  Modifiers: None
RID: 55190 (;State transition'):
  Reactants: SREBF1 (annotations: UNIPROT:P36956,REFSEQ:NM_004176,ENTREZ:6720,HGNC:11289,HGNC_SYMBOL:SREBF1,)
  Products: SREBF1 (annotations: UNIPROT:P36956,REFSEQ:NM_004176,ENTREZ:6720,HGNC:11289,HGNC_SYMBOL:SREBF1,)
  Modifiers: Desmosterol (annotations: CHEBI:CHEBI:17737); 25-hydroxycholesterol
  (References: WIKIPATHWAYS:WP4718)
RID: 56127 (;Positive influence'):
  Reactants: HADH (formerSymbols: HADHSC) (annotations: HGNC_SYMBOL:HADH,REFSEQ:NM_005327,,HGNC:4799,ENTREZ:3033,UNIPROT:Q16836)
  Products: Mitochondrial Beta-Oxidation (annotations: WIKIPATHWAYS:WP143)
  Modifiers: None
RID: 55966 (;State transition'):
  Reactants: Desmosterol (annotations: CHEBI:CHEBI:17737)
  Products: Cholesterol (annotations: CHEBI:CHEBI:16113,KEGG_COMPOUND:C00187)
  Modifiers: DHCR24 (formerSymbols: DCE) (annotations: REFSEQ:NM_014762,HGNC_SYMBOL:DHCR24,,ENTREZ:1718,UNIPROT:Q15392,HGNC:2859)
  (References: DOI:10.1016/B978-0-12-824048-9.00005-5)
RID: 55119 (;Transport'):
  Reactants: Phospholipids (annotations: CHEBI:CHEBI:16247)
  Products: Phospholipids (annotations: CHEBI:CHEBI:16247)
  Modifiers: MTTP (formerSymbols: MTP) (annotations: HGNC:7467,REFSEQ:NM_000253,ENTREZ:4547,HGNC_SYMBOL:MTTP,,WIKIPATHWAYS:WP430,UNIPROT:P55157,PUBMED:18477307)
  (References: PUBMED:18477307)
RID: 55336 (PDmap:re513.0;State transition'):
  Reactants: carnitine (annotations: CHEBI:CHEBI:17126,REACTOME:REACT_11423.1); L-palmitoylcarnitine (annotations: PUBCHEM:11953816,CHEBI:CHEBI:17490,HMDB:HMDB0000222,CAS:2364-67-2,REACTOME:REACT_11789.2,KEGG_COMPOUND:C02990,CHEMSPIDER:10128117)
  Products: palmitoyl-CoA (annotations: REACTOME:REACT_11391.1,CHEMSPIDER:14902,PUBCHEM:15667,HMDB:HMDB0001338,KEGG_COMPOUND:C00154,CHEBI:CHEBI:15525,WIKIPEDIA:palmitoyl CoA,CAS:1763-10-6)
  Modifiers: CPT2 (formerSymbols: CPT1) (annotations: HGNC_SYMBOL:CPT2,HGNC:2330,REFSEQ:NM_000098,UNIPROT:P23786,,ENTREZ:1376)
  (References: PUBMED:7711730|REACTOME:REACT_11133.3)
RID: 56175 (;State transition'):
  Reactants: Glyceralaldehyde-3-Phosphate (annotations: CHEBI:CHEBI:17138)
  Products: 1,3-Bisphosphoglycerate (annotations: CHEBI:CHEBI:89363)
  Modifiers: GAPDH (formerSymbols: GAPD) (annotations: REFSEQ:NM_002046,HGNC_SYMBOL:GAPDH,,ENTREZ:2597,UNIPROT:P04406,HGNC:4141)
  (References: WIKIPATHWAYS:WP534)
RID: 55947 (;State transition'):
  Reactants: Mevalonate-P (annotations: CHEBI:CHEBI:25350)
  Products: Mevalonate-PP (annotations: CHEBI:CHEBI:25350)
  Modifiers: PMVK (annotations: HGNC_SYMBOL:PMVK,REFSEQ:NM_006556,UNIPROT:Q15126,,HGNC:9141,ENTREZ:10654)
  (References: DOI:10.1016/B978-0-12-824048-9.00005-5)
RID: 55922 (;State transition'):
  Reactants: Mevalonate-PP (annotations: CHEBI:CHEBI:25350)
  Products: Isopentenyl diphosphate (annotations: CHEBI:CHEBI:16584)
  Modifiers: MVD (annotations: HGNC_SYMBOL:MVD,REFSEQ:NM_002461,UNIPROT:P53602,ENTREZ:4597,,HGNC:7529)
  (References: DOI:10.1016/B978-0-12-824048-9.00005-5)
RID: 55575 (;State transition'):
  Reactants: SREBF1 (annotations: PUBMED:28416361,UNIPROT:P36956,REFSEQ:NM_004176,ENTREZ:6720,HGNC:11289,HGNC_SYMBOL:SREBF1,)
  Products: SREBF1 (annotations: PUBMED:28416361,UNIPROT:P36956,REFSEQ:NM_004176,ENTREZ:6720,HGNC:11289,HGNC_SYMBOL:SREBF1,)
  Modifiers: mTORC1 (annotations: GO:GO:0031931)
RID: 55392 (PDmap:re238.0;Positive influence'):
  Reactants: H+ (annotations: CHEBI:CHEBI:15378)
  Products: H+ (annotations: CHEBI:CHEBI:15378)
  Modifiers: None
  (References: PUBMED:19427899)
RID: 55714 (;Positive influence'):
  Reactants: PPARA (formerSymbols: PPAR) (annotations: HGNC_SYMBOL:PPARA,ENTREZ:5465,REFSEQ:NM_001001928,,PUBMED:26451809,UNIPROT:Q07869,HGNC:9232)
  Products: CPT2 (formerSymbols: CPT1) (annotations: HGNC_SYMBOL:CPT2,PUBMED:19595610,HGNC:2330,REFSEQ:NM_000098,UNIPROT:P23786,,ENTREZ:1376)
  Modifiers: None
RID: 55201 (;Transcription'):
  Reactants: FASN (annotations: HGNC:3594,UNIPROT:P49327,REFSEQ:NM_004104,,ENTREZ:2194,HGNC_SYMBOL:FASN)
  Products: FASN (annotations: HGNC:3594,UNIPROT:P49327,REFSEQ:NM_004104,,ENTREZ:2194,HGNC_SYMBOL:FASN)
  Modifiers: SREBF2 (annotations: HGNC:11290,REFSEQ:NM_004599,UNIPROT:Q12772,,HGNC_SYMBOL:SREBF2,ENTREZ:6721)
  (References: WIKIPATHWAYS:WP4718)
RID: 55961 (;Positive influence'):
  Reactants: AKT1 (annotations: ENTREZ:207,HGNC:391,PUBMED:28416361,HGNC_SYMBOL:AKT1,REFSEQ:NM_005163,UNIPROT:P31749,)
  Products: CDKN1B (annotations: ENTREZ:1027,,,UNIPROT:P46527,HGNC:1785,REFSEQ:NM_004064,HGNC_SYMBOL:CDKN1B)
  Modifiers: None
RID: 55826 (;Positive influence'):
  Reactants: CPT1
  Products: Beta-Oxidation
  Modifiers: None
RID: 55806 (;Positive influence'):
  Reactants: GYS
  Products: Glycogen Synthesis (annotations: GO:GO:0005978,PUBMED:28416361)
  Modifiers: None
RID: 55902 (;Positive influence'):
  Reactants: PPARA (formerSymbols: PPAR) (annotations: HGNC_SYMBOL:PPARA,ENTREZ:5465,REFSEQ:NM_001001928,,PUBMED:26451809,UNIPROT:Q07869,HGNC:9232)
  Products: CYP7A1 (formerSymbols: CYP7) (annotations: HGNC:2651,,REFSEQ:NM_000780,ENTREZ:1581,HGNC_SYMBOL:CYP7A1,UNIPROT:P22680)
  Modifiers: None
RID: 55542 (;Negative influence'):
  Reactants: PFKFB
  Products: Glycolysis
  Modifiers: None
RID: 55640 (;State transition'):
  Reactants: Fructose-1,6-Bisphosphate (annotations: CHEBI:CHEBI:78682)
  Products: Fructose-6-Phosphate (annotations: CHEBI:CHEBI:15946,CHEBI:CHEBI:16084)
  Modifiers: FBP1 (formerSymbols: FBP) (annotations: HGNC_SYMBOL:FBP1,UNIPROT:P09467,REFSEQ:NM_000507,PUBMED:31284506,HGNC:3606,ENTREZ:2203,)
RID: 55490 (;Positive influence'):
  Reactants: RPS6KB1 (formerSymbols: STK14A) (annotations: HGNC:10436,UNIPROT:P23443,ENTREZ:6198,,HGNC_SYMBOL:RPS6KB1,REFSEQ:NM_003161)
  Products: Translation (annotations: GO:GO:0006412)
  Modifiers: None
RID: 55167 (;Known transition omitted'):
  Reactants: ACOT1 (annotations: UNIPROT:Q86TX2,REFSEQ:NM_001037161,ENTREZ:641371,HGNC:33128,,HGNC_SYMBOL:ACOT1)
  Products: Fatty Acid Biosynthesis (annotations: WIKIPATHWAYS:WP4491,GO:GO:0006633)
  Modifiers: None
RID: 55146 (;Translation'):
  Reactants: HMGCS1 (formerSymbols: HMGCS) (annotations: UNIPROT:Q01581,HGNC:5007,HGNC_SYMBOL:HMGCS1,,ENTREZ:3157,REFSEQ:NM_001098272)
  Products: HMGCS1 (formerSymbols: HMGCS) (annotations: UNIPROT:Q01581,HGNC:5007,HGNC_SYMBOL:HMGCS1,,ENTREZ:3157,REFSEQ:NM_001098272)
  Modifiers: None
RID: 55414 (;Positive influence'):
  Reactants: SLC25A11 (formerSymbols: SLC20A4) (annotations: REFSEQ:NM_003562,HGNC:10981,ENTREZ:8402,UNIPROT:Q02978,HGNC_SYMBOL:SLC25A11,)
  Products: malate-aspartate shuttle (annotations: GO:GO:0043490)
  Modifiers: None
  (References: PUBMED:23986233|PUBMED:25809592|PUBMED:23216354|PUBMED:16368075)
RID: 55854 (;State transition'):
  Reactants: Oxalacetate (annotations: CHEBI:CHEBI:16452)
  Products: Phosphoenolpyruvate (annotations: CHEBI:CHEBI:18021,CHEBI:CHEBI:44897,CHEBI:CHEBI:58702)
  Modifiers: PCK
RID: 55550 (;State transition'):
  Reactants: FBP1 (formerSymbols: FBP) (annotations: HGNC_SYMBOL:FBP1,UNIPROT:P09467,REFSEQ:NM_000507,PUBMED:31284506,HGNC:3606,ENTREZ:2203,)
  Products: FBP1 (formerSymbols: FBP) (annotations: HGNC_SYMBOL:FBP1,UNIPROT:P09467,REFSEQ:NM_000507,PUBMED:31284506,HGNC:3606,ENTREZ:2203,)
  Modifiers: PKA
RID: 55959 (;State transition'):
  Reactants: Unsaturated Fatty Acids
  Products: Fatty acyl-CoA
  Modifiers: ACSL
RID: 55116 (;Transport'):
  Reactants: Long-chain Fatty Acids (annotations: CHEBI:CHEBI:15904)
  Products: Long-chain Fatty Acids (annotations: CHEBI:CHEBI:15904)
  Modifiers: CD36 (annotations: HGNC:1663,REFSEQ:NM_001001547,HGNC_SYMBOL:CD36,,ENTREZ:948,UNIPROT:P16671,PUBMED:18477307)
  (References: PUBMED:12856180|PUBMED:18477307)
RID: 55586 (;Positive influence'):
  Reactants: NFE2L2 (annotations: UNIPROT:Q16236,,PUBMED:28416361,ENTREZ:4780,REFSEQ:NM_006164,HGNC:7782,HGNC_SYMBOL:NFE2L2)
  Products: G6PD (annotations: UNIPROT:P11413,HGNC:4057,ENTREZ:2539,HGNC_SYMBOL:G6PD,,REFSEQ:NM_000402)
  Modifiers: None
RID: 56158 (;State transition'):
  Reactants: 3-Phosphoglycerate (annotations: CHEBI:CHEBI:17050,CHEBI:CHEBI:17794,CHEBI:CHEBI:57998)
  Products: 2-Phosphoglycerate (annotations: CHEBI:CHEBI:24344)
  Modifiers: PGAM1 (formerSymbols: PGAMA) (annotations: ,HGNC:8888,ENTREZ:5223,UNIPROT:P18669,HGNC_SYMBOL:PGAM1,REFSEQ:NM_002629)
  (References: WIKIPATHWAYS:WP534)
RID: 56161 (;State transition'):
  Reactants: Glycogen (n) (annotations: CHEBI:CHEBI:28087); UDP-Glucose (annotations: CHEBI:CHEBI:18066)
  Products: Glycogen (n+1) (annotations: CHEBI:CHEBI:28087)
  Modifiers: GYS; GBE1 (annotations: HGNC:4180,HGNC_SYMBOL:GBE1,,REFSEQ:NM_000158,WIKIPEDIA:Glycogen_branching_enzyme,UNIPROT:Q04446,ENTREZ:2632)
  (References: WIKIPATHWAYS:WP500|PUBMED:31284506)
RID: 56198 (;State transition'):
  Reactants: Acetaldehyde (annotations: CHEBI:CHEBI:15343)
  Products: Acetate (annotations: CHEBI:CHEBI:30089,CHEBI:CHEBI:47622)
  Modifiers: ALDH
RID: 55825 (;State transition'):
  Reactants: SQOX (annotations: CHEBI:CHEBI:78662)
  Products: LNSOL (annotations: CHEBI:CHEBI:16521)
  Modifiers: LSS (annotations: HGNC_SYMBOL:LSS,,REFSEQ:NM_001001438,UNIPROT:P48449,ENTREZ:4047,HGNC:6708)
  (References: DOI:10.1016/B978-0-12-824048-9.00005-5)
RID: 55173 (;Known transition omitted'):
  Reactants: ACOT2 (annotations: REFSEQ:NM_006821,HGNC_SYMBOL:ACOT2,,ENTREZ:10965,HGNC:18431,UNIPROT:P49753)
  Products: Fatty Acid Biosynthesis (annotations: WIKIPATHWAYS:WP4491,GO:GO:0006633)
  Modifiers: None
RID: 55973 (;Transport'):
  Reactants: Malate (annotations: CHEBI:CHEBI:15595,CHEBI:CHEBI:30797)
  Products: Malate (annotations: CHEBI:CHEBI:15595,CHEBI:CHEBI:30797)
  Modifiers: GLAST1
RID: 55738 (;Negative influence'):
  Reactants: ROCK (annotations: ,ENTREZ:9475,HGNC:10252,HGNC_SYMBOL:ROCK2,REFSEQ:NM_001321643,UNIPROT:O75116)
  Products: AKT1 (annotations: ENTREZ:207,HGNC:391,PUBMED:28416361,HGNC_SYMBOL:AKT1,REFSEQ:NM_005163,UNIPROT:P31749,)
  Modifiers: None
RID: 55708 (;Transport'):
  Reactants: Fatty acyl-CoA
  Products: Long-chain Fatty Acids
  Modifiers: DBI (annotations: HGNC_SYMBOL:DBI,ENTREZ:1622,,UNIPROT:P07108,PUBMED:18477307,HGNC:2690,REFSEQ:NM_020548)
  (References: PUBMED:18477307)
RID: 55104 (;Transport'):
  Reactants: Long-chain Fatty Acids (annotations: CHEBI:CHEBI:15904)
  Products: Long-chain Fatty Acids (annotations: CHEBI:CHEBI:15904)
  Modifiers: Diffusion (annotations: GO:GO:0022803,PUBMED:18477307)
  (References: PUBMED:18477307)
RID: 55427 (PDmap:re573.0;State transition'):
  Reactants: icosanoyl-CoA (annotations: PUBCHEM:16061151,HMDB:HMDB0004258,REACTOME:REACT_22685.1,KEGG_COMPOUND:C02041,CHEMSPIDER:17220830,CHEBI:CHEBI:15527,CAS:15895-27-9)
  Products: 3-oxodocosanoyl-CoA (annotations: REACTOME:REACT_22766.1,CHEBI:CHEBI:52328)
  Modifiers: ELOVL7 (annotations: HGNC_SYMBOL:ELOVL7,HGNC:26292,UNIPROT:A1L3X0,ENTREZ:79993,REFSEQ:NM_001104558,)
  (References: REACTOME:REACT_22192.1)
RID: 55341 (;State transition'):
  Reactants: peroxynitrite (annotations: CHEBI:CHEBI:25941); TXN (annotations: ENTREZ:7295,UNIPROT:P10599,HGNC:12435,,REFSEQ:NM_001244938,HGNC_SYMBOL:TXN)
  Products: nitrite (annotations: CAS:14797-65-0,HMDB:HMDB0002786,WIKIPEDIA:Nitrite,PUBCHEM:946,CHEMSPIDER:921,KEGG_COMPOUND:C00088,CHEBI:CHEBI:16301); H2O (annotations: HMDB:HMDB0002111,CHEBI:CHEBI:15377,PUBCHEM:962,CHEMSPIDER:937,MESH_2012:D014867,WIKIPEDIA:Water,CAS:7732-18-5,CHEMBL_COMPOUND:CHEMBL1098659,KEGG_COMPOUND:C00001); hC TXN:hC TXN
  Modifiers: PRDX5 (annotations: UNIPROT:P30044,REFSEQ:NM_181651,,HGNC_SYMBOL:PRDX5,HGNC:9355,ENTREZ:25824)
  (References: REACTOME:REACT_264249)
RID: 55103 (;Transport'):
  Reactants: Fatty acyl-CoA (annotations: CHEBI:CHEBI:37554)
  Products: Peroxisomal Beta-Oxidation (annotations: GO:GO:0006635,WIKIPATHWAYS:WP1941)
  Modifiers: DBI (annotations: HGNC_SYMBOL:DBI,ENTREZ:1622,,UNIPROT:P07108,PUBMED:18477307,HGNC:2690,REFSEQ:NM_020548)
RID: 55812 (;State transition'):
  Reactants: LNSOL (annotations: CHEBI:CHEBI:16521)
  Products: 24,25-Dihydrolanosterol (annotations: CHEBI:CHEBI:28113)
  Modifiers: DHCR24 (formerSymbols: DCE) (annotations: REFSEQ:NM_014762,HGNC_SYMBOL:DHCR24,,ENTREZ:1718,UNIPROT:Q15392,HGNC:2859)
  (References: DOI:10.1016/B978-0-12-824048-9.00005-5)
RID: 55634 (;State transition'):
  Reactants: CREB1 (annotations: REFSEQ:NM_134442,HGNC:2345,ENTREZ:1385,HGNC_SYMBOL:CREB1,UNIPROT:P16220,)
  Products: CREB1 (annotations: REFSEQ:NM_134442,HGNC:2345,ENTREZ:1385,HGNC_SYMBOL:CREB1,UNIPROT:P16220,)
  Modifiers: PKA
RID: 55982 (;Positive influence'):
  Reactants: RPS6KB2 (annotations: REFSEQ:NM_003952,HGNC:10437,ENTREZ:6199,,UNIPROT:Q9UBS0,HGNC_SYMBOL:RPS6KB2)
  Products: Cell Proliferation (annotations: GO:GO:0072574)
  Modifiers: None
RID: 55117 (;Known transition omitted'):
  Reactants: Cholesterol (annotations: CHEBI:CHEBI:16113,KEGG_COMPOUND:C00187)
  Products: Cell membranes (annotations: GO:GO:0044091)
  Modifiers: None
RID: 55413 (PDmap:re519.0;State transition'):
  Reactants: trans-dodec-2-enoyl-CoA (annotations: CHEBI:CHEBI:15471,REACTOME:REACT_5571.1)
  Products: (S)-3-hydroxylauroyl-CoA (annotations: REACTOME:REACT_5323.1,KEGG_COMPOUND:C05262,HMDB:HMDB0003936,CAS:72059-49-5,CHEMSPIDER:389501,CHEBI:CHEBI:27668,PUBCHEM:440603)
  Modifiers: ECHS1 (annotations: HGNC_SYMBOL:ECHS1,,ENTREZ:1892,UNIPROT:P30084,HGNC:3151,REFSEQ:NM_004092)
  (References: REACTOME:REACT_64.2|PUBMED:13295248)
RID: 55664 (;Truncation'):
  Reactants: Fructose-1,6-Bisphosphate (annotations: CHEBI:CHEBI:78682)
  Products: Glyceralaldehyde-3-Phosphate (annotations: CHEBI:CHEBI:17138); Dihydroxyacetone-Phosphate (annotations: CHEBI:CHEBI:16108)
  Modifiers: ALDOB (annotations: ENTREZ:229,REFSEQ:NM_000035,HGNC:417,,HGNC_SYMBOL:ALDOB,UNIPROT:P05062)
RID: 55618 (;Positive influence'):
  Reactants: PKLR (annotations: HGNC_SYMBOL:PKLR,REFSEQ:NM_000298,PUBMED:31284506,HGNC:9020,UNIPROT:P30613,ENTREZ:5313,)
  Products: Glycolysis (annotations: GO:GO:0061621)
  Modifiers: None
RID: 55614 (;State transition'):
  Reactants: Isopentenyl diphosphate (annotations: CHEBI:CHEBI:16584)
  Products: DMAPP (annotations: CHEBI:CHEBI:57623)
  Modifiers: IDI1 (annotations: ,HGNC:5387,UNIPROT:Q13907,HGNC_SYMBOL:IDI1,REFSEQ:NM_004508,ENTREZ:3422)
  (References: DOI:10.1016/B978-0-12-824048-9.00005-5)
RID: 55693 (;Reduced trigger'):
  Reactants: IRS2 (formerSymbols: ECHD) (annotations: UNIPROT:Q9Y4H2,HGNC:6126,ENTREZ:8660,HGNC_SYMBOL:IRS2,,REFSEQ:NM_003749)
  Products: PI3K (annotations: REFSEQ:NM_000188,,HGNC_SYMBOL:HK1,UNIPROT:P19367,HGNC:4922,ENTREZ:3098)
  Modifiers: None
RID: 55647 (;State transition'):
  Reactants: PFKL (annotations: HGNC:8876,UNIPROT:P17858,PUBMED:31284506,REFSEQ:NM_001002021,,ENTREZ:5211,HGNC_SYMBOL:PFKL)
  Products: PFKL (annotations: HGNC:8876,UNIPROT:P17858,PUBMED:31284506,REFSEQ:NM_001002021,,ENTREZ:5211,HGNC_SYMBOL:PFKL)
  Modifiers: None
RID: 55256 (;Transport'):
  Reactants: precursor protein N-terminus binding (annotations: GO:GO:0047485)
  Products: precursor protein N-terminus binding (annotations: GO:GO:0047485)
  Modifiers: TOM complex (annotations: GO:GO:0005742); TIM22 complex (annotations: GO:GO:0042721); TIM23 complex (annotations: GO:GO:0005744); TIM9-TIM10 complex (annotations: GO:GO:0042719)
  (References: DOI:10.1016/S0022-2836(02)01440-7|DOI:10.1146/annurev.cellbio.13.1.25|DOI:10.1101/2020.03.22.002386v3)
RID: 55962 (;Positive influence'):
  Reactants: PFKL (annotations: HGNC:8876,UNIPROT:P17858,PUBMED:31284506,REFSEQ:NM_001002021,,ENTREZ:5211,HGNC_SYMBOL:PFKL)
  Products: Glycolysis (annotations: GO:GO:0061621)
  Modifiers: None
RID: 55086 (;State transition'):
  Reactants: Phosphatidic Acid
  Products: DAG
  Modifiers: LPIN
RID: 55564 (;State transition'):
  Reactants: PKLR (annotations: HGNC_SYMBOL:PKLR,REFSEQ:NM_000298,PUBMED:31284506,HGNC:9020,UNIPROT:P30613,ENTREZ:5313,)
  Products: PKLR (annotations: HGNC_SYMBOL:PKLR,REFSEQ:NM_000298,PUBMED:31284506,HGNC:9020,UNIPROT:P30613,ENTREZ:5313,)
  Modifiers: PKA
RID: 55094 (;Known transition omitted'):
  Reactants: APOB:LDLR:LDLRAP1
  Products:  
  Modifiers: MYLIP (annotations: REFSEQ:NM_013262,ENTREZ:29116,UNIPROT:Q8WY64,HGNC:21155,HGNC_SYMBOL:MYLIP,)
  (References: KEGG_PATHWAY:map04979)
RID: 55308 (;Transport'):
  Reactants: citrate(3-) (annotations: KEGG_COMPOUND:C00158,PUBCHEM:311,CHEBI:CHEBI:30769,CHEBI:CHEBI:16947,WIKIPEDIA:Citric acid,REACTOME:REACT_2769.1,CHEMBL_COMPOUND:CHEMBL1261,CHEMSPIDER:305,HMDB:HMDB0000094,CAS:77-92-9)
  Products: citrate(3-) (annotations: KEGG_COMPOUND:C00158,PUBCHEM:311,CHEBI:CHEBI:30769,CHEBI:CHEBI:16947,WIKIPEDIA:Citric acid,REACTOME:REACT_2769.1,CHEMBL_COMPOUND:CHEMBL1261,CHEMSPIDER:305,HMDB:HMDB0000094,CAS:77-92-9)
  Modifiers: None
RID: 55407 (PDmap:re570.0;State transition'):
  Reactants: fatty acyl-CoA (annotations: CHEBI:CHEBI:37554,REACTOME:REACT_5036.3); 1,2-diacyl-sn-glycerol (annotations: CHEBI:CHEBI:17815,REACTOME:REACT_4481.3)
  Products: coenzyme A (annotations: CHEBI:CHEBI:15346,REACTOME:REACT_3654.2); triglyceride (annotations: CHEBI:CHEBI:17855,REACTOME:REACT_22886.2)
  Modifiers: DGAT2 (annotations: HGNC_SYMBOL:DGAT2,,HGNC:16940,REFSEQ:NM_032564,UNIPROT:Q96PD7,ENTREZ:84649)
  (References: PUBMED:14521909|PUBMED:11481335|REACTOME:REACT_22179.1)
RID: 55945 (;Positive influence'):
  Reactants: RXRA (annotations: UNIPROT:P19793,,HGNC:10477,REFSEQ:NM_002957,ENTREZ:6256,HGNC_SYMBOL:RXRA)
  Products: NR1I2 (annotations: ,HGNC_SYMBOL:NR1I2,HGNC:7968,REFSEQ:NM_003889,ENTREZ:8856,UNIPROT:O75469)
  Modifiers: None
RID: 55169 (;Known transition omitted'):
  Reactants: Diepoxy-Squalene (annotations: CHEBI:CHEBI:138307)
  Products: 24,25-epoxycholesterol (annotations: CHEBI:CHEBI:41633)
  Modifiers: None
  (References: WIKIPATHWAYS:WP4718)
RID: 55344 (PDmap:re536.0;State transition'):
  Reactants: (S)-3-hydroxybutanoyl-CoA (annotations: CHEBI:CHEBI:15453,REACTOME:REACT_4099.1)
  Products: acetoacetyl-CoA (annotations: HMDB:HMDB0001484,CHEBI:CHEBI:15345,PUBCHEM:439214,CHEMSPIDER:388353,CAS:1420-36-6,REACTOME:REACT_2705.1,KEGG_COMPOUND:C00332,WIKIPEDIA:Acetoacetyl-CoA)
  Modifiers: HADH (formerSymbols: HADHSC) (annotations: HGNC_SYMBOL:HADH,REFSEQ:NM_005327,,HGNC:4799,ENTREZ:3033,UNIPROT:Q16836)
  (References: REACTOME:REACT_447.2|PUBMED:8687463|PUBMED:10231530)
RID: 55654 (;State transition'):
  Reactants: Isocitrate (annotations: CHEBI:CHEBI:16087)
  Products: α-Ketogluatarate (annotations: CHEBI:CHEBI:30915);  NADPH (annotations: CHEBI:CHEBI:57783,CHEBI:CHEBI:16474)
  Modifiers: isocitrate dehydrogenase
RID: 55589 (;State transition'):
  Reactants: Succinyl-CoA (annotations: CHEBI:CHEBI:15380,CHEBI:CHEBI:57292)
  Products: Succinate (annotations: CHEBI:CHEBI:30031)
  Modifiers: GDP-Forming SUCL; SUCLA2 (formerSymbols: LINC00444) (annotations: HGNC:11448,HGNC_SYMBOL:SUCLA2,REFSEQ:NM_003850,,UNIPROT:Q9P2R7,ENTREZ:8803)
RID: 56181 (;State transition'):
  Reactants: Glyceraldehyde (annotations: CHEBI:CHEBI:5445,CHEBI:CHEBI:17378)
  Products: Glyceralaldehyde-3-Phosphate (annotations: CHEBI:CHEBI:17138)
  Modifiers: TKFC (formerSymbols: DAK) (annotations: REFSEQ:NM_015533,HGNC_SYMBOL:TKFC,ENTREZ:26007,,HGNC:24552,UNIPROT:Q3LXA3)
RID: 56123 (;State transition'):
  Reactants: Fructose-6-Phosphate (annotations: CHEBI:CHEBI:15946,CHEBI:CHEBI:16084)
  Products: Fructose-1,6-Bisphosphate (annotations: CHEBI:CHEBI:78682)
  Modifiers: PFKL (annotations: HGNC:8876,UNIPROT:P17858,PUBMED:31284506,REFSEQ:NM_001002021,,ENTREZ:5211,HGNC_SYMBOL:PFKL)
RID: 56037 (;Negative influence'):
  Reactants: PPARA (formerSymbols: PPAR) (annotations: HGNC_SYMBOL:PPARA,ENTREZ:5465,REFSEQ:NM_001001928,,PUBMED:26451809,UNIPROT:Q07869,HGNC:9232)
  Products: SREBF1 (annotations: UNIPROT:P36956,REFSEQ:NM_004176,ENTREZ:6720,HGNC:11289,HGNC_SYMBOL:SREBF1,)
  Modifiers: None
RID: 55509 (;Positive influence'):
  Reactants: FOXO1 (formerSymbols: FKHR,FOXO1A) (annotations: HGNC:3819,,REFSEQ:NM_002015,ENTREZ:2308,PUBMED:28416361,HGNC_SYMBOL:FOXO1,UNIPROT:Q12778)
  Products: Cell Survival
  Modifiers: None
RID: 56018 (;Known transition omitted'):
  Reactants: SREBF1 (annotations: UNIPROT:P36956,REFSEQ:NM_004176,ENTREZ:6720,HGNC:11289,HGNC_SYMBOL:SREBF1,)
  Products: SREBP-1c (annotations: PUBMED:26451809)
  Modifiers: None
RID: 55943 (;Positive influence'):
  Reactants: Oxysterols (annotations: CHEBI:CHEBI:53030)
  Products: NR1H3 (annotations: REFSEQ:NM_001130101,,HGNC:7966,ENTREZ:10062,UNIPROT:Q13133,HGNC_SYMBOL:NR1H3)
  Modifiers: None
RID: 56044 (;Positive influence'):
  Reactants: NR1H3 (annotations: REFSEQ:NM_001130101,,HGNC:7966,ENTREZ:10062,UNIPROT:Q13133,HGNC_SYMBOL:NR1H3)
  Products: Cholesterol Metabolism (annotations: KEGG_PATHWAY:map04979)
  Modifiers: None
RID: 55106 (;Known transition omitted'):
  Reactants: Cholesterol (annotations: CHEBI:CHEBI:16113,KEGG_COMPOUND:C00187); NPC2 (annotations: ,REFSEQ:NM_006432,HGNC_SYMBOL:NPC2,UNIPROT:P61916,HGNC:14537,ENTREZ:10577)
  Products: Cholesterol (annotations: CHEBI:CHEBI:16113,KEGG_COMPOUND:C00187)
  Modifiers: STARD3:VAPA; NPC1:OSBPL5
  (References: WIKIPATHWAYS:WP5304)
RID: 55237 (;Modulation'):
  Reactants: Mt-dNTP pool (annotations: PUBMED:23149385)
  Products: mt DNA replication
  Modifiers: None
  (References: PUBMED:23149385|TAXONOMY:10090)
RID: 56202 (;State transition'):
  Reactants: Acetaldehyde (annotations: CHEBI:CHEBI:15343)
  Products: Ethanol (annotations: CHEBI:CHEBI:16236)
  Modifiers: ADH
RID: 55264 (;State transition'):
  Reactants: O2 (annotations: CHEBI:CHEBI:15379,KEGG_COMPOUND:C00007,HMDB:HMDB0001377,PUBCHEM:977,CHEMSPIDER:952,CAS:7782-44-7,WIKIPEDIA:Oxygen); NADPH (annotations: KEGG_COMPOUND:C00005,HMDB:HMDB0000221,CHEMSPIDER:17215925,CHEMBL_COMPOUND:CHEMBL213053,CHEBI:CHEBI:16474,CAS:53-57-6,WIKIPEDIA:NADPH,PUBCHEM:22833512)
  Products: superoxide (annotations: HMDB:HMDB0002168,WIKIPEDIA:Superoxide,PUBCHEM:5359597,CHEMSPIDER:4514331,KEGG_COMPOUND:C00704,CHEBI:CHEBI:18421,CAS:11062-77-4); NADP+ (annotations: CHEBI:CHEBI:18009,WIKIPEDIA:NADP,KEGG_COMPOUND:C00006,CAS:53-59-8,PUBCHEM:5886,CHEMBL_COMPOUND:CHEMBL213053,HMDB:HMDB0000217,CHEMSPIDER:5675,REACTOME:REACT_4609.3); H+ (annotations: CHEBI:CHEBI:15378)
  Modifiers: NOX2
  (References: REACTOME:REACT_264249)
RID: 55972 (;State transition'):
  Reactants: Glycogen (n) (annotations: CHEBI:CHEBI:28087); UDP-Glucose (annotations: CHEBI:CHEBI:18066)
  Products: Glycogen (n+1) (annotations: CHEBI:CHEBI:28087)
  Modifiers: GYS; GBE1 (annotations: HGNC:4180,HGNC_SYMBOL:GBE1,,REFSEQ:NM_000158,WIKIPEDIA:Glycogen_branching_enzyme,UNIPROT:Q04446,ENTREZ:2632)
RID: 55601 (;Positive influence'):
  Reactants: FABP1 (annotations: REFSEQ:NM_001443,UNIPROT:P07148,,HGNC:3555,HGNC_SYMBOL:FABP1,ENTREZ:2168)
  Products: Fatty Acid Transport (annotations: WIKIPATHWAYS:WP5061)
  Modifiers: None
RID: 55791 (;Positive influence'):
  Reactants: ChREBP (annotations: PUBMED:26451809)
  Products: FASN (annotations: HGNC:3594,UNIPROT:P49327,REFSEQ:NM_004104,,ENTREZ:2194,HGNC_SYMBOL:FASN)
  Modifiers: None
RID: 55637 (;Positive influence'):
  Reactants: HNF4A (formerSymbols: MODY,MODY1,TCF14) (annotations: ,HGNC:5024,ENTREZ:3172,UNIPROT:P41235,HGNC_SYMBOL:HNF4A,REFSEQ:NM_000457)
  Products: G6PC (annotations: PUBMED:28416361,)
  Modifiers: None
RID: 55585 (;Negative influence'):
  Reactants: AMPK (annotations: GO:GO:0031588)
  Products: mTORC1 (annotations: GO:GO:0031931)
  Modifiers: None
  (References: PUBMED:22539004|PUBMED:23361334)
RID: 55150 (;State transition'):
  Reactants: SREBF2 (annotations: HGNC:11290,REFSEQ:NM_004599,UNIPROT:Q12772,,HGNC_SYMBOL:SREBF2,ENTREZ:6721)
  Products: SREBF2 (annotations: HGNC:11290,REFSEQ:NM_004599,UNIPROT:Q12772,,HGNC_SYMBOL:SREBF2,ENTREZ:6721)
  Modifiers: None
RID: 56186 (;State transition'):
  Reactants: Glucose-6-Phosphate (annotations: CHEBI:CHEBI:14314)
  Products: Fructose-6-Phosphate (annotations: CHEBI:CHEBI:15946,CHEBI:CHEBI:16084)
  Modifiers: GPI (annotations: ENTREZ:2821,,HGNC_SYMBOL:GPI,HGNC:4458,REFSEQ:NM_000175,UNIPROT:P06744)
  (References: WIKIPATHWAYS:WP534)
RID: 55785 (;Positive influence'):
  Reactants: ChREBP (annotations: PUBMED:26451809)
  Products: ACACB (annotations: UNIPROT:O00763,HGNC_SYMBOL:ACACB,HGNC:85,REFSEQ:NM_001093,ENTREZ:32,)
  Modifiers: None
RID: 56069 (;Known transition omitted'):
  Reactants: Nascent HDL
  Products: HDL
  Modifiers: None
RID: 55923 (;Positive influence'):
  Reactants: PCK1 (annotations: ,PUBMED:28416361,HGNC:8724,UNIPROT:P35558,HGNC_SYMBOL:PCK1,REFSEQ:NM_002591,ENTREZ:5105)
  Products: Gluconeogenesis (annotations: GO:GO:0006094)
  Modifiers: None
RID: 55885 (;Positive influence'):
  Reactants: ACACB (annotations: UNIPROT:O00763,HGNC_SYMBOL:ACACB,HGNC:85,REFSEQ:NM_001093,ENTREZ:32,)
  Products: Fatty Acid Synthesis (annotations: GO:GO:0005835)
  Modifiers: None
RID: 56060 (;Known transition omitted'):
  Reactants: Acyl-CoA (annotations: CHEBI:CHEBI:17984)
  Products: Long-chain Fatty Acids
  Modifiers: None
RID: 55770 (;Known transition omitted'):
  Reactants: AHRR (formerSymbols: AHH,AHHR) (annotations: HGNC:346,,HGNC_SYMBOL:AHRR,REFSEQ:NM_020731,UNIPROT:A9YTQ3,ENTREZ:57491)
  Products: AHRR (formerSymbols: AHH,AHHR) (annotations: HGNC:346,,HGNC_SYMBOL:AHRR,REFSEQ:NM_020731,UNIPROT:A9YTQ3,ENTREZ:57491)
  Modifiers: None
RID: 56218 (;Known transition omitted'):
  Reactants: Threonine (annotations: CHEBI:CHEBI:16857,CHEBI:CHEBI:26986)
  Products: Glycin (annotations: CHEBI:CHEBI:55443,CHEBI:CHEBI:15428)
  Modifiers: None
RID: 55635 (;Positive influence'):
  Reactants: FOXA2 (formerSymbols: HNF3B) (annotations: PUBMED:19595610,ENTREZ:3170,HGNC_SYMBOL:FOXA2,UNIPROT:Q9Y261,REFSEQ:NM_021784,,HGNC:5022)
  Products: CPT1A (formerSymbols: CPT1) (annotations: UNIPROT:P50416,PUBMED:19595610,HGNC_SYMBOL:CPT1A,HGNC:2328,ENTREZ:1374,REFSEQ:NM_001876,)
  Modifiers: None
RID: 55263 (PDmap:re540.0;State transition'):
  Reactants: sn-glycerol 3-phosphate (annotations: CHEMSPIDER:388308,KEGG_COMPOUND:C00093,WIKIPEDIA:Glycerol 3-phosphate,HMDB:HMDB0000126,REACTOME:REACT_4327.2,CHEBI:CHEBI:15978,PUBCHEM:439162,CAS:57-03-4)
  Products: glycerone phosphate (annotations: HMDB:HMDB0001473,WIKIPEDIA:Dihydroxyacetone phosphate,CHEMSPIDER:648,PUBCHEM:668,CHEBI:CHEBI:16108,CAS:57-04-5,KEGG_COMPOUND:C00111)
  Modifiers: GPD2 (annotations: ENTREZ:2820,HGNC:4456,REFSEQ:NM_000408,,UNIPROT:P43304,HGNC_SYMBOL:GPD2)
  (References: PUBMED:8163052|PUBMED:7821823|PUBMED:8687421|REACTOME:REACT_16938.2)
RID: 55641 (;Positive influence'):
  Reactants: NR1I3 (annotations: ENTREZ:9970,UNIPROT:Q14994,,HGNC:7969,REFSEQ:NM_001077469,HGNC_SYMBOL:NR1I3)
  Products: SREBF1 (annotations: UNIPROT:P36956,REFSEQ:NM_004176,ENTREZ:6720,HGNC:11289,HGNC_SYMBOL:SREBF1,)
  Modifiers: None
RID: 56112 (;State transition'):
  Reactants: Long-chain Fatty Acids
  Products: Fatty acyl-CoA
  Modifiers: ACSL
  (References: WIKIPATHWAYS:WP5061)
RID: 55949 (;Positive influence'):
  Reactants: APOA5 (annotations: HGNC:17288,HGNC_SYMBOL:APOA5,UNIPROT:Q6Q788,,ENTREZ:116519,REFSEQ:NM_001166598)
  Products: Apolipoprotein Metabolism
  Modifiers: None
RID: 55091 (;State transition'):
  Reactants: Glycerol-3-P
  Products: DHA-P
  Modifiers: GPD1 (annotations: ,UNIPROT:P21695,HGNC:4455,HGNC_SYMBOL:GPD1,ENTREZ:2819,REFSEQ:NM_001257199); GPD2 (annotations: ENTREZ:2820,HGNC:4456,REFSEQ:NM_000408,,UNIPROT:P43304,HGNC_SYMBOL:GPD2)
RID: 56009 (;State transition'):
  Reactants: 1,3-Bisphosphoglycerate (annotations: CHEBI:CHEBI:89363)
  Products: 2,3-Bisphosphoglycerate (annotations: CHEBI:CHEBI:19324)
  Modifiers: BPGM (annotations: ENTREZ:669,HGNC_SYMBOL:BPGM,REFSEQ:NM_001724,,HGNC:1093,UNIPROT:P07738)
RID: 55913 (;Positive influence'):
  Reactants: PCK1 (annotations: ,PUBMED:28416361,HGNC:8724,UNIPROT:P35558,HGNC_SYMBOL:PCK1,REFSEQ:NM_002591,ENTREZ:5105)
  Products: Fatty Acid Metabolism (annotations: GO:GO:0009062)
  Modifiers: None
RID: 56014 (;State transition'):
  Reactants: PDPK1 (annotations: ,ENTREZ:5170,HGNC:8816,REFSEQ:NM_001261816,HGNC_SYMBOL:PDPK1,UNIPROT:O15530)
  Products: PDPK1 (annotations: ,ENTREZ:5170,HGNC:8816,REFSEQ:NM_001261816,HGNC_SYMBOL:PDPK1,UNIPROT:O15530)
  Modifiers: PIP3 (annotations: CHEBI:CHEBI:60169)
RID: 56053 (;Positive influence'):
  Reactants: FOXO1 (formerSymbols: FKHR,FOXO1A) (annotations: HGNC:3819,,REFSEQ:NM_002015,ENTREZ:2308,PUBMED:28416361,HGNC_SYMBOL:FOXO1,UNIPROT:Q12778)
  Products: G6PC (annotations: PUBMED:28416361,)
  Modifiers: None
RID: 56137 (;State transition'):
  Reactants: PFKFB1 (formerSymbols: PFRX) (annotations: ENTREZ:5207,REFSEQ:NM_001271804,UNIPROT:P16118,HGNC:8872,HGNC_SYMBOL:PFKFB1,)
  Products: PFKFB1 (formerSymbols: PFRX) (annotations: ENTREZ:5207,REFSEQ:NM_001271804,UNIPROT:P16118,HGNC:8872,HGNC_SYMBOL:PFKFB1,)
  Modifiers: Protein kinase A
RID: 55938 (;Positive influence'):
  Reactants: NR1H3 (annotations: REFSEQ:NM_001130101,,HGNC:7966,ENTREZ:10062,UNIPROT:Q13133,HGNC_SYMBOL:NR1H3)
  Products: FASN (annotations: HGNC:3594,UNIPROT:P49327,REFSEQ:NM_004104,,ENTREZ:2194,HGNC_SYMBOL:FASN)
  Modifiers: None
RID: 55162 (;State transition'):
  Reactants: Cholesterol (annotations: CHEBI:CHEBI:16113,KEGG_COMPOUND:C00187)
  Products: 27-hydroxycholesterol (annotations: CHEBI:CHEBI:17703)
  Modifiers: CYP27A1 (formerSymbols: CYP27) (annotations: HGNC_SYMBOL:CYP27A1,REFSEQ:NM_000784,,ENTREZ:1593,UNIPROT:Q02318,HGNC:2605)
  (References: WIKIPATHWAYS:WP4718)
RID: 55286 (PDmap:re538.0;State transition'):
  Reactants: (S)-methylmalonyl-CoA (annotations: REACTOME:REACT_4910.1,CHEBI:CHEBI:15466,HMDB:HMDB0001269,WIKIPEDIA:Methylmalonyl-CoA,PUBCHEM:439291,CHEMSPIDER:388424,CAS:104809-02-1,KEGG_COMPOUND:C00683)
  Products: (R)-methylmalonyl-CoA (annotations: CHEBI:CHEBI:15465,REACTOME:REACT_5502.1)
  Modifiers: MCEE (annotations: ENTREZ:84693,,REFSEQ:NM_032601,HGNC:16732,HGNC_SYMBOL:MCEE,UNIPROT:Q96PE7)
  (References: REACTOME:REACT_1909.2|PUBMED:11481338|PUBMED:13934211)
RID: 55965 (;State transition'):
  Reactants: Cholesterol (annotations: CHEBI:CHEBI:16113,KEGG_COMPOUND:C00187); Phospholipids; APOA1 (annotations: HGNC:600,,UNIPROT:P02647,ENTREZ:335,REFSEQ:NM_000039,HGNC_SYMBOL:APOA1)
  Products: Nascent HDL
  Modifiers: None
RID: 55581 (;State transition'):
  Reactants: IRS2 (formerSymbols: ECHD) (annotations: UNIPROT:Q9Y4H2,HGNC:6126,ENTREZ:8660,HGNC_SYMBOL:IRS2,,REFSEQ:NM_003749)
  Products: IRS2 (formerSymbols: ECHD) (annotations: UNIPROT:Q9Y4H2,HGNC:6126,ENTREZ:8660,HGNC_SYMBOL:IRS2,,REFSEQ:NM_003749)
  Modifiers: INSR:INS (annotations: REFSEQ:NM_000189,HGNC_SYMBOL:HK2,UNIPROT:P52789,ENTREZ:3099,HGNC:4923,)
RID: 55563 (;Positive influence'):
  Reactants: PFKFB
  Products: Gluconeogenesis
  Modifiers: None
RID: 55631 (;Known transition omitted'):
  Reactants: PPARGC1A (formerSymbols: PPARGC1) (annotations: UNIPROT:Q9UBK2,ENTREZ:10891,HGNC:9237,HGNC_SYMBOL:PPARGC1A,,REFSEQ:NM_013261)
  Products: PPARGC1A (formerSymbols: PPARGC1) (annotations: UNIPROT:Q9UBK2,ENTREZ:10891,HGNC:9237,HGNC_SYMBOL:PPARGC1A,,REFSEQ:NM_013261)
  Modifiers: None
RID: 56091 (;Positive influence'):
  Reactants: FOXA2 (formerSymbols: HNF3B) (annotations: PUBMED:19595610,ENTREZ:3170,HGNC_SYMBOL:FOXA2,UNIPROT:Q9Y261,REFSEQ:NM_021784,,HGNC:5022)
  Products: HMGCS2 (annotations: UNIPROT:P54868,HGNC:5008,HGNC_SYMBOL:HMGCS2,ENTREZ:3158,,REFSEQ:NM_005518)
  Modifiers: None
RID: 55981 (;Known transition omitted'):
  Reactants: Linoleoyl-CoA (annotations: CHEBI:CHEBI:15530)
  Products: Cis,cis-3,6-Dodecadienoyl-CoA (annotations: CHEBI:CHEBI:28002); Acetyl-CoA (annotations: CHEBI:CHEBI:15351,CHEBI:CHEBI:57288)
  Modifiers: Mitochondrial trifunctional enzyme; ACADL (annotations: ,REFSEQ:NM_001608,HGNC_SYMBOL:ACADL,HGNC:88,ENTREZ:33,UNIPROT:P28330)
RID: 56212 (;State transition'):
  Reactants: Fructose-1,6-Bisphosphate (annotations: CHEBI:CHEBI:78682)
  Products: Fructose-6-Phosphate (annotations: CHEBI:CHEBI:15946,CHEBI:CHEBI:16084)
  Modifiers: FBP1 (formerSymbols: FBP) (annotations: HGNC_SYMBOL:FBP1,UNIPROT:P09467,REFSEQ:NM_000507,PUBMED:31284506,HGNC:3606,ENTREZ:2203,)
  (References: WIKIPATHWAYS:WP534)
RID: 55597 (;Negative influence'):
  Reactants: PLIN2 (formerSymbols: ADFP) (annotations: HGNC:248,REFSEQ:NM_001122,,HGNC_SYMBOL:PLIN2,ENTREZ:123,UNIPROT:Q99541)
  Products: MGLL (annotations: ,HGNC:17038,ENTREZ:11343,REFSEQ:NM_007283,HGNC_SYMBOL:MGLL,UNIPROT:Q99685)
  Modifiers: None
RID: 55207 (;Transcription'):
  Reactants: SCD (formerSymbols: SCDOS) (annotations: ,ENTREZ:6319,HGNC_SYMBOL:SCD,UNIPROT:O00767,HGNC:10571,REFSEQ:NM_005063)
  Products: SCD (formerSymbols: SCDOS) (annotations: ,ENTREZ:6319,HGNC_SYMBOL:SCD,UNIPROT:O00767,HGNC:10571,REFSEQ:NM_005063)
  Modifiers: SREBF2 (annotations: HGNC:11290,REFSEQ:NM_004599,UNIPROT:Q12772,,HGNC_SYMBOL:SREBF2,ENTREZ:6721)
  (References: WIKIPATHWAYS:WP4718)
RID: 55363 (;State transition'):
  Reactants: NO (annotations: HMDB:HMDB0003378,CAS:10102-43-9,WIKIPEDIA:Nitric oxide,KEGG_COMPOUND:C00533,CHEBI:CHEBI:16480,PUBCHEM:145068,MESH_2012:D009569,CHEMSPIDER:127983,CHEMBL_COMPOUND:CHEMBL1200689); superoxide (annotations: HMDB:HMDB0002168,WIKIPEDIA:Superoxide,PUBCHEM:5359597,CHEMSPIDER:4514331,KEGG_COMPOUND:C00704,CHEBI:CHEBI:18421,CAS:11062-77-4)
  Products: peroxynitrite (annotations: CHEBI:CHEBI:25941)
  Modifiers: None
  (References: REACTOME:REACT_264249)
RID: 55951 (;Positive influence'):
  Reactants: Androstane (annotations: CHEBI:CHEBI:35509)
  Products: NR1I3 (annotations: ENTREZ:9970,UNIPROT:Q14994,,HGNC:7969,REFSEQ:NM_001077469,HGNC_SYMBOL:NR1I3)
  Modifiers: None
RID: 55330 (PDmap:re548.0;State transition'):
  Reactants: acetyl-CoA (annotations: CHEBI:CHEBI:15351,WIKIPEDIA:Acetyl-CoA,HMDB:HMDB0001206,CHEMSPIDER:392413,PUBCHEM:444493,REACTOME:REACT_3839.1,CAS:72-89-9,KEGG_COMPOUND:C00024); hydrogencarbonate (annotations: CHEMBL_COMPOUND:CHEMBL363707,CAS:71-52-3,HMDB:HMDB0000595,REACTOME:REACT_4357.1,CHEMSPIDER:749,PUBCHEM:769,WIKIPEDIA:Bicarbonate,CHEBI:CHEBI:17544,KEGG_COMPOUND:C00288)
  Products: malonyl-CoA (annotations: REACTOME:REACT_3059.1,WIKIPEDIA:Malonyl-CoA,HMDB:HMDB0001175,CAS:524-14-1,CHEBI:CHEBI:15531,PUBCHEM:10663,KEGG_COMPOUND:C00083,CHEMSPIDER:10213)
  Modifiers: ACACA (formerSymbols: ACAC,ACC) (annotations: REFSEQ:NM_198836,UNIPROT:Q13085,HGNC_SYMBOL:ACACA,ENTREZ:31,HGNC:84,)
  (References: PUBMED:18455495|PUBMED:7732023|PUBMED:16854592|REACTOME:REACT_11201.2)
RID: 55334 (PDmap:re525.0;State transition'):
  Reactants: 3-oxodecanoyl-CoA (annotations: CAS:50411-91-1,KEGG_COMPOUND:C05265,PUBCHEM:440606,REACTOME:REACT_5482.1,CHEBI:CHEBI:28528,HMDB:HMDB0003939,CHEMSPIDER:389504)
  Products: octanoyl-CoA (annotations: CHEBI:CHEBI:15533,KEGG_COMPOUND:C01944,CHEMSPIDER:371,PUBCHEM:380,HMDB:HMDB0001070,REACTOME:REACT_5128.1,WIKIPEDIA:octanoyl-Coenzyme A,CAS:1264-52-4)
  Modifiers: trifunctional Protein
  (References: REACTOME:REACT_250.2|PUBMED:1550553)
RID: 55783 (;State transition'):
  Reactants: Cholesterol (annotations: CHEBI:CHEBI:16113,KEGG_COMPOUND:C00187)
  Products: Cholesterol (annotations: CHEBI:CHEBI:16113,KEGG_COMPOUND:C00187)
  Modifiers: ABCA1 (formerSymbols: ABC1,HDLDT1) (annotations: REFSEQ:NM_005502,HGNC:29,HGNC_SYMBOL:ABCA1,,ENTREZ:19,UNIPROT:O95477)
RID: 55457 (;State transition'):
  Reactants: NDUFA10 (annotations: REFSEQ:NM_004544,UNIPROT:O95299,ENTREZ:4705,HGNC_SYMBOL:NDUFA10,HGNC:7684,)
  Products: NDUFA10 (annotations: REFSEQ:NM_004544,UNIPROT:O95299,ENTREZ:4705,HGNC_SYMBOL:NDUFA10,HGNC:7684,)
  Modifiers: PINK1 (formerSymbols: PARK6) (annotations: ENTREZ:65018,UNIPROT:Q9BXM7,HGNC_SYMBOL:PINK1,,REFSEQ:NM_032409,HGNC:14581)
  (References: PUBMED:24652937)
RID: 55979 (;State transition'):
  Reactants: PFKL (annotations: HGNC:8876,UNIPROT:P17858,PUBMED:31284506,REFSEQ:NM_001002021,,ENTREZ:5211,HGNC_SYMBOL:PFKL)
  Products: PFKL (annotations: HGNC:8876,UNIPROT:P17858,PUBMED:31284506,REFSEQ:NM_001002021,,ENTREZ:5211,HGNC_SYMBOL:PFKL)
  Modifiers: None
RID: 56107 (;Positive influence'):
  Reactants: CYP4A11 (formerSymbols: CYP4A2) (annotations: ENTREZ:1579,HGNC:2642,UNIPROT:Q02928,REFSEQ:NM_000778,HGNC_SYMBOL:CYP4A11,)
  Products: Microsomal Omega-Oxidation (annotations: WIKIPATHWAYS:WP206)
  Modifiers: None
RID: 55645 (;State transition'):
  Reactants: 7-Dehydrodemosterol (annotations: CHEBI:CHEBI:27910)
  Products: 7-Dehydrocholesterol (annotations: CHEBI:CHEBI:17759)
  Modifiers: DHCR24 (formerSymbols: DCE) (annotations: REFSEQ:NM_014762,HGNC_SYMBOL:DHCR24,,ENTREZ:1718,UNIPROT:Q15392,HGNC:2859)
  (References: DOI:10.1016/B978-0-12-824048-9.00005-5)
RID: 55442 (;State transition'):
  Reactants: O2 (annotations: CHEBI:CHEBI:15379,KEGG_COMPOUND:C00007,HMDB:HMDB0001377,PUBCHEM:977,CHEMSPIDER:952,CAS:7782-44-7,WIKIPEDIA:Oxygen)
  Products: superoxide (annotations: HMDB:HMDB0002168,WIKIPEDIA:Superoxide,PUBCHEM:5359597,CHEMSPIDER:4514331,KEGG_COMPOUND:C00704,CHEBI:CHEBI:18421,CAS:11062-77-4)
  Modifiers: complex I (annotations: GO:GO:0005747)
  (References: PUBMED:19427899|PUBMED:15262965)
RID: 56156 (;State transition'):
  Reactants: Lactate (annotations: CHEBI:CHEBI:24996)
  Products: Pyruvate (annotations: CHEBI:CHEBI:15361)
  Modifiers: LDHA (annotations: UNIPROT:P00338,REFSEQ:NM_005566,HGNC_SYMBOL:LDHA,HGNC:6535,,ENTREZ:3939)
  (References: WIKIPATHWAYS:WP534)
RID: 56216 (;State transition'):
  Reactants: UDP-Glucose (annotations: CHEBI:CHEBI:18066)
  Products: Glycogen (n) (annotations: CHEBI:CHEBI:28087)
  Modifiers: Glycogenin
  (References: WIKIPATHWAYS:WP500)
RID: 55153 (;Known transition omitted'):
  Reactants: ACSL1 (formerSymbols: FACL2) (annotations: ENTREZ:2180,HGNC:3569,REFSEQ:NM_001995,UNIPROT:P33121,HGNC_SYMBOL:ACSL1,)
  Products: Fatty Acid Biosynthesis (annotations: WIKIPATHWAYS:WP4491,GO:GO:0006633)
  Modifiers: None
RID: 55136 (;Known transition omitted'):
  Reactants: LP(a)
  Products: LP(a)
  Modifiers: Secretion
  (References: WIKIPATHWAYS:WP5304)
RID: 55996 (;Positive influence'):
  Reactants: EHHADH (formerSymbols: ECHD) (annotations: ENTREZ:1962,UNIPROT:Q08426,,HGNC:3247,HGNC_SYMBOL:EHHADH,REFSEQ:NM_001166415)
  Products: Fatty Acid Metabolism (annotations: GO:GO:0009062)
  Modifiers: None
RID: 55921 (;Transport'):
  Reactants: H2O (annotations: CHEBI:CHEBI:15377)
  Products: H2O (annotations: CHEBI:CHEBI:15377)
  Modifiers: AQP9 (annotations: HGNC:643,HGNC_SYMBOL:AQP9,UNIPROT:O43315,REFSEQ:NM_020980,PUBMED:19096781,ENTREZ:366,)
  (References: PUBMED:19096781)
RID: 56002 (;State transition'):
  Reactants: Diacylglycerol
  Products: Monoacylglycerol (annotations: CHEBI:CHEBI:17408)
  Modifiers: LIPC (annotations: HGNC_SYMBOL:LIPC,,ENTREZ:3990,REFSEQ:NM_000236,HGNC:6619,UNIPROT:P11150)
RID: 55931 (;Positive influence'):
  Reactants: Fructose-1,6-Bisphosphate (annotations: CHEBI:CHEBI:78682)
  Products: PKLR (annotations: HGNC_SYMBOL:PKLR,REFSEQ:NM_000298,PUBMED:31284506,HGNC:9020,UNIPROT:P30613,ENTREZ:5313,)
  Modifiers: None
RID: 55692 (;State transition'):
  Reactants: GSK3B (annotations: HGNC_SYMBOL:GSK3B,ENTREZ:2932,PUBMED:28416361,,HGNC:4617,UNIPROT:P49841,REFSEQ:NM_001146156)
  Products: GSK3B (annotations: HGNC_SYMBOL:GSK3B,ENTREZ:2932,PUBMED:28416361,,HGNC:4617,UNIPROT:P49841,REFSEQ:NM_001146156)
  Modifiers: None
RID: 55346 (;State transition'):
  Reactants: damaged mt DNA
  Products: mt DNA (annotations: GO:GO:0000262)
  Modifiers: TFAM (formerSymbols: TCF6,TCF6L2) (annotations: REFSEQ:NM_003201,HGNC:11741,HGNC_SYMBOL:TFAM,UNIPROT:Q00059,,ENTREZ:7019); Mt-DNA repair (annotations: PUBMED:23149385); Mt-dNTP pool (annotations: PUBMED:23149385)
  (References: PUBMED:23149385)
RID: 55684 (;Known transition omitted'):
  Reactants: Fatty acyl-CoA
  Products: Fatty acyl-carnitine
  Modifiers: None
RID: 55813 (;Positive influence'):
  Reactants: SCP2 (annotations: HGNC_SYMBOL:SCP2,ENTREZ:6342,REFSEQ:NM_002979,,UNIPROT:P22307,HGNC:10606)
  Products: Peroxisomal Beta-Oxidation (annotations: WIKIPATHWAYS:WP1941)
  Modifiers: None
RID: 55803 (;Transport'):
  Reactants: Fatty acyl-CoA
  Products: Very Long Fatty Acids-CoA
  Modifiers: DBI (annotations: HGNC_SYMBOL:DBI,ENTREZ:1622,,UNIPROT:P07108,PUBMED:18477307,HGNC:2690,REFSEQ:NM_020548)
  (References: PUBMED:18477307)
RID: 55649 (;Negative influence'):
  Reactants: AHRR (formerSymbols: AHH,AHHR) (annotations: HGNC:346,,HGNC_SYMBOL:AHRR,REFSEQ:NM_020731,UNIPROT:A9YTQ3,ENTREZ:57491)
  Products: AHR (annotations: HGNC:348,HGNC_SYMBOL:AHR,,UNIPROT:P35869,REFSEQ:NM_001621,ENTREZ:196)
  Modifiers: None
RID: 55439 (PDmap:re527.0;State transition'):
  Reactants: trans-oct-2-enoyl-CoA (annotations: CHEBI:CHEBI:27537,REACTOME:REACT_5037.1)
  Products: (S)-3-hydroxyoctanoyl-CoA (annotations: CHEBI:CHEBI:28632,REACTOME:REACT_2973.1)
  Modifiers: ECHS1 (annotations: HGNC_SYMBOL:ECHS1,,ENTREZ:1892,UNIPROT:P30084,HGNC:3151,REFSEQ:NM_004092)
  (References: REACTOME:REACT_109.2|PUBMED:13295248)
RID: 55877 (;State transition'):
  Reactants: ACC
  Products: ACC
  Modifiers: AMPK (annotations: GO:GO:0031588)
RID: 55929 (;Positive influence'):
  Reactants: PI3K (annotations: REFSEQ:NM_000188,,HGNC_SYMBOL:HK1,UNIPROT:P19367,HGNC:4922,ENTREZ:3098)
  Products: PI3K cascade (annotations: GO:GO:0014065)
  Modifiers: None
RID: 55822 (;Positive influence'):
  Reactants: APOA1 (annotations: HGNC:600,,UNIPROT:P02647,ENTREZ:335,REFSEQ:NM_000039,HGNC_SYMBOL:APOA1)
  Products: Apolipoprotein Metabolism
  Modifiers: None
RID: 55506 (;Positive influence'):
  Reactants: CREB1 (annotations: REFSEQ:NM_134442,HGNC:2345,ENTREZ:1385,HGNC_SYMBOL:CREB1,UNIPROT:P16220,)
  Products: Cell Survival
  Modifiers: None
RID: 55830 (;Positive influence'):
  Reactants: PPARG (annotations: HGNC:9236,REFSEQ:NM_005037,HGNC_SYMBOL:PPARG,UNIPROT:P37231,,ENTREZ:5468)
  Products: SREBF1 (annotations: UNIPROT:P36956,REFSEQ:NM_004176,ENTREZ:6720,HGNC:11289,HGNC_SYMBOL:SREBF1,)
  Modifiers: None
RID: 55408 (PDmap:re394.0;State transition'):
  Reactants: pyruvate dehydrogenase complex (annotations: REACTOME:REACT_5500.1,GO:GO:0005967); H2O (annotations: HMDB:HMDB0002111,CHEBI:CHEBI:15377,PUBCHEM:962,CHEMSPIDER:937,MESH_2012:D014867,WIKIPEDIA:Water,CAS:7732-18-5,CHEMBL_COMPOUND:CHEMBL1098659,KEGG_COMPOUND:C00001)
  Products: pyruvate dehydrogenase complex (annotations: REACTOME:REACT_5500.1,GO:GO:0005967); phosphate(3-) (annotations: WIKIPEDIA:Phosphate,PUBCHEM:1061,CAS:14265-44-2,KEGG_COMPOUND:C00009,CHEMSPIDER:1032,CHEBI:CHEBI:18367,REACTOME:REACT_5781.1,HMDB:HMDB0001429)
  Modifiers: PDP2:PDPR; Mg2+ (annotations: REACTOME:REACT_5401.1,CHEBI:CHEBI:18420)
  (References: PUBMED:12676647)
RID: 55701 (;State transition'):
  Reactants: Acetoacetyl-CoA (annotations: CHEBI:CHEBI:15345)
  Products: HMG-CoA (annotations: CHEBI:CHEBI:11814)
  Modifiers: HMGCS1 (formerSymbols: HMGCS) (annotations: UNIPROT:Q01581,HGNC:5007,HGNC_SYMBOL:HMGCS1,,ENTREZ:3157,REFSEQ:NM_001098272)
  (References: DOI:10.1016/B978-0-12-824048-9.00005-5)
RID: 56179 (;State transition'):
  Reactants: Pyruvate (annotations: CHEBI:CHEBI:15361)
  Products: Mitochondrial Metabolism
  Modifiers: None
  (References: WIKIPATHWAYS:WP534)
RID: 55860 (;Transport'):
  Reactants: Citrate (annotations: CHEBI:CHEBI:16947,CHEBI:CHEBI:133748,CHEBI:CHEBI:50744)
  Products: Citrate (annotations: CHEBI:CHEBI:16947,CHEBI:CHEBI:133748,CHEBI:CHEBI:50744)
  Modifiers: SLC25A1 (formerSymbols: SLC20A3) (annotations: HGNC_SYMBOL:SLC25A1,REFSEQ:NM_005984,UNIPROT:P53007,,ENTREZ:6576,HGNC:10979)
RID: 56084 (;Transport'):
  Reactants: Aspartate (annotations: CHEBI:CHEBI:29995,CHEBI:CHEBI:72314)
  Products: Aspartate (annotations: CHEBI:CHEBI:29995,CHEBI:CHEBI:72314)
  Modifiers: DIC"

Error (if any): None

Synthesize a comprehensive answer to the USER QUESTION based on the available data from the map and noting any retrieval issues as instructed in the system prompt. Do not search the web for additional information."
