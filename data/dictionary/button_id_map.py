button_id_map = {
    # Applied I
    'Applied_I_course_outline': [7],
    'Applied_I_lecture': list(range(9, 26)),
    'Applied_I_text_book': list(range(27, 66)),
    'Applied_I_exam': list(range(67, 101)),
    'Applied_I_video': [],

    # General Physics
    'General_Physics_course_outline': [105],
    'General_Physics_lecture': list(range(510, 517)) + list(range(107, 112)) + list(range(357, 365)),
    'General_Physics_text_book': list(range(113, 153)),
    'General_Physics_exam': list(range(154, 172)) + list(range(366, 393)),
    'General_Physics_video': [],

    # Civics & Ethics
    'Civics_&_Ethics_course_outline': [301],
    'Civics_&_Ethics_lecture': list(range(303, 332)) + list(range(454, 480)),
    'Civics_&_Ethics_text_book': list(range(333, 342)) + list(range(481, 487)),
    'Civics_&_Ethics_exam': list(range(343, 352)) + list(range(489, 509)),
    'Civics_&_Ethics_video': [],

    # General Chemistry
    'General_Chemistry_course_outline': [237],
    'General_Chemistry_lecture': list(range(239, 261)) + list(range(434, 448)),
    'General_Chemistry_text_book': list(range(262, 271)) + list(range(450, 454)),
    'General_Chemistry_exam': list(range(272, 297)) + list(range(416, 433)),
    'General_Chemistry_video': [],

    # Communicative English
    'Communicative_English_course_outline': [],
    'Communicative_English_lecture': [519, 520, 518],
    'Communicative_English_text_book': [],
    'Communicative_English_exam': [],
    'Communicative_English_video': [],

    # Introduction to Computing (Python)
    'Introduction_to_computing_course_outline': [176],
    'Introduction_to_computing_lecture': list(range(178, 201)),
    'Introduction_to_computing_text_book': list(range(202, 211)) + list(range(396, 399)),
    'Introduction_to_computing_exam': list(range(212, 227)) + list(range(400, 414)),
    'Introduction_to_computing_video': [228, 229],
    'Introduction_to_computing_tool': [230],
    'Introduction_to_computing_lab': [232],
    'Introduction_to_project': [234],

    # Applied II (Second Semester)
    'Applied_II_course_outline': [],
    'Applied_II_lecture': [972, 973],
    'Applied_II_text_book': [],
    'Applied_II_exam': [],
    'Applied_II_video': [],
    'engineering_Applied_II_course_outline': [847],
    'engineering_Applied_II_lecture': list(range(849, 859)),
    'engineering_Applied_II_text_book': list(range(867, 876)),
    'engineering_Applied_II_exam': list(range(877, 888)),
    'engineering_Applied_II_video': list(range(889, 935)),


    # Applied Mathematics I
    'Applied_Math_I_course_outline': [1],
    'Applied_Math_I_lecture': list(range(2, 18)),
    'Applied_Math_I_text_book': list(range(19, 50)),
    'Applied_Math_I_exam': list(range(51, 80)),
    'Applied_Math_I_video': [],

    # Engineering Drawing I
    'Engineering_Drawing_I_course_outline': [201],
    'Engineering_Drawing_I_lecture': list(range(203, 228)),
    'Engineering_Drawing_I_text_book': list(range(229, 254)),
    'Engineering_Drawing_I_exam': list(range(255, 280)),
    'Engineering_Drawing_I_video': [],

    # Digital Logic Design
    'Digital_Logic_Design_course_outline': [301],
    'Digital_Logic_Design_lecture': list(range(303, 340)),
    'Digital_Logic_Design_text_book': list(range(341, 370)),
    'Digital_Logic_Design_exam': list(range(371, 395)),
    'Digital_Logic_Design_video': [],

    # Object-Oriented Programming (Java)
    'Object_Oriented_Programming_course_outline': [401],
    'Object_Oriented_Programming_lecture': list(range(403, 440)),
    'Object_Oriented_Programming_text_book': list(range(441, 470)),
    'Object_Oriented_Programming_exam': list(range(471, 490)),
    'Object_Oriented_Programming_video': [],

    # Data Structures and Algorithms
    'Data_Structures_Algorithms_course_outline': [501],
    'Data_Structures_Algorithms_lecture': list(range(503, 530)),
    'Data_Structures_Algorithms_text_book': list(range(531, 560)),
    'Data_Structures_Algorithms_exam': list(range(561, 590)),
    'Data_Structures_Algorithms_video': [],

    # Database Systems
    'Database_Systems_course_outline': [601],
    'Database_Systems_lecture': list(range(603, 630)),
    'Database_Systems_text_book': list(range(631, 660)),
    'Database_Systems_exam': list(range(661, 690)),
    'Database_Systems_video': [],

    # Operating Systems
    'Operating_Systems_course_outline': [701],
    'Operating_Systems_lecture': list(range(703, 730)),
    'Operating_Systems_text_book': list(range(731, 760)),
    'Operating_Systems_exam': list(range(761, 790)),
    'Operating_Systems_video': [],

    # Software Engineering
    'Software_Engineering_course_outline': [801],
    'Software_Engineering_lecture': list(range(803, 830)),
    'Software_Engineering_text_book': list(range(831, 860)),
    'Software_Engineering_exam': list(range(861, 890)),
    'Software_Engineering_video': [],

    # Networks & Communication
    'Networks_Communication_course_outline': [901],
    'Networks_Communication_lecture': list(range(903, 930)),
    'Networks_Communication_text_book': list(range(931, 960)),
    'Networks_Communication_exam': list(range(961, 990)),
    'Networks_Communication_video': [],

    # Signals and Systems
    'Signals_Systems_course_outline': [1001],
    'Signals_Systems_lecture': list(range(1003, 1030)),
    'Signals_Systems_text_book': list(range(1031, 1060)),
    'Signals_Systems_exam': list(range(1061, 1090)),
    'Signals_Systems_video': [],

    # Microprocessor and Assembly Language
    'Microprocessor_Assembly_course_outline': [1101],
    'Microprocessor_Assembly_lecture': list(range(1103, 1130)),
    'Microprocessor_Assembly_text_book': list(range(1131, 1160)),
    'Microprocessor_Assembly_exam': list(range(1161, 1190)),
    'Microprocessor_Assembly_video': [],

    # Embedded Systems
    'Embedded_Systems_course_outline': [1201],
    'Embedded_Systems_lecture': list(range(1203, 1230)),
    'Embedded_Systems_text_book': list(range(1231, 1260)),
    'Embedded_Systems_exam': list(range(1261, 1290)), 
    'Embedded_Systems_video': [],

    # Artificial Intelligence
    'Artificial_Intelligence_course_outline': [1301],
    'Artificial_Intelligence_lecture': list(range(1303, 1330)),

    'Artificial_Intelligence_text_book': list(range(1331, 1360)),
    'Artificial_Intelligence_exam': list(range(1361, 1390)),
    'Artificial_Intelligence_video': [],

    # Computer Architecture
    'Computer_Architecture_course_outline': [1401],
    'Computer_Architecture_lecture': list(range(1403, 1430)),
    'Computer_Architecture_text_book': list(range(1431, 1460)),
    'Computer_Architecture_exam': list(range(1461, 1490)),
    'Computer_Architecture_video': [],

    # Competitive Programming
    'competitive_programming_description': 'https://t.me/c/2062416584/2',
    'competitive_programming_book': list(range(47, 60)),
    'competitive_programming_club': [
        'https://t.me/CSEC_ASTU',
        'https://t.me/A2SVDiscussion'
    ],
    'competitive_programming_site': [
        'https://codeforces.com/',
        'https://leetcode.com/',
        'https://open.kattis.com/'
    ],
    'competitive_programming_advisor': [
        'Nasiha Abdella CSE 0941290901',
        'Amina Yassin CSE 0934012312'
    ],

}