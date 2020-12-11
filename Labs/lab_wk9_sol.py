# course: Object-oriented programming, year 2, semester 1
# academic year: 2020-21
# author: B. Schoen-Phelan
# date: 13-11-2020
# purpose: A solution to the word games lab exercise


class Student:
    """
    The component class of the composition.
    This class contains data about the student.
    ...
    Attributes:
    -----------
        UNDERGRADUATE, POSTGRADUATE : range(2)
        Used to define the level of a study of a student.
        These are class variables. Usage via class name.
        Example: Student.UNDERGRADUATE

        __study_type : range(2)
        Allowed are only the predefined Student.UNDERGRADUATE
        and Student.POSTGRADUATE class variables.

        __f_name : str
        First name of a student.

        __l_name : str
        last name of a student

        __courses : list
        contains a list of courses that a student is enrolled into
        empty by default


    Methods:
    --------
        study_type : property
            returns self.__study_type which is ("UNDERGRADUATE", "POSTGRADUATE")
            available as setter
            raises a ValueError if the supplied value does not match the tuple

        student_name : property
            returns self.__f_name, self.__l_name
            available as a setter that expects first and last name
            in this sequence in a list
            raises a TypeError if the names are not supplied in a list data type

        courses : property
            returns self.__courses which is of type list
            available as a setter that adds a string value to the
            self.__courses list
            raises a TypeError if the supplied names are not in a str type

        get_all_student_data : property
            arguments: none
            returns all information from
            self.student_name, self.study_type, self.course
    """
    # STUDY_TYPE = ("UNDERGRADUATE", "POSTGRADUATE")
    UNDERGRADUATE, POSTGRADUATE = range(2)

    def __init__(self, study_type, f_name, l_name):

        # if study_type not in Student.STUDY_TYPE:
        if study_type not in (Student.POSTGRADUATE, Student.UNDERGRADUATE):
            raise ValueError

        self.__study_type = study_type
        self.__f_name = f_name
        self.__l_name = l_name
        self.__courses = []

    # extra dunder method in order to return the object's content as a string
    # rather than returning the object memory location
    def __str__(self):
        return f"{self.student_name} {self.study_type} {self.courses}"

    @property
    def study_type(self):
        return self.__study_type

    @study_type.setter
    def study_type(self, value):
        # if value not in Student.STUDY_TYPE:
        if value not in (Student.UNDERGRADUATE, Student.POSTGRADUATE):
            raise ValueError

        self.__study_type = value

    @property
    def student_name(self):
        return self.__f_name, self.__l_name

    @student_name.setter
    def student_name(self, value):
        if type(value) != list:
            raise TypeError

        self.__f_name = value[0]
        self.__l_name = value[1]

    @property
    def courses(self):
        return self.__courses

    @courses.setter
    def courses(self, value):
        if type(value) != str:
            raise TypeError

        self.__courses.append(value)

    # because we are returning only attributes and do
    # nothing else with them, we could and probably should
    # make this method a property
    # if you do that, remove the () in the call further down
    def get_all_student_data(self):
        return self.student_name, self.study_type, self.courses



class RegistrationData:
    """
    The composite class. Creates a student object in its init function.

    Attributes:
    -----------
        __address : str
            Student address as one string data type

        __registration_fee : int
            Fee to pay

        __s_id : str
            A student's student ID. Is only assigned later.
            Default is "NA"

        __student_obj : Student
            Student Object, takes study_type, first name and last name
            as arguments.

    Methods:
    --------
        student_object_property : property
            returns __student_obj

        student_id_property : property
            returns __s_id
            available as a setter method. Will raise a TypeError
            if the student ID is not supplied as a string.

        address_property : property
            returns __address
            available as a setter.

        registration_fee_property : property
            returns __registration_fee
            available as a setter

        display_student_data
            no arguments
            no returns
            prints all available information about the student to screen
    """
    def __init__(self, address, registration_fee, study_type, f_name, l_name, s_id="NA"):
        self.__address = address
        self.__registration_fee = registration_fee
        self.__s_id = s_id
        try:
            self.__student_obj = Student(study_type, f_name, l_name)  # object of student class
        except Exception as e:
            pass


    @property
    def student_object_property(self):
        return self.__student_obj

    @property
    def student_id_property(self):
        return self.__s_id

    @student_id_property.setter
    def student_id_property(self, value):
        if type(value) != str:
            raise TypeError

        self.__s_id = value

    @property
    def address_property(self):
        return self.__address

    @address_property.setter
    def address_property(self, value):
        self.__address = value

    @property
    def registration_fee_property(self):
        return self.__registration_fee

    @registration_fee_property.setter
    def registration_fee_property(self, value):
        self.__registration_fee = value

    def display_student_data(self):
        print("Student Info: ", self.student_object_property.get_all_student_data(), self.student_id_property)
        print("Address: ", self.address_property)
        print("Registration fee: ", self.registration_fee_property)




r = RegistrationData("8 Lower Kevin Street, Dublin 8, Ireland", 1500,
                     Student.POSTGRADUATE, "Bianca", "Phelan")
r.display_student_data()
r.student_id_property="C12345"
r.display_student_data()
for course in ("OOP", "Advanced Databases", "Environmental Analytics"):
    r.student_object_property.courses = course

r.display_student_data()
print(r.student_object_property)   #extra to match the __str__ additional function
# print(RegistrationData.__doc__)
