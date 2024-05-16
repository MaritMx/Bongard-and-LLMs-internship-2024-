This GitHub stores the files used by the internship project of Marit Metz in which we compare the abstract reasoning abilities on Bongard problems between vision language models (GPT, Gemini, LLaVA), adults, and children. 

**This GitHub contains the following files:**


- Cleaned individual squares.zip = a zip file containing the individual squares of the CLEANED Bongard problems. Created using the extracting_images_loop.py script. Named like p0{BP number} {set number} {column number} {row number}. 

- Cleaned original BPs.zip = a zip file containing all CLEANED Bongard problems.

- GPT data collection = a file containing the open-ended and multiple-choice messages to the OpenAI API. 

- Individual squares.zip == a zip file containing the individual squares of the UNCLEANED Bongard problems. Created using the extracting_images_loop.py script. Named like p0{BP number} {set number} {column number} {row number}.

- Original BPs.zip = a zip file containing all original, UNCLEANED, Bongard problems.

- extracting images loop.py = script to extract the individual squares from a Bongard problem. Note the different size parameters for cleaned and uncleaned Bongard problems.

- mc_neither_stimuli_selection.py = script to randomly select 1 of 3 possible neither stimuli options per multiple-choice BP item.

- splitting images in 2.py =  a script to split the newly created BPs into left and right parts to be able to use them in the API prompts. 

- version_creator_MC_BPs = file to create the multiple-choice versions of a selected set of BPs using the cleaned individual squares. Creates a total of 7 versions of each BP in the problem_sets, with each version having 3 orientations. Also stores a stimulus for both of the sets in all orientations. 

- version_creator_open-ended_BPs.py = script to create open-ended versions of the BPs using cleaned individual squares. Creates 5 additional versions of each BP item. 
 
