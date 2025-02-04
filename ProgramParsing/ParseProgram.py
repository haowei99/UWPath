from Database import DatabaseConnection
from ProgramParsing.MajorParser import MajorParser

if __name__ == "__main__":
    files = ["RequiredCSMajor.html", "RequiredActsciMajor.html", "RequiredCFMMajor.html", "RequiredSTATMajor.html",
             "RequiredAPPLIEDMajor.html", "RequiredAMATH-SCI-COMP-Major.html", "RequiredCOMajor.html",
             "RequiredPMATHTeachingMajor.html", "RequiredBiostatisticsMajor.html", "RequiredMATH-Finance-Major.html",
             "RequiredComputationalMATHMajor.html", "RequiredMATHStudiesMajor.html",
             "RequiredAISpecialization.html", "RequiredBioinformaticsSpecialization.html",
             "RequiredBusinessSpecialization.html", "RequiredFineArtSpecialization.html",
             "RequiredSoftwareSpecialization.html", "RequiredMATH-MS-Business-Specialization.html", "RequiredDigitalHardware.html", "RequiredACTSCIJoint.html",
             "RequiredAMATHJoint.html", "RequiredCSJoint.html",
             "RequiredACTSCI-FINANCE-Option.html"]

    #below files are not parsable because "One of.." doesn not beong to a <p> tag
        #RequiredHumanComputerInteractionSpecialization.html
        #RequiredACTSCI-PredictiveAnalysis-Option.html
        #RequiredDATASciMajor.html
    # below files are not parsable because COMPLETELY DIFF FORMAT
        #RequiredAMATHBiologySpecialization.html
        #RequiredAMATHEconSpecialization.html
        #Engineering Specialization: Heat and Mass Transfer
        #Physics Specialization
        #Mathematical Economics
        #Mathematics/Business Administration
        #Mathematics/Chartered Professional Accountancy (co-op only)
        #Mathematical Optimization has three different specialization in one page
        #Mathematics/Financial Analysis and Risk Management


    #Title has Degreee Requiremnt
        #Mathematical Economics
        #Information Technology Management

    #MINOR PROBLEM
    # "RequiredCOJoint.html" is not consistent... "Threee of" is not embedded in <p> MINOR
    # RequiredMATH-Finance-Major.html is not consistent "One of" is not in <p>
    # RequiredMATHCPAFINMajor.html (Mathematics/Chartered Professional Accountancy (co-op only)) "Two of" is not in <p>
    # RequiredPMATHJoint.html, Need to parse "Three additional PMATH courses. #TODO URGENT
    # "RequiredPMATHMajor.html" cannot get additional requirments
    # RequiredMATHTeachingMajor.html "Additional Req is not in <p> but in big <span>

    #Engineering Specialization: Communication and Control is not available
    #Joint Computer Science is not available

    #TODO parse which specialization is under which major

    #continue with Data Science
    #files = ["RequiredMATHCPAFINMajor.html"] #use this for single files


    dbc = DatabaseConnection()

    dbc.create_requirements()

    for file in files:
        parser = MajorParser()
        parser.load_file(file)

        print(parser)

        # Parser requirement is a list of MajorReq Object
        dbc.insert_requirements(parser.requirement)

        dbc.commit()

    dbc.close()