import requests
import pandas as pd
import time

class FWCAPI():

    @staticmethod
    def __get_result(query_url,hdr,payload):
        response = requests.get(url=query_url,headers=hdr,params=payload)
        response_json = response.json()        
        if response.status_code != 200:
            raise ValueError(response_json['errors'][0]['detail'])
        result_df=pd.DataFrame.from_records([response_json['result']])
        return result_df

    @staticmethod
    def __get_all_results(query_url,hdr,payload):
        response = requests.get(url=query_url,headers=hdr,params=payload)
        response_json = response.json()        
        if response.status_code != 200:
            raise ValueError(response_json['errors'][0]['detail'])
        page_count = response_json['_meta']['page_count']
        result_list=[]
        result_list.append(pd.DataFrame.from_dict(response_json['results']))

        # if # of page >=2, get all pages results
        if(page_count>1):
            for idx in range(2,page_count+1):
                page_paras = {
                    'page' : idx,
                    'limit': 100
                        }
                page_response = requests.get(url=query_url,headers=hdr,params=page_paras).json()
                result_list.append(pd.DataFrame.from_dict(page_response['results']))
                time.sleep(1)
        result_df = pd.concat(result_list)
        return result_df

    def __init__(self,subscription_key):
        """A wrapper for Australian Fair Work Commission Modern Awards API https://uatdeveloper.fwc.gov.au/

        Parameters
        ----------
        subscription_key : string 
            The subscription key used for the API access. You should be able to find it under "Profile" section once you have registered.
        """
        self.key = subscription_key
        self.hdr = {
        'Cache-Control': 'no-cache',
        'Ocp-Apim-Subscription-Key': self.key,
        }
        self.baseurl = "https://uatapi.fwc.gov.au/api/v1/awards"

    def get_awards(self,name,award_operative_from=None,award_operative_to=None):
        """This API is designed to retrieve a list of modern awards to support payroll business processes. https://uatdeveloper.fwc.gov.au/api-details#api=fwc-maapi-v1&operation=GetAwards

        Parameters
        ----------
        name : string
            The human readable title of the award. Example:"mining" returns all awards with the word 'mining' in its title. You can use the plus sign ("+") to add multiple keywords to refine your search. "Mining+Black" will return awards which have the word "mining" AND "black".
        award_operative_from : string, optional
            Format - date-time (as date-time in RFC3339). The date when the award came into operation. The default format is "YYYY-MM-DD", by default None
        award_operative_to : _type_, optional
            Format - date-time (as date-time in RFC3339). The date when the award ceased to be in effect (was revoked). The default format is "YYYY-MM-DD", by default None

        Returns
        -------
        A pandas dataframe
            A list of modern awards
        """
        # construct url
        query_url = f"{self.baseurl}?"

        #construct payload to API
        payload = {}
        payload['name'] = name
        payload['award_operative_from']=award_operative_from
        payload['award_operative_to']=award_operative_to
        payload['limit']=100

        return self.__get_all_results(query_url,self.hdr,payload)

    def get_award(self,id_or_code,award_operative_from=None,award_operative_to=None):
        """This API is designed to retrieve a modern award using the "award_fixed_id" or the award "code" to support payroll business processes. https://uatdeveloper.fwc.gov.au/api-details#api=fwc-maapi-v1&operation=AwardsIdentification

        Parameters
        ----------
        id_or_code : string
            Search by "award_fixed_id" or "code". Example "id_or_code="12" or "id_or_code"="MA000012".
        award_operative_from : string, optional
            Format - date-time (as date-time in RFC3339). The date when the award came into operation. The default format is "YYYY-MM-DD", by default None
        award_operative_to : _type_, optional
            Format - date-time (as date-time in RFC3339). The date when the award ceased to be in effect (was revoked). The default format is "YYYY-MM-DD", by default None

        Returns
        -------
        A pandas dataframe
            A modern award
        """

        # construct url
        query_url = f"{self.baseurl}/{id_or_code}"

        #construct payload to API
        payload = {}
        payload['award_operative_from']=award_operative_from
        payload['award_operative_to']=award_operative_to
        payload['limit']=100

        return self.__get_all_results(query_url,self.hdr,payload)        

    def get_classification(self,id_or_code,classification_fixed_id):
        """This API is designed to retrieve a current individual classification for a specific award using a fixed identifier. https://uatdeveloper.fwc.gov.au/api-details#api=fwc-maapi-v1&operation=IndividualClassification

        Parameters
        ----------
        id_or_code : string
            Search by "award_fixed_id" or "code". Example "id_or_code="12" or "id_or_code"="MA000012".
        classification_fixed_id : string
            Format - int32. Unique identification number of classification that is fixed over each year. Example: "classification_fixed_id"="98".

        Returns
        -------
        A pandas dataframe
            A current individual classification for a specific award
        """
         
        # construct url
        query_url = f"{self.baseurl}/{id_or_code}/classifications/{classification_fixed_id}"

        #construct payload to API
        payload = {}
        payload['limit']=100

        return self.__get_result(query_url,self.hdr,payload)   

    def get_payrates(self,id_or_code,classification_level=None,classification_fixed_id=None,employee_rate_type_code=None,operative_from=None,operative_to=None):
        """This API is designed to retrieve the pay-rates for a given award to support payroll business processes. https://uatdeveloper.fwc.gov.au/api-details#api=fwc-maapi-v1&operation=GetPayRates

        Parameters
        ----------
        id_or_code : string
            Search by "award_fixed_id" or "code". Example "id_or_code="12" or "id_or_code"="MA000012".
        classification_level : string, optional
            Format - int32. A numerical representation of the classification within the hierarchical structure of classifications in a clause. Starts at 1 for the lowest level classification. Example: "classification_level"="1", by default None
        classification_fixed_id : string, optional
            Format - int32. Unique identification number of classification that is fixed over each year. Example "classification_fixed_id"="549", by default None
        employee_rate_type_code : string, optional
            An indicator if the rate is for an adult or otherwise. Go to Documentation Guide, Classification tab for the categories. Search with a comma (",") delimiter to allow multiple codes. Example: "employee_rate_type_code"="AD" or "employee_rate_type_code"="AD,TN", by default None
        operative_from : string, optional
            Format - date-time (as date-time in RFC3339). The date on which the classification came into effect. The default format is "YYYY-MM-DD", by default None
        operative_to : string, optional
            Format - date-time (as date-time in RFC3339). The date on which the classification ceased to be in effect. The default format is "YYYY-MM-DD", by default None

        Returns
        -------
        A pandas dataframe
            The pay-rates for a given award
        """

        # construct url
        query_url = f"{self.baseurl}/{id_or_code}/pay-rates?"

        #construct payload to API
        payload = {}
        payload['classification_level']=classification_level
        payload['classification_fixed_id']=classification_fixed_id
        payload['employee_rate_type_code']=employee_rate_type_code
        payload['operative_from']=operative_from
        payload['operative_to']=operative_to
        payload['limit']=100

        return self.__get_all_results(query_url,self.hdr,payload)       

    def get_classifications(self,id_or_code,classification_level=None,classification_fixed_id=None,operative_from=None,operative_to=None):
        """This API is designed to retrieve award classification information using the "award_ fixed_ id" or the award "code" to support payroll business processes. https://uatdeveloper.fwc.gov.au/api-details#api=fwc-maapi-v1&operation=AwardClassification

        Parameters
        ----------
        id_or_code : string
            Search by "award_fixed_id" or "code". Example "id_or_code="12" or "id_or_code"="MA000012".
        classification_level : string, optional
            Format - int32. A numerical representation of the classification within the hierarchical structure of classifications in a clause. Starts at 1 for the lowest level classification. Example: "classification_level"="1", by default None
        classification_fixed_id : string, optional
            Format - int32. Unique identification number of classification that is fixed over each year. Example "classification_fixed_id"="549", by default None
        operative_from : string, optional
            Format - date-time (as date-time in RFC3339). The date on which the classification came into effect. The default format is "YYYY-MM-DD", by default None
        operative_to : string, optional
            Format - date-time (as date-time in RFC3339). The date on which the classification ceased to be in effect. The default format is "YYYY-MM-DD", by default None

        Returns
        -------
        A pandas dataframe
            Award classification information
        """

        # construct url
        query_url = f"{self.baseurl}/{id_or_code}/classifications?"

        #construct payload to API
        payload = {}
        payload['classification_level']=classification_level
        payload['classification_fixed_id']=classification_fixed_id
        payload['operative_from']=operative_from
        payload['operative_to']=operative_to        
        payload['limit']=100
        
        return self.__get_all_results(query_url,self.hdr,payload)    


        

    def get_current_payrate(self,id_or_code,classification_fixed_id):
        """This API is designed to retrieve the current pay-rate of an individual classification for a specific award using a fixed identifier. Where the query returns more than one result, the default sort is "calculated_pay_rate_id" ascending and then "calculated_rate_type" ascending. https://uatdeveloper.fwc.gov.au/api-details#api=fwc-maapi-v1&operation=IndividualPayRate

        Parameters
        ----------
        id_or_code : string
            Search by "award_fixed_id" or "code". Example "id_or_code="12" or "id_or_code"="MA000012".
        classification_fixed_id : string
            Format - int32. Unique identification number of classification that is fixed over each year. Example "classification_fixed_id"="549".

        Returns
        -------
        A pandas dataframe
            Current pay-rate of an individual classification for a specific award
        """
        # https://uatdeveloper.fwc.gov.au/api-details#api=fwc-maapi-v1&operation=IndividualPayRate
        # construct url
        query_url = f"{self.baseurl}/{id_or_code}/classifications/{classification_fixed_id}/pay-rates?"

        #construct payload to API
        payload = {}
        payload['limit']=100

        return self.__get_all_results(query_url,self.hdr,payload)

    def get_expense_allowance(self,id_or_code,expense_allowance_fixed_id):
        """This API is designed to retrieve a current individual expense-related allowance for a specific award using a fixed identifier. https://uatdeveloper.fwc.gov.au/api-details#api=fwc-maapi-v1&operation=IndividualExpenseAllowance

        Parameters
        ----------
        id_or_code : string
            Search by "award_fixed_id" or "code". Example "id_or_code="12" or "id_or_code"="MA000012".
        expense_allowance_fixed_id : string
            Format - int32. Unique identification number of the expense-related allowance that is fixed over each year. Example "expense_allowance_fixed_id"="9"

        Returns
        -------
        A pandas dataframe
            A current individual expense-related allowance for a specific award
        """

        # construct url
        query_url = f"{self.baseurl}/{id_or_code}/expense-allowances/{expense_allowance_fixed_id}"

        #construct payload to API
        payload = {}
        payload['limit']=100

        return self.__get_result(query_url,self.hdr,payload)        

    def get_expense_allowances(self,id_or_code,allowance_type_code=None,is_all_purpose=None,operative_from=None,operative_to=None):
        """This API is designed to retrieve the expense-related allowance for a specific award using the "award_fixed_id" or the award "code" to support payroll business processes. https://uatdeveloper.fwc.gov.au/api-details#api=fwc-maapi-v1&operation=ExpenseAllowances

        Parameters
        ----------
        id_or_code : string
            Search by "award_fixed_id" or "code". Example "id_or_code="12" or "id_or_code"="MA000012".
        allowance_type_code : string, optional
            Codes used by the ATO for single touch pay roll. Go to the Documentation Guide, Allowance Codes tab for a full list of codes. Search with a comma (",") delimiter to allow multiple codes. Example: "allowance_type_code"="MD" or "allowance_type_code"="MD,CD", by default None
        is_all_purpose : string, optional
            Used to flag whether an allowance applies for all purposes. The default value is null ("--"). Example: "true" or "false", by default None
        operative_from : string, optional
            Format - date-time (as date-time in RFC3339). The date on which the allowance came into effect. The default format is "YYYY-MM-DD", by default None
        operative_to : string, optional
            Format - date-time (as date-time in RFC3339). The date on which the allowance ceased to be in effect. The default format is "YYYY-MM-DD"., by default None

        Returns
        -------
        A pandas dataframe
            The expense-related allowance for a specific award
        """
        
        # construct url
        query_url = f"{self.baseurl}/{id_or_code}/expense-allowances?"

        #construct payload to API
        payload = {}
        payload['allowance_type_code']=allowance_type_code
        payload['is_all_purpose']=is_all_purpose
        payload['operative_from']=operative_from
        payload['operative_to']=operative_to
        payload['limit']=100

        return self.__get_all_results(query_url,self.hdr,payload)        


    def get_penalties(self,id_or_code,penalty_fixed_id=None,classification_level=None,penalty_code=None,employee_rate_type_code=None,base_pay_rate_Id=None,operative_from=None,operative_to=None):
        """This API is designed to retrieve the penalties for a given award using the "award_fixed_id" or award "code" to support payroll business processes. https://uatdeveloper.fwc.gov.au/api-details#api=fwc-maapi-v1&operation=PenaltyModel

        Parameters
        ----------
        id_or_code : string
            Search by "award_fixed_id" or "code". Example "id_or_code="12" or "id_or_code"="MA000012".
        penalty_fixed_id : string, optional
            Format - int32. Unique identification number of the penalty that is fixed over time, by default None
        classification_level : string, optional
            Format - int32. A numerical representation of the classification within the hierarchical structure of classifications in a clause. Starts at 1 for the lowest level classification. Example: "classification_level"="1", by default None
        penalty_code : string, optional
            A 5-digit code used to categorize a penalty rate. Go to the Documentation Guide, Penalty Codes tab for a full list of codes. Search with a comma (",") delimiter to allow multiple codes. Example "penalty_code"="OTFMF" or "penalty_code"="OTFMF,SWTMO", by default None
        employee_rate_type_code : string, optional
            An indicator if the rate is for an adult or otherwise. Go to Documentation Guide, Penalty tab for the categories. Search with a comma (",") delimiter to allow multiple codes. Example: "employee_rate_type_code"="AD" or "employee_rate_type_code"="AD,TN", by default None
        base_pay_rate_Id : string, optional
            A unique identification number of the base pay-rate resource used to calculate the penalty value. Example "basePayRateId=123456", by default None
        operative_from : string, optional
            Format - date-time (as date-time in RFC3339). The date on which the classification came into effect. The default format is "YYYY-MM-DD", by default None
        operative_to : string, optional
            Format - date-time (as date-time in RFC3339). The date on which the classification ceased to be in effect. The default format is "YYYY-MM-DD", by default None

        Returns
        -------
        A pandas dataframe
            The penalties for a given award
        """

        # construct url
        query_url = f"{self.baseurl}/{id_or_code}/penalties?"

        #construct payload to API
        payload = {}
        payload['penalty_fixed_id']=penalty_fixed_id
        payload['classification_level']=classification_level
        payload['penalty_code']=penalty_code
        payload['employee_rate_type_code']=employee_rate_type_code
        payload['base_pay_rate_Id']=base_pay_rate_Id
        payload['operative_from']=operative_from
        payload['operative_to']=operative_to
        payload['limit']=100

        return self.__get_all_results(query_url,self.hdr,payload)        

    def get_wage_allowance(self,id_or_code,wage_allowance_fixed_id):
        """This API is designed to retrieve a current individual wage-related allowance for a specific award using a fixed identifier. https://uatdeveloper.fwc.gov.au/api-details#api=fwc-maapi-v1&operation=IndividualWageAllowance

        Parameters
        ----------
        id_or_code : string
            Search by "award_fixed_id" or "code". Example "id_or_code="12" or "id_or_code"="MA000012".
        wage_allowance_fixed_id : string
            Format - int32. Unique identification number of the wage-related allowance that is fixed over each year. Example: "wage_allowance_fixed_id"="191"

        Returns
        -------
        A pandas dataframe
            A current individual wage-related allowance for a specific award
        """

        # construct url
        query_url = f"{self.baseurl}/{id_or_code}/wage-allowances/{wage_allowance_fixed_id}"

        #construct payload to API
        payload = {}
        payload['limit']=100

        return self.__get_result(query_url,self.hdr,payload)        

    def get_wage_allowances(self,id_or_code,allowance_type_code=None,is_all_purpose=None,operative_from=None,operative_to=None):
        """This API is designed to retrieve the wage-related allowance for a specific award using the "award_fixed_id" or the award "code" to support payroll business processes. https://uatdeveloper.fwc.gov.au/api-details#api=fwc-maapi-v1&operation=WageAllowanceModel

        Parameters
        ----------
        id_or_code : string
            Search by "award_fixed_id" or "code". Example "id_or_code="12" or "id_or_code"="MA000012".
        allowance_type_code : string, optional
            Codes used by the ATO for single touch pay roll. Go to the Documentation Guide, Allowance Codes tab for a full list of codes. Search with a comma (",") delimiter to allow multiple codes. Example: "allowance_type_code"="MD" or "allowance_type_code"="MD,CD", by default None
        is_all_purpose : string, optional
            Used to flag whether an allowance applies for all purposes. The default value is null ("--"). Example: "true" or "false", by default None
        operative_from : string, optional
            Format - date-time (as date-time in RFC3339). The date on which the allowance came into effect. The default format is "YYYY-MM-DD", by default None
        operative_to : string, optional
            Format - date-time (as date-time in RFC3339). The date on which the allowance ceased to be in effect. The default format is "YYYY-MM-DD"., by default None

        Returns
        -------
        A pandas dataframe
            The wage-related allowance for a specific award
        """
        
        # construct url
        query_url = f"{self.baseurl}/{id_or_code}//wage-allowances?"

        #construct payload to API
        payload = {}
        payload['allowance_type_code']=allowance_type_code
        payload['is_all_purpose']=is_all_purpose
        payload['operative_from']=operative_from
        payload['operative_to']=operative_to
        payload['limit']=100

        return self.__get_all_results(query_url,self.hdr,payload)    