pyfwc
=======================

A simple python wrapper for Australian Fair Work Commission API (https://uatdeveloper.fwc.gov.au/)

Requirements
-----

1. Register on the [official website](https://uatdeveloper.fwc.gov.au/) and obtain a subscription key
2. Install package by the following command:
`pip install pyfwc`

Usage
-----

Create FWC API object


```python
from pyfwc import FWCAPI
fwc = FWCAPI(YOUR_SUBSCRIPTION_KEY)
```

Award
-----

Retrieve all awards for the specified parameters


```python
fwc.get_awards(name='mining')
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>award_id</th>
      <th>award_fixed_id</th>
      <th>code</th>
      <th>name</th>
      <th>award_operative_from</th>
      <th>award_operative_to</th>
      <th>version_number</th>
      <th>last_modified_datetime</th>
      <th>published_year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1132</td>
      <td>1</td>
      <td>MA000001</td>
      <td>Black Coal Mining Industry Award 2020</td>
      <td>2010-01-01T00:00:00+00:00</td>
      <td>None</td>
      <td>3</td>
      <td>2022-01-17T16:12:10+00:00</td>
      <td>2021</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1142</td>
      <td>11</td>
      <td>MA000011</td>
      <td>Mining Industry Award 2020</td>
      <td>2010-01-01T00:00:00+00:00</td>
      <td>None</td>
      <td>2</td>
      <td>2022-01-20T15:49:41+00:00</td>
      <td>2021</td>
    </tr>
  </tbody>
</table>
</div>



Retrieve specific award using an award identifier


```python
fwc.get_award(id_or_code='MA000001').head(3)
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>award_id</th>
      <th>award_fixed_id</th>
      <th>code</th>
      <th>name</th>
      <th>award_operative_from</th>
      <th>award_operative_to</th>
      <th>version_number</th>
      <th>last_modified_datetime</th>
      <th>published_year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>1</td>
      <td>MA000001</td>
      <td>Black Coal Mining Industry Award 2020</td>
      <td>2010-01-01T00:00:00+00:00</td>
      <td>None</td>
      <td>3</td>
      <td>2022-01-17T16:12:10+00:00</td>
      <td>2021</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>1</td>
      <td>MA000001</td>
      <td>Black Coal Mining Industry Award 2020</td>
      <td>2010-01-01T00:00:00+00:00</td>
      <td>None</td>
      <td>3</td>
      <td>2021-06-26T11:33:16+00:00</td>
      <td>2020</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0</td>
      <td>1</td>
      <td>MA000001</td>
      <td>Black Coal Mining Industry Award 2020</td>
      <td>2010-01-01T00:00:00+00:00</td>
      <td>None</td>
      <td>3</td>
      <td>2019-10-23T11:12:07+00:00</td>
      <td>2019</td>
    </tr>
  </tbody>
</table>
</div>



Classifications
-----

Retrieve a current individual classification using a fixed identifier.


```python
fwc.get_classification(id_or_code='MA000002',classification_fixed_id='98')
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>classification_fixed_id</th>
      <th>clause_fixed_id</th>
      <th>clauses</th>
      <th>clause_description</th>
      <th>parent_classification_name</th>
      <th>classification</th>
      <th>classification_level</th>
      <th>next_down_classification_fixed_id</th>
      <th>next_up_classification_fixed_id</th>
      <th>operative_from</th>
      <th>operative_to</th>
      <th>version_number</th>
      <th>last_modified_datetime</th>
      <th>published_year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>98</td>
      <td>3</td>
      <td>16.1</td>
      <td>Clerical Employees</td>
      <td>None</td>
      <td>Level 1—Year 1</td>
      <td>1</td>
      <td>None</td>
      <td>99</td>
      <td>2021-07-01T00:00:00+00:00</td>
      <td>None</td>
      <td>1</td>
      <td>2022-03-03T18:52:51+00:00</td>
      <td>2021</td>
    </tr>
  </tbody>
</table>
</div>



Retrieve all the pay-rates for an award using an award identifier.


```python
fwc.get_payrates(id_or_code='MA000001').head(3)
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>classification_fixed_id</th>
      <th>base_pay_rate_id</th>
      <th>base_rate_type</th>
      <th>base_rate</th>
      <th>calculated_pay_rate_id</th>
      <th>calculated_rate_type</th>
      <th>calculated_rate</th>
      <th>parent_classification_name</th>
      <th>classification</th>
      <th>classification_level</th>
      <th>employee_rate_type_code</th>
      <th>operative_from</th>
      <th>operative_to</th>
      <th>version_number</th>
      <th>published_year</th>
      <th>last_modified_datetime</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>18</td>
      <td>None</td>
      <td>None</td>
      <td>NaN</td>
      <td>None</td>
      <td>None</td>
      <td>0.0</td>
      <td>Group B</td>
      <td>(Adult coal mining industry employee engaged i...</td>
      <td>NaN</td>
      <td>None</td>
      <td>2021-07-01T00:00:00+00:00</td>
      <td>None</td>
      <td>1</td>
      <td>2021</td>
      <td>2022-03-03T18:52:51+00:00</td>
    </tr>
    <tr>
      <th>1</th>
      <td>8</td>
      <td></td>
      <td>None</td>
      <td>NaN</td>
      <td>None</td>
      <td>None</td>
      <td>0.0</td>
      <td>Group A</td>
      <td>(Adult coal mining industry employees, without...</td>
      <td>NaN</td>
      <td>None</td>
      <td>2021-07-01T00:00:00+00:00</td>
      <td>None</td>
      <td>2</td>
      <td>2021</td>
      <td>2022-03-03T18:52:51+00:00</td>
    </tr>
    <tr>
      <th>2</th>
      <td>90835</td>
      <td>None</td>
      <td>None</td>
      <td>NaN</td>
      <td>None</td>
      <td>None</td>
      <td>0.0</td>
      <td>Adult apprentices</td>
      <td>Adult apprentices - % of the Mineworker - Indu...</td>
      <td>NaN</td>
      <td>None</td>
      <td>2021-07-01T00:00:00+00:00</td>
      <td>None</td>
      <td>1</td>
      <td>2021</td>
      <td>2022-01-13T16:41:36+00:00</td>
    </tr>
  </tbody>
</table>
</div>



Retrieve award classification information using an award identifier.


```python
fwc.get_classifications(id_or_code='MA000012').head(3)
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>classification_fixed_id</th>
      <th>clause_fixed_id</th>
      <th>clauses</th>
      <th>clause_description</th>
      <th>parent_classification_name</th>
      <th>classification</th>
      <th>classification_level</th>
      <th>next_down_classification_fixed_id</th>
      <th>next_up_classification_fixed_id</th>
      <th>operative_from</th>
      <th>operative_to</th>
      <th>version_number</th>
      <th>last_modified_datetime</th>
      <th>published_year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>549</td>
      <td>31</td>
      <td>16.1</td>
      <td>Pharmacy employees</td>
      <td>None</td>
      <td>Pharmacy assistant level 1</td>
      <td>1.0</td>
      <td>NaN</td>
      <td>553.0</td>
      <td>2021-07-01T00:00:00+00:00</td>
      <td>None</td>
      <td>1</td>
      <td>2022-03-03T18:52:51+00:00</td>
      <td>2021</td>
    </tr>
    <tr>
      <th>1</th>
      <td>553</td>
      <td>31</td>
      <td>16.1</td>
      <td>Pharmacy employees</td>
      <td>None</td>
      <td>Pharmacy student—1st year of course</td>
      <td>1.0</td>
      <td>549.0</td>
      <td>550.0</td>
      <td>2021-07-01T00:00:00+00:00</td>
      <td>None</td>
      <td>1</td>
      <td>2022-03-03T18:52:51+00:00</td>
      <td>2021</td>
    </tr>
    <tr>
      <th>2</th>
      <td>550</td>
      <td>31</td>
      <td>16.1</td>
      <td>Pharmacy employees</td>
      <td>None</td>
      <td>Pharmacy assistant level 2</td>
      <td>2.0</td>
      <td>553.0</td>
      <td>554.0</td>
      <td>2021-07-01T00:00:00+00:00</td>
      <td>None</td>
      <td>1</td>
      <td>2022-03-03T18:52:51+00:00</td>
      <td>2021</td>
    </tr>
  </tbody>
</table>
</div>



Retrieve the current pay-rate for a classification using a fixed identifier.


```python
fwc.get_current_payrate(id_or_code='MA000012',classification_fixed_id='549')
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>classification_fixed_id</th>
      <th>base_pay_rate_id</th>
      <th>base_rate_type</th>
      <th>base_rate</th>
      <th>calculated_pay_rate_id</th>
      <th>calculated_rate_type</th>
      <th>calculated_rate</th>
      <th>parent_classification_name</th>
      <th>classification</th>
      <th>classification_level</th>
      <th>employee_rate_type_code</th>
      <th>operative_from</th>
      <th>operative_to</th>
      <th>version_number</th>
      <th>published_year</th>
      <th>last_modified_datetime</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>549</td>
      <td>BR90099</td>
      <td>Weekly</td>
      <td>848.5</td>
      <td>CR25779</td>
      <td>Hourly</td>
      <td>22.33</td>
      <td>None</td>
      <td>Pharmacy assistant level 1</td>
      <td>1</td>
      <td>AD</td>
      <td>2021-07-01T00:00:00+00:00</td>
      <td>None</td>
      <td>1</td>
      <td>2021</td>
      <td>2022-03-03T18:52:51+00:00</td>
    </tr>
  </tbody>
</table>
</div>



Expense Allowances
-----

Retrieve a current individual expense-related allowance using a fixed identifier.


```python
fwc.get_expense_allowance(id_or_code='MA000012',expense_allowance_fixed_id='49')
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>expense_allowance_fixed_id</th>
      <th>clause_fixed_id</th>
      <th>clauses</th>
      <th>allowance_type_code</th>
      <th>parent_allowance</th>
      <th>allowance</th>
      <th>is_all_purpose</th>
      <th>allowance_amount</th>
      <th>payment_frequency</th>
      <th>last_adjusted_year</th>
      <th>cpi_quarter_last_adjusted</th>
      <th>operative_from</th>
      <th>operative_to</th>
      <th>version_number</th>
      <th>last_modified_datetime</th>
      <th>published_year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>49</td>
      <td>1864</td>
      <td>19.3(b)(i)</td>
      <td>None</td>
      <td>None</td>
      <td>Meal allowance—overtime which exceeds 1.5 hour...</td>
      <td>False</td>
      <td>19.69</td>
      <td>per occasion</td>
      <td>2020</td>
      <td>March Quarter</td>
      <td>2021-07-01T00:00:00+00:00</td>
      <td>None</td>
      <td>1</td>
      <td>2022-02-15T15:41:38+00:00</td>
      <td>2021</td>
    </tr>
  </tbody>
</table>
</div>



Retrieve award expense-related allowance information using an award identifier.


```python
fwc.get_expense_allowances(id_or_code='MA000012').head(3)
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>expense_allowance_fixed_id</th>
      <th>clause_fixed_id</th>
      <th>clauses</th>
      <th>allowance_type_code</th>
      <th>parent_allowance</th>
      <th>allowance</th>
      <th>is_all_purpose</th>
      <th>allowance_amount</th>
      <th>payment_frequency</th>
      <th>last_adjusted_year</th>
      <th>cpi_quarter_last_adjusted</th>
      <th>operative_from</th>
      <th>operative_to</th>
      <th>version_number</th>
      <th>last_modified_datetime</th>
      <th>published_year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>49</td>
      <td>1864</td>
      <td>19.3(b)(i)</td>
      <td>None</td>
      <td>None</td>
      <td>Meal allowance—overtime which exceeds 1.5 hour...</td>
      <td>False</td>
      <td>19.69</td>
      <td>per occasion</td>
      <td>2020</td>
      <td>March Quarter</td>
      <td>2021-07-01T00:00:00+00:00</td>
      <td>None</td>
      <td>1</td>
      <td>2022-02-15T15:41:38+00:00</td>
      <td>2021</td>
    </tr>
    <tr>
      <th>1</th>
      <td>9660</td>
      <td>23173</td>
      <td>19.3(c)</td>
      <td>None</td>
      <td>None</td>
      <td>Meal allowance—overtime which exceeds 4 hours</td>
      <td>False</td>
      <td>17.64</td>
      <td>per occasion</td>
      <td>2020</td>
      <td>March Quarter</td>
      <td>2021-07-01T00:00:00+00:00</td>
      <td>None</td>
      <td>1</td>
      <td>2022-02-15T15:41:38+00:00</td>
      <td>2021</td>
    </tr>
    <tr>
      <th>2</th>
      <td>53</td>
      <td>1867</td>
      <td>19.7</td>
      <td>None</td>
      <td>None</td>
      <td>Motor vehicle allowance</td>
      <td>False</td>
      <td>0.80</td>
      <td>per km</td>
      <td>2020</td>
      <td>March Quarter</td>
      <td>2020-07-01T00:00:00+00:00</td>
      <td>None</td>
      <td>1</td>
      <td>2022-02-15T15:41:38+00:00</td>
      <td>2021</td>
    </tr>
  </tbody>
</table>
</div>



Penalties
-----

Retrieve all the penalties for an award using an award identifier.


```python
fwc.get_penalties(id_or_code='MA000012').head(3)
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>penalty_fixed_id</th>
      <th>clause_fixed_id</th>
      <th>clause_description</th>
      <th>classification_level</th>
      <th>penalty_code</th>
      <th>penalty_description</th>
      <th>rate</th>
      <th>employee_rate_type_code</th>
      <th>penalty_calculated_value</th>
      <th>calculated_includes_all_purpose</th>
      <th>base_pay_rate_id</th>
      <th>operative_from</th>
      <th>operative_to</th>
      <th>version_number</th>
      <th>published_year</th>
      <th>last_modified_datetime</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2132</td>
      <td>21735</td>
      <td>Full-time and part-time adult employees—penalt...</td>
      <td>1</td>
      <td>None</td>
      <td>Saturday - Between 6.00 pm and 9.00 pm</td>
      <td>150.0</td>
      <td>AD</td>
      <td>33.50</td>
      <td>False</td>
      <td>BR90099</td>
      <td>2021-07-01T00:00:00+00:00</td>
      <td>None</td>
      <td>1</td>
      <td>2021</td>
      <td>2022-01-21T13:24:14+00:00</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2132</td>
      <td>21735</td>
      <td>Full-time and part-time adult employees—penalt...</td>
      <td>1</td>
      <td>None</td>
      <td>Saturday - Between 6.00 pm and 9.00 pm</td>
      <td>150.0</td>
      <td>AD</td>
      <td>33.50</td>
      <td>False</td>
      <td>BR90103</td>
      <td>2021-07-01T00:00:00+00:00</td>
      <td>None</td>
      <td>1</td>
      <td>2021</td>
      <td>2022-01-21T13:24:14+00:00</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2133</td>
      <td>21735</td>
      <td>Full-time and part-time adult employees—penalt...</td>
      <td>1</td>
      <td>None</td>
      <td>Saturday - Between 9.00 pm and midnight</td>
      <td>175.0</td>
      <td>AD</td>
      <td>39.08</td>
      <td>False</td>
      <td>BR90099</td>
      <td>2021-07-01T00:00:00+00:00</td>
      <td>None</td>
      <td>1</td>
      <td>2021</td>
      <td>2022-01-21T13:24:14+00:00</td>
    </tr>
  </tbody>
</table>
</div>



Wage Allowances
-----

Retrieve a current individual wage-related allowance using a fixed identifier.


```python
fwc.get_wage_allowance(id_or_code='MA000012',wage_allowance_fixed_id='191')
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>wage_allowance_fixed_id</th>
      <th>clause_fixed_id</th>
      <th>clauses</th>
      <th>allowance_type_code</th>
      <th>parent_allowance</th>
      <th>allowance</th>
      <th>is_all_purpose</th>
      <th>rate</th>
      <th>rate_unit</th>
      <th>base_pay_rate_id</th>
      <th>allowance_amount</th>
      <th>payment_frequency</th>
      <th>operative_from</th>
      <th>operative_to</th>
      <th>version_number</th>
      <th>last_modified_datetime</th>
      <th>published_year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>191</td>
      <td>788</td>
      <td>19.9</td>
      <td>None</td>
      <td>None</td>
      <td>Broken Hill allowance</td>
      <td>False</td>
      <td>4.28</td>
      <td>Percent</td>
      <td>BR90101</td>
      <td>38.5</td>
      <td>per week</td>
      <td>2021-07-01T00:00:00+00:00</td>
      <td>None</td>
      <td>1</td>
      <td>2022-03-03T09:01:31+00:00</td>
      <td>2021</td>
    </tr>
  </tbody>
</table>
</div>



Retrieve award wage-related allowance information using an award identifier.


```python
fwc.get_wage_allowances(id_or_code='MA000012').head(3)
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>wage_allowance_fixed_id</th>
      <th>clause_fixed_id</th>
      <th>clauses</th>
      <th>allowance_type_code</th>
      <th>parent_allowance</th>
      <th>allowance</th>
      <th>is_all_purpose</th>
      <th>rate</th>
      <th>rate_unit</th>
      <th>base_pay_rate_id</th>
      <th>allowance_amount</th>
      <th>payment_frequency</th>
      <th>operative_from</th>
      <th>operative_to</th>
      <th>version_number</th>
      <th>last_modified_datetime</th>
      <th>published_year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>191</td>
      <td>788</td>
      <td>19.9</td>
      <td>None</td>
      <td>None</td>
      <td>Broken Hill allowance</td>
      <td>False</td>
      <td>4.28</td>
      <td>Percent</td>
      <td>BR90101</td>
      <td>38.50</td>
      <td>per week</td>
      <td>2021-07-01T00:00:00+00:00</td>
      <td>None</td>
      <td>1.0</td>
      <td>2022-03-03T09:01:31+00:00</td>
      <td>2021</td>
    </tr>
    <tr>
      <th>1</th>
      <td>12011</td>
      <td>23000</td>
      <td>19.2</td>
      <td>None</td>
      <td>None</td>
      <td>Home medicine reviews or residential medicatio...</td>
      <td>False</td>
      <td>0.00</td>
      <td>Percent</td>
      <td>BR90109</td>
      <td>106.40</td>
      <td>per week</td>
      <td>2021-07-01T00:00:00+00:00</td>
      <td>None</td>
      <td>1.0</td>
      <td>2022-03-03T09:01:31+00:00</td>
      <td>2021</td>
    </tr>
    <tr>
      <th>2</th>
      <td>191</td>
      <td>788</td>
      <td>19.9</td>
      <td>None</td>
      <td>None</td>
      <td>Broken Hill allowance</td>
      <td>False</td>
      <td>4.28</td>
      <td>Percent</td>
      <td>None</td>
      <td>37.56</td>
      <td>per week</td>
      <td>2020-07-01T00:00:00+00:00</td>
      <td>2021-06-30T00:00:00+00:00</td>
      <td>NaN</td>
      <td>2022-03-03T09:01:31+00:00</td>
      <td>2020</td>
    </tr>
  </tbody>
</table>
</div>



Contribution
-----
Contributors and committers are are welcome.
