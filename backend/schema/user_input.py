from pydantic import BaseModel,Field,field_validator,computed_field
from typing import Literal,Annotated,Optional
import pycountry
import pycountry_convert as pc


class UserInput(BaseModel):
    Country:Optional[str] = Field(None, description="Name of the country")
    Year: Optional[int] = Field(None, description="Year of the data")
    Status: Optional[Literal['Developed', 'Developing']] = Field(None, description="Development status of the country")
    Adult_Mortality: Optional[int] = Field(None, description="Adult mortality rate per 1000 population")
    Infant_Deaths: Optional[int] =  Field(None, description="Number of infant deaths per 1000 live births")
    Alcohol: Optional[float] = Field(None, description="Alcohol consumption per capita (in liters)")
    Percentage_Expenditure: Optional[float] = Field(None, description="Percentage of expenditure on health")
    Hepatitis_B: Optional[int] = Field(None, description="Hepatitis B immunization coverage percentage")
    Measles: Optional[int] = Field(None, description="Number of measles cases per 1000 population")
    BMI: Optional[float] = Field(None, description="Body Mass Index (BMI)")
    Under_Five_Deaths: Optional[int] = Field(None, description="Number of under-five deaths per 1000 live births")
    Polio: Optional[int] = Field(None, description="Polio immunization coverage percentage")
    Total_Expenditure: Optional[float] = Field(None, description="Total expenditure on health as a percentage of GDP")
    Diphtheria: Optional[int] = Field(None, description="Diphtheria immunization coverage percentage")
    HIV_AIDS: Optional[float] = Field(None, description="HIV/AIDS death rate per 1000 population")
    GDP: Optional[float] = Field(None, description="Gross Domestic Product (GDP) per capita")
    Population: Optional[int] = Field(None, description="Population of the country")
    Thinness_1_19_years: Optional[float] = Field(None, description="Thinness prevalence among children aged 1-19 years (%)")
    Thinness_5_9_years: Optional[float] = Field(None, description="Thinness prevalence among children aged 5-9 years (%)")
    Income_Composition_of_Resources: Optional[float] = Field(None, description="Income composition of resources (0-1)")
    Schooling: Optional[float] = Field(None, description="Average years of schooling")



    @computed_field
    @property
    def get_continent(self) -> str:
      try:
            country_code = pycountry.countries.lookup(self.Country).alpha_2
            continent_code = pc.country_alpha2_to_continent_code(country_code)
            continent_map = {
                "AF": "Africa",
                "AS": "Asia",
                "EU": "Europe",
                "NA": "North America",
                "SA": "South America",
                "OC": "Oceania",
                "AN": "Antarctica"
            }

            return continent_map[continent_code]
      except:
            return "Unknown"

    @computed_field
    @property
    def continent_code(self)->int:
      if self.get_continent == 'Africa':
        return 1
      elif self.get_continent == 'Asia':
        return 2
      elif self.get_continent == 'Europe':
        return 3
      elif self.get_continent == 'North America':
        return 4
      elif self.get_continent == 'South America':
        return 5
      elif self.get_continent == 'Oceania':
        return 6
      elif self.get_continent == 'Antarctica':
        return 7
      else:
        return 0



    @computed_field
    @property
    def get_status(self) -> int:
      if self.Status== 'Developed':
          return 1
      elif self.Status == 'Developing':
          return 0
      else:
          raise ValueError("Invalid status. Must be 'Developed' or 'Developing'.")

