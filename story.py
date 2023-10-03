import time

def typewriter_effect(text, delay=0.035):
    for char in text:
        print(char, end='', flush=True)  
        time.sleep(delay)  
    print() 

# need to add: start again from the beginning, go to previous input. 
# Interactive Horror Story
# Setting and Introduction
typewriter_effect("You wake up from a heavy sleep, still tired. Your eyes don't seem to open, but the monster residing in your stomack, the anxiety, urges to get out of bed and face the looming dread of the day ahead.")
typewriter_effect("You merely want to survive...")
typewriter_effect("Alarms, beeping notifications, calendar reminders...every single sound is there just to remind you that you, and only you, made this choice.")
typewriter_effect("You are PhD student.")
typewriter_effect("And this is a horror story.")
typewriter_effect("You force yourself to get out of bed to make some breakfast.")

typewriter_effect("Reluctantly, you shuffle to the kitchen, your steps heavy.")
typewriter_effect("As you barely manage to nibble on a couple of biscuits, an eerie silence fills the room, and your phone suddenly starts ringing.")
typewriter_effect("Each ring sends a shiver down your spine. Do you dare to pick up the phone?")

while True:
    phoneChoice = input("> ").lower()

    if(phoneChoice == "yes"):
        typewriter_effect("Your trembling hand reaches for the phone.")
        typewriter_effect("On the other side of the line, your collegue Elena sounds agitated and asks you why you aren't in the group meeting checking if you received the email about the time-change.")
        typewriter_effect("You start panicking and you, desparetely, ask if you can make it in time now.")
        typewriter_effect("She gravely responds 'barely'.")
        typewriter_effect("You're getting ready as fast as you can.")
        typewriter_effect("You exit your place and you get to the bus stop. The screen says 20 minutes until the next bus.")
        typewriter_effect("Calculations are running in your mind. You can hear your heart pounding in your chest.")
        typewriter_effect("A sense of confidence is overflowing your body, thinking that you can make it on time if you run there instead of waiting for the bus.") 
        typewriter_effect("Do you listen to that feeling?")
        
        while True:
            runOrnot = input("> ").lower()

            if(runOrnot == "yes"):
                typewriter_effect("You start to run as fast as you can.")
                typewriter_effect("Your mind is racing with bleak thoughts. How can you be so irresponsible? You don't deserve the PhD title. You are a disappointment.")
                typewriter_effect("As you are getting closer to the department, you notice the sky is dark gray, while the streets are slippery with stale dirt and rain.")
                typewriter_effect("You are finally there! Unable to catch your breath, you can feel the arteries in your stomach palpitating and your vains contracting. You vomit.")
                typewriter_effect("You have no time to wash up so wipe your mouth with your shirt, leaving saffron-yellow stains.")
                typewriter_effect("Once you open the door of the conference room, you feel a cold air hit your face.")
                typewriter_effect("All eyes turn on you. You can feel their annoyance, their disgust. Why did you even bother coming?")
                typewriter_effect("You take a spare seat and you supervisor glares at you, waiting for you to say something. You apologise.")
                typewriter_effect("He says that next time you are late you are out.") 
                typewriter_effect("No sentiment in his tone. He then changes the topic and asks you if you can take a final look at the paper your group is working on and to present it in case it's accepted.") 
                typewriter_effect("Do you accept?")
                

                while True:
                    paperChoice = input("> ").lower()

                    if(paperChoice == "yes"):
                        typewriter_effect("You accept to take a final look at the paper and be the presenter.")
                        typewriter_effect("To your disappointment, you notice many formatting issues. Terrifying typos, irrelevant citations, and worst of all...plagiarism.")
                        typewriter_effect("Working until the small hours, you manage to save the manuscript and bring it into a decent form before the submission.")
                        typewriter_effect("A few weeks later, the response arrives.")
                        typewriter_effect("Your paper is accepted")
                        typewriter_effect("On the day of the conference you drive to the North of Italy to attend and present at the conference.")
                        typewriter_effect("The time has come and the you still don't feel ready despite having rehearsed a million times.")
                        typewriter_effect("The spotlight is on you now. You swallow your saliva and you start talking.") 
                        typewriter_effect("The words flow easier than you thought. You can feel the audience excited and perplexed. You have grabbed their attention.")
                        typewriter_effect("Your mouth feels dry and every word is harder to enunciate because of the thirst.")
                        typewriter_effect("You see there is a bottle of water in front of you.") 
                        typewriter_effect("Do you drink and interrupt your flow or do you wait until the end of your presentation?")

                        

                        while True:
                            waterChoice = input("> ").lower()

                            if(waterChoice == "drink water"):
                                typewriter_effect("As you anxiously swallow the water, it goes down the wrong pipe, causing you to choke and tragically lose your life as someone who could not even finish their PhD.") 
                                typewriter_effect("You died a failure!")
                                break

                            elif(waterChoice == "wait"):
                                typewriter_effect("Congratulations, you might not be a pawn of your physical needs but you are definitely a pawn of academia!")
                                typewriter_effect("Your paper is cited a zillion times and you will soon be on tenure track!")

                                break
                            
                            else:
                                typewriter_effect("Invalid answer. Enter 'drink water' or 'wait'.")

                        break

                    elif(paperChoice == 'no'): 
                        typewriter_effect("You take a moment to decide, haunted by all the times they forced you into fruitless labor just to churn out publications.")
                        typewriter_effect("You've had enough with these borderline pseudoscientific practices that drain your soul.")
                        typewriter_effect("You muster every ounce of courage you have left and you firmly reply 'No'.")
                        typewriter_effect("Your supervisor looks at you in the eye with a gaze that you cannot classify as dissappointment or disdainyet he adds your name to the list of authors for your contributions.")
                        typewriter_effect("The paper is presented by a collegue of yours, but you soon find out that it is riddled with plagiarism, and now you must face the dire consequences.")
                        typewriter_effect("As a poor student with no means to bail yourself out, you end up in jail, withering your life away, writing equations onto the grimy walls of your cell.")

                        break
                break

            elif(runOrnot == "no"):
                typewriter_effect("You look at the time and you decide to wait for the bus.")
                typewriter_effect("You fix your eyes on the timetable wishing that the minutes will start passing faster, defying the laws of the universe.")
                typewriter_effect("To your suprise, the bus is on-time. You validate your ticket and you take a seat. You should be in the department in 15 minutes.")
                typewriter_effect("Suddenly, the bus stops. A cold silence falls in the crowded vehicle when a police officer enters. He announces that there has been a suicide.")
                typewriter_effect("A young female student ended her life by jumping from the emblemantic tower of the city. The streets will be closed until further notice.")
                typewriter_effect("You take a look from the window. Besides the police you also notice an ambulance, and a cleaning service.")
                typewriter_effect("You cynically think to yourself, 'someone has to clean up all this blood and scattered brains'.")
                typewriter_effect("You start thinking whether you should continue on foot or wait until the streets open again. What do you do?")

                while True:
                    footOrbus = input("> ").lower()

                    if footOrbus == 'go on foot':
                        typewriter_effect("As you jump off the bus, a chilling sensation creeps up your spine.")
                        typewriter_effect("You can feel your phone vibrating in your pocket, and as you pull it out, your heart sinks.")
                        typewriter_effect("It's your supervisor. His voice trembles as he announces that the meeting is finished and that he is very disappointed in you.")
                        typewriter_effect("He wants to terminate the collaboration. You can hear the anger in his voice.")
                        typewriter_effect("Desperation sets in as you try to convince him otherwise, but you soon realise it's futile.")
                        typewriter_effect("In a flash, your dreams in academia crumble, and a sense of dread fills the air.")
                        typewriter_effect("You're forced into the unforgiving industry.")
                        typewriter_effect("Time slips away as you find yourself trapped in a world you never wanted to be a part of, haunted by your past mistakes.")
                        typewriter_effect("You never manage to escape the dystopia of the industry. Thinking that you are nothing but a pawn of capitalism, you commit suicide at the age of 27.")

                        break
                    
                    elif(footOrbus == 'wait in the bus'):
                        typewriter_effect("As you are waiting in the bus you can feel your phone vibrating in your pocket.")
                        typewriter_effect("It's your supervisor. He announces that the meeting is finished and that he is very dissappointed in you.")
                        typewriter_effect("He wants to terminate the collaboration.")
                        typewriter_effect("You are trying to convince him otherwise, but you fail.")
                        typewriter_effect("Going into the industry is not an option for you so you return back to your town, where you become a tractor driver.")

                        break

                    else:
                        typewriter_effect("Invalid choice. Enter 'go on foot' or 'wait in the bus'.")
            
                break

            else:
                ("Invalid answer. Choose yes or no")

        break 

    elif(phoneChoice == "no"):
        typewriter_effect("You decide to ignore it as it is still very early and you would like to spend some relaxing time by yourself.")
        typewriter_effect("The silence in the room feels unnerving as you savor your plain breakfast, the only sound being the faint ticking of the clock.")
        typewriter_effect("With your breakfast finished, you move to your dimly lit desk, you open your laptop, and you check your emails.")
        typewriter_effect("As the screen lights up, you see an email that mentions a time-change in the meeting you have today. You check the clock and you see that it's way past that time.")
        typewriter_effect("You stomack ties into a knot as you realize the dreadful consequences of your negligence.")
        typewriter_effect("Your mind is torn between being honest with your collegues or making up and excuse")
        typewriter_effect("What do you do?")

        while True:
            excuseOrnot = input("> ").lower()

            if(excuseOrnot == "be honest"):
                typewriter_effect("You choose to be honest.")
                typewriter_effect("Your palms all sweaty and your breathing heavy. You click the MS Teams logo on your flickering screen.")
                typewriter_effect("Your supervisor is online. You call. He picks up. His voice is grim, devoid of life.")
                typewriter_effect("He doesn't grant you a chance to speak.")
                typewriter_effect("With a cold tone, he tells you he's had enough of inadequate candidates and that failing to do the bare minimum means that you are not cut for the job.") 
                typewriter_effect("He ends your collaboration.")
                
                typewriter_effect("Your heart shatters in million pieces. All those years of studying and trying were in vain.")
                typewriter_effect("You decide do go on a walk to clear your head. You don't notice a speeding bicycle racing towards your path.")
                typewriter_effect("The collision leaves you in a vegetative state for a year. On your 27th birthday, they finally pull the plug...")
                break

            elif(excuseOrnot == "make up excuse"):
                typewriter_effect("You decide to make up an excuse.")
                typewriter_effect("You can feel the blood rising to your head. You need to keep calm and convince them.")
                typewriter_effect("Your frail fingers nervously start typing. Drops of sweat fall on the keyboard. You can feel you neck hot.")
                typewriter_effect("'Dear all, I am deeply sorry to inform you that I was involved in a minor car accident in the heart of the city.")
                typewriter_effect("Fortunately, I am safe and sound. I am very sorry that I missed today's meeting and I promise I will make it up to all of you next time.")
                typewriter_effect("Thanks for understanding.'")
                typewriter_effect("You hit 'send'")
                typewriter_effect("Moments later you receive a call.  It's the department's secretary. She delivers the news that you must now find a new supervisor.")
                typewriter_effect("You are in shock. What could have gone wrong?")
                typewriter_effect("Later in the day, you receive an email from your supervisor. He explains that it would have been impossible to have been in a car accident")
                typewriter_effect("as all the streets were closed that day because a girl commited suicide by jumping from a tower in the center of the city.")
                typewriter_effect("You beg for forgiveness but your supervisor is adamant.")
                typewriter_effect("As academia doesn't work out for you, and you are refusing to go into the industry, you turn into music by buskering")
                typewriter_effect("around the city until you die from heroin overdose.")
            

                break
            else:
                typewriter_effect("Invalid answer. Choose 'be honest' or 'make up excuse'.")


        break
    else:
        typewriter_effect("Invalid choice. Enter yes or no.")

