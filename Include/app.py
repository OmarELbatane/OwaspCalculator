import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 
import webbrowser



class RiskAssessmentApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("OWASP Risk Rating Calculator")
        self.geometry("1400x1000")
        self.configure(bg='lightblue')  
        self.choices = {}
        self.score = 0


        self.section_data = {
            "section1": {
                "title": "Threat Agent Factors",
                "definition": "Technical Impact Factors in cybersecurity assess the impact of a vulnerability exploit in terms of confidentiality, integrity, availability, and accountability.",
                "phrases": {
                    "Skill Level": {
                        " ---------" : 0,
                        " No technical skills": 1,
                        " Some technical skills": 3,
                        " Advanced computer user": 5,
                        " Network and programming skills": 6,
                        " Security penetration skills": 9,
                        " No threat" : 0
                    },
                    "Motive": {
                        " ---------" : 0,
                        " Low or no reward": 1,
                        " Possible reward": 4,
                        " High reward": 9,
                        " No threat" : 0
                    },
                    "Opportunity": {
                        " ---------" : 0,
                        " Full access or expensive resources required": 0,
                        " Special access or resources required": 4,
                        " Some access or resources required": 7,
                        " No access or resources required " : 9,
                        " No threat" : 0
                    },
                    "Size ": {
                        "---------" : 0,
                        " Developers": 2,
                        " System administrators": 2,
                        " Intranet users": 4,
                        " Partners ": 5,
                        " Authenticated users" : 6,
                        " Anonymous Internet users " :9,
                        " No threat" : 0

                    },
                    
                }
            },

            "section2": {
                "title": "Vulnerability Factors",
                "definition": "In cybersecurity, Vulnerability Factors evaluate the likelihood of a vulnerability's discovery and exploitation.",
                "phrases": {
                    "Ease of Discovery": {
                        " ---------" : 0,
                        " Practically impossible": 1,
                        " Difficult ": 3,
                        " Easy ": 7,
                        " Automated tools available": 9,
                        " No threat" : 0
                    },
                    "Ease of Exploit": {
                        " ---------" : 0,
                        " Theoretical": 1,
                        " Difficult": 3,
                        " Easy ": 5,
                        " Automated tools available" : 9,
                        " No threat" : 0
                    },
                    "Awareness ": {
                        " ---------" : 0,
                        " Unknown": 1,
                        " Hidden ": 4,
                        " Obvious  ": 6,
                        " Public knowledge" : 9,
                        " No threat" : 0
                    },
                    "Intrusion Detection ": {
                        " ---------" : 0,
                        " Active detection in application": 1,
                        " Logged and reviewed": 2,
                        " Logged without review  ": 3,
                        " Not logged" : 9,
                        " No threat" : 0
                    },
                }
            },

            "section3": {
                "title": "Technical Impact Factors",
                "definition": "Technical impact in cybersecurity is assessed based on confidentiality, integrity, availability, and accountability.",
                "phrases": {
                    "Loss of Confidentiality": {
                        " ---------" : 0,
                        " Minimal non-sensitive data disclosed": 1,
                        " Minimal critical data disclosed": 2,
                        " Extensive non-sensitive data disclosed": 3,
                        " Extensive critical data disclosed": 4,
                        " All data disclosed": 5,
                        " No threat" : 0
                    },
                    "Loss of Integrity": {
                        " ---------" : 0,
                        " Minimal slightly corrupt data": 1,
                        " Minimal seriously corrupt data ": 2,
                        " Extensive slightly corrupt data": 3,
                        " Extensive seriously corrupt data": 3,
                        " All data totally corrupt ": 2,
                        " No threat" : 0
                    },

                    "Loss of Availability": {
                        " ---------" : 0,
                        " Minimal secondary services interrupted ": 1,
                        " Minimal primary services interrupted ": 2,
                        " Extensive secondary services interrupted": 3,
                        " Extensive primary services interrupted": 3,
                        " All services completely lost": 2,
                        " No threat" : 0
                    },

                    "Loss of Accountability": {
                        " ---------" : 0,
                        " Fully traceable": 1,
                        " Minimal seriously corrupt data ": 2,
                        " Possibly traceable ": 3,
                        " Completely anonymous": 3,
                        " No threat" : 0
                    },

                }
            },


            "section4": {
                "title": "Business Impact Factors",
                "definition": "Business impact in cybersecurity considers financial damage, reputation damage, non-compliance, and privacy violations unique to each company.",
                "phrases": {
                    "Financial damage": {
                        " ---------" : 0,
                        " Less than the cost to fix the vulnerability ": 1,
                        " Minor effect on annual profit ": 3,
                        " Significant effect on annual profit": 7,
                        " Bankruptcy": 9,
                        " No threat" : 0
                    },
                    "Reputation damage": {
                        " ---------" : 0,
                        " Minimal damage": 1,
                        " Loss of major accounts ": 4,
                        " Loss of goodwill": 5,
                        " Brand damage": 9,
                        " No threat" : 0
                    },
                    "Non-compliance": {
                        " ---------" : 0,
                        " Minor violation": 2,
                        " Clear violation ": 5,
                        " High profile violation": 7,
                        " No threat" : 0
                    },
                    "Privacy violation": {
                        " ---------" : 0,
                        " One individual": 3,
                        " Hundreds of people ": 5,
                        " Thousands of people ": 7,
                        " Millions of people ": 9,
                        " No threat" : 0
                    }
                }
            }
        }

        self.create_widgets()

    def create_widgets(self):
        title_label = tk.Label(self, text="OWASP Risk Rating Calculator", font=("Segoe UI", 20, "bold"),bg='lightblue')
        title_label.pack(pady=20)

        for key, data in self.section_data.items():
            self.create_section(key, data["title"], data["phrases"], data["definition"])

        eval_button = tk.Button(self, text="Évaluer le Risque", command=self.evaluate_risk)
        eval_button.pack(pady=10)

        help_button = tk.Button(self, text="For more help, visit the main site by clicking here", command=self.show_help)
        help_button.pack(pady=10)

        # Initialisation de self.total_score_label
        self.total_score_label = tk.Label(self, text="Risk Total: ", font=("Segoe UI", 12), bg='lightblue')
        self.total_score_label.pack(pady=10)

        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, self)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def create_section(self, section_key, title, phrases, definition):
        frame = tk.Frame(self, borderwidth=2, relief=tk.GROOVE, bg='lightblue')
        frame.pack(pady=10, padx=10, fill=tk.X)

        title_label = tk.Label(frame, text=title, font=("Segoe UI", 16, 'bold'), bg='lightblue')
        title_label.pack(side=tk.TOP, padx=10)

        definition_label = tk.Label(frame, text=self.section_data[section_key]["definition"], font=("Segoe UI", 12), bg='lightblue')
        definition_label.pack(side=tk.TOP, padx=10, pady=(0, 10))

        for phrase, options in phrases.items():
            phrase_label = ttk.Label(frame, text=phrase, background='lightblue')
            phrase_label.pack(side=tk.LEFT, padx=10)
            var = tk.StringVar(frame)
            self.choices[f"{section_key}_{phrase}"] = var
            option_menu = ttk.OptionMenu(frame, var, *options.keys())
            option_menu.pack(side=tk.LEFT, padx=10)


    def evaluate_risk(self):
        scores = [0, 0, 0, 0]  # Un score pour chaque section/catégorie
        risk_levels = []

        for key, var in self.choices.items():
            section_key, phrase = key.split("_", 1)
            option_value = self.section_data[section_key]["phrases"][phrase].get(var.get(), 0)
        
            if section_key == "section1":
                scores[0] += option_value
            elif section_key == "section2":
                scores[1] += option_value
            elif section_key == "section3":
                scores[2] += option_value
            elif section_key == "section4":
                scores[3] += option_value

        for i in range(4):
            scores[i] = scores[i]/4

        score1 = (scores[0]+ scores[1])/2
        score2 = max(scores[2], scores[3])
        total_score = score1 * score2 

        total_risk_level = self.determine_risk_level(total_score)
        self.total_score_label.config(text=f"Risk Total: {total_score} \t Risk LEVEL : {total_risk_level}", bg='lightblue')

        for score in scores:
            print(score)
            risk_levels.append(self.determine_risk_level(score))

        self.update_graph(scores, risk_levels)



    def show_help(self):
        webbrowser.open('https://owasp.org/www-community/OWASP_Risk_Rating_Methodology')



    def determine_risk_level(self, score):
        if score <= 3:  
            return "LOW"
        elif 3 < score <= 6:
            return "MEDIUM"
        else:
            return "HIGH"

    def update_graph(self, scores, risk_levels):
        self.ax.clear()
        colors = {"LOW": "green", "MEDIUM": "yellow", "HIGH": "red"}
        categories = ["Threat Agent Factors", "Vulnerability Factors", "Technical Impact Factors", "Business Impact Factors"]

        for i, (score, level) in enumerate(zip(scores, risk_levels)):
            color = colors[level]
            self.ax.bar(categories[i], score, color=color)
            self.ax.text(categories[i], score / 2, f"{score}\n{level.capitalize()}", ha='center', va='center', color='white')

        self.ax.set_yticks(range(0, int(max(scores)) + 1))
        self.ax.set_ylabel("Score et Niveau de Risque")
        self.canvas.draw()



if __name__ == "__main__":
    app = RiskAssessmentApp()
    app.mainloop()
