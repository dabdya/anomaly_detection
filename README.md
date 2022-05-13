# Обнаружение аномалий в технологических системах

## Команда проекта

Имя, фамилия  | Группа | Логин
--- | --- | --- |
Пищулов Сергей | ФТ-301 | <a href=https://github.com/SergeyPishchulov>SergeyPishchulov</a>
Коновалов Артем | ФТ-301 | <a href=https://github.com/dabdya>dabdya</a>

## Лидерборд

<table>
	<thead>
		<tr>
			<th rowspan="0"></th>
			<th colspan="3">IsolationForest</th>
			<th colspan="3">MSET</th>
			<th colspan="3">LSTM-AE</th>
			<th colspan="3">LSTM-AD</th>
			<th colspan="3">LSTM-VAE</th>
		</tr>
		<tr>
			<th>F1</th><th>FAR</th><th>MAR</th>
			<th>F1</th><th>FAR</th><th>MAR</th>
			<th>F1</th><th>FAR</th><th>MAR</th>
			<th>F1</th><th>FAR</th><th>MAR</th>
			<th>F1</th><th>FAR</th><th>MAR</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<th>ALL</th>
			<td>0.62</td><td>0.13</td><td>0.44</td>
			<td>0.74</td><td>0.19</td><td>0.21</td>
			<th>0.89</th><td>0.09</td><td>0.06</td>
			<td>0.88</td><td>0.07</td><td>0.12</td>
			<td>0.88</td><td>0.09</td><td>0.08</td>
		</tr>
		<tr>
			<th>valve1</th>
			<td>0.53</td><td>0.09</td><td>0.57</td>
			<td>0.72</td><td>0.20</td><td>0.23</td>
			<th>0.92</th><td>0.08</td><td>0.03</td>
			<td>0.91</td><td>0.05</td><td>0.09</td>
			<td>0.91</td><td>0.08</td><td>0.04</td>
		</tr>
		<tr>
			<th>valve2</th>
			<td>0.62</td><td>0.12</td><td>0.45</td>
			<td>0.76</td><td>0.17</td><td>0.19</td>
			<td>0.89</td><td>0.07</td><td>0.09</td>
			<th>0.92</th><td>0.05</td><td>0.07</td>
			<td>0.90</td><td>0.07</td><td>0.07</td>
		</tr>
		<tr>
			<th>other0</th>
			<td>0.80</td><td>0.05</td><td>0.23</td>
			<td>0.75</td><td>0.17</td><td>0.23</td>
			<td>0.29</td><td>0.09</td><td>0.79</td>
			<th>0.93</th><td>0.10</td><td>0.0</td>
			<td>0.93</td><td>0.10</td><td>0.0</td>
		</tr>
		<tr>
			<th>other1</th>
			<td>0.80</td><td>0.23</td><td>0.13</td>
			<td>0.93</td><td>0.08</td><td>0.0</td>
			<th>0.94</th><td>0.10</td><td>0.0</td>
			<td>0.90</td><td>0.12</td><td>0.0</td>
			<td>0.91</td><td>0.11</td><td>0.0</td>
		</tr>
		<tr>
			<th>other2</th>
			<td>0.78</td><td>0.16</td><td>0.18</td>
			<td>0.79</td><td>0.16</td><td>0.16</td>
			<th>0.93</th><td>0.10</td><td>0.0</td>
			<td>0.91</td><td>0.11</td><td>0.0</td>
			<td>0.91</td><td>0.11</td><td>0.0</td>
		</tr>
		<tr>
			<th>other3</th>
			<td>0.71</td><td>0.20</td><td>0.18</td>
			<td>0.70</td><td>0.22</td><td>0.18</td>
			<td>0.89</td><td>0.10</td><td>0.0</td>
			<td>0.88</td><td>0.12</td><td>0.0</td>
			<th>0.95</th><td>0.03</td><td>0.04</td>
		</tr>
		<tr>
			<th>other4</th>
			<td>0.08</td><td>0.05</td><td>0.95</td>
			<td>0.55</td><td>0.30</td><td>0.34</td>
			<td>0.68</td><td>0.05</td><td>0.42</td>
			<th>0.73</th><td>0.01</td><td>0.41</td>
			<td>0.13</td><td>0.05</td><td>0.92</td>
		</tr>
		<tr>
			<th>other5</th>
			<td>0.88</td><td>0.09</td><td>0.07</td>
			<td>0.80</td><td>0.16</td><td>0.15</td>
			<td>0.76</td><td>0.0</td><td>0.38</td>
			<td>0.91</td><td>0.04</td><td>0.11</td>
			<th>0.92</th><td>0.10</td><td>0.0</td>
		</tr>
		<tr>
			<th>other6</th>
			<td>0.71</td><td>0.69</td><td>0.05</td>
			<td>0.77</td><td>0.20</td><td>0.0</td>
			<th>0.79</th><td>0.51</td><td>0.0</td>
			<td>0.27</td><td>0.12</td><td>0.79</td>
			<td>0.31</td><td>0.06</td><td>0.79</td>
		</tr>
		<tr>
			<th>other7</th>
			<td>0.48</td><td>0.10</td><td>0.62</td>
			<td>0.89</td><td>0.12</td><td>0.0</td>
			<th>0.92</th><td>0.10</td><td>0.0</td>
			<td>0.86</td><td>0.08</td><td>0.12</td>
			<td>0.90</td><td>0.11</td><td>0.0</td>
		</tr>
		<tr>
			<th>other8</th>
			<td>0.57</td><td>0.05</td><td>0.56</td>
			<td>0.77</td><td>0.14</td><td>0.27</td>
			<td>0.72</td><td>0.06</td><td>0.37</td>
			<th>0.98</th><td>0.04</td><td>0.0</td>
			<th>0.94</th><td>0.10</td><td>0.0</td>
		</tr>
		<tr>
			<th>other9</th>
			<td>0.52</td><td>0.23</td><td>0.50</td>
			<th>0.91</th><td>0.10</td><td>0.0</td>
			<td>0.91</td><td>0.11</td><td>0.0</td>
			<td>0.70</td><td>0.07</td><td>0.38</td>
			<td>0.67</td><td>0.11</td><td>0.38</td>
		</tr>
		<tr>
			<th>other10</th>
			<td>0.82</td><td>0.19</td><td>0.06</td>
			<td>0.44</td><td>0.36</td><td>0.51</td>
			<th>0.91</th><td>0.11</td><td>0.0</td>
			<td>0.74</td><td>0.0</td><td>0.42</td>
			<td>0.73</td><td>0.04</td><td>0.37</td>
		</tr>
		<tr>
			<th>other11</th>
			<td>0.82</td><td>0.19</td><td>0.03</td>
			<th>0.93</th><td>0.08</td><td>0.0</td>
			<td>0.90</td><td>0.11</td><td>0.0</td>
			<td>0.91</td><td>0.11</td><td>0.0</td>
			<td>0.91</td><td>0.11</td><td>0.0</td>
		</tr>
		<tr>
			<th>other12</th>
			<td>0.53</td><td>0.24</td><td>0.48</td>
			<td>0.67</td><td>0.23</td><td>0.29</td>
			<td>0.90</td><td>0.12</td><td>0.0</td>
			<td>0.49</td><td>0.09</td><td>0.62</td>
			<th>0.91</th><td>0.11</td><td>0.0</td>
		</tr>
		<tr>
			<th>other13</th>
			<td>0.81</td><td>0.24</td><td>0.01</td>
			<td>0.62</td><td>0.24</td><td>0.44</td>
			<th>0.91</th><td>0.10</td><td>0.0</td>
			<td>0.79</td><td>0.52</td><td>0.0</td>
			<td>0.79</td><td>0.51</td><td>0.0</td>
		</tr>
	</tbody>
</table>
