# Обнаружение аномалий в технологичеких системах

<table>
	<thead>
    <tr>
      <th>Метод</th>
      <th>Метрика</th>
      <th>all</th><th>valve1</th>
      <th>valve2</th>
      <th>other0</th>
      <th>other1</th>
      <th>other2</th>
      <th>other3</th>
      <th>other4</th>
      <th>other5</th>
      <th>other6</th>
      <th>other7</th>
      <th>other8</th>
      <th>other9</th>
      <th>other10</th>
      <th>other11</th>
      <th>other12</th>
      <th>other13</th>
    </tr>
	</thead>
    <tbody>
      <tr>
        <td rowspan="3">MSET</td>
        <td>F1</td>
        <td><b>0.74</b></td><td>0.72</td><td>0.76</td>
        <td>0.75</td><td>0.93</td><td>0.79</td>
        <td>0.7</td><td>0.55</td><td>0.8</td>
        <td>0.77</td><td>0.89</td><td>0.77</td>
        <td>0.91</td><td>0.44</td><td>0.93</td>
        <td>0.67</td><td>0.62</td>
      </tr>
      <tr>
        <td>FAR</td>
        <td><b>0.19</b></td><td>0.2</td><td>0.17</td>
        <td>0.17</td><td>0.08</td><td>0.16</td>
        <td>0.22</td><td>0.3</td><td>0.16</td>
        <td>0.2</td><td>0.12</td><td>0.14</td>
        <td>0.1</td><td>0.36</td><td>0.08</td>
        <td>0.23</td><td>0.24</td>
      </tr>
      <tr>
        <td>MAR</td>
        <td><b>0.21</b></td><td>0.23</td><td>0.19</td>
        <td>0.23</td><td>0.0</td><td>0.16</td>
        <td>0.18</td><td>0.34</td><td>0.15</td>
        <td>0.0</td><td>0.0</td><td>0.27</td>
        <td>0.0</td><td>0.51</td><td>0.0</td>
        <td>0.29</td><td>0.44</td>
      </tr>
      <! ########################## ––>
      <tr>
        <td rowspan="3">IForest</td>
        <td>F1</td>
        <td><b>0.62</b></td><td>0.53</td><td>0.62</td>
        <td>0.78</td><td>0.81</td><td>0.52</td>
        <td>0.71</td><td>0.08</td><td>0.48</td>
        <td>0.8</td><td>0.82</td><td>0.8</td>
        <td>0.88</td><td>0.57</td><td>0.82</td>
        <td>0.53</td><td>0.71</td>
      </tr>
      <tr>
        <td>FAR</td>
        <td><b>0.13</b></td><td>0.09</td><td>0.16</td>
        <td>0.12</td><td>0.24</td><td>0.23</td>
        <td>0.2</td><td>0.05</td><td>0.1</td>
        <td>0.05</td><td>0.19</td><td>0.23</td>
        <td>0.09</td><td>0.05</td><td>0.19</td>
        <td>0.24</td><td>0.69</td>
      </tr>
      <tr>
        <td>MAR</td>
        <td><b>0.44</b></td><td>0.57</td><td>0.45</td>
        <td>0.18</td><td>0.01</td><td>0.5</td>
        <td>0.18</td><td>0.95</td><td>0.62</td>
        <td>0.23</td><td>0.03</td><td>0.13</td>
        <td>0.07</td><td>0.56</td><td>0.06</td>
        <td>0.48</td><td>0.05</td>
      </tr>
      <! ########################## ––>
      <tr>
        <td rowspan="3">LSTM-AE</td>
        <td>F1</td>
        <td><b>0.87</b></td><td>0.89</td><td>0.89</td>
        <td>0.92</td><td>0.91</td><td>0.91</td>
        <td>0.9</td><td>0.69</td><td>0.91</td>
        <td>0.29</td><td>0.9</td><td>0.94</td>
        <td>0.67</td><td>0.72</td><td>0.91</td>
        <td>0.9</td><td>0.79</td>
      </tr>
      <tr>
        <td>FAR</td>
        <td><b>0.09</b></td><td>0.07</td><td>0.06</td>
        <td>0.1</td><td>0.11</td><td>0.11</td>
        <td>0.09</td><td>0.05</td><td>0.1</td>
        <td>0.08</td><td>0.11</td><td>0.1</td>
        <td>0.11</td><td>0.06</td><td>0.11</td>
        <td>0.12</td><td>0.52</td>
      </tr>
      <tr>
        <td>MAR</td>
        <td><b>0.1</b></td><td>0.09</td><td>0.11</td>
        <td>0.0</td><td>0.0</td><td>0.0</td>
        <td>0.0</td><td>0.41</td><td>0.0</td>
        <td>0.79</td><td>0.0</td><td>0.0</td>
        <td>0.38</td><td>0.37</td><td>0.0</td>
        <td>0.0</td><td>0.0</td>
      </tr>
      <! ########################## ––>
      <tr>
        <td rowspan="3">LSTM-AD</td>
        <td>F1</td>
        <td><b>0.88</b></td><td>0.91</td><td>0.92</td>
        <td>0.93</td><td>0.9</td><td>0.91</td>
        <td>0.88</td><td>0.73</td><td>0.91</td>
        <td>0.27</td><td>0.86</td><td>0.98</td>
        <td>0.7</td><td>0.74</td><td>0.91</td>
        <td>0.49</td><td>0.79</td>
      </tr>
      <tr>
        <td>FAR</td>
        <td><b>0.07</b></td><td>0.05</td><td>0.05</td>
        <td>0.1</td><td>0.12</td><td>0.11</td>
        <td>0.12</td><td>0.01</td><td>0.04</td>
        <td>0.12</td><td>0.08</td><td>0.04</td>
        <td>0.07</td><td>0.0</td><td>0.11</td>
        <td>0.09</td><td>0.52</td>
      </tr>
      <tr>
        <td>MAR</td>
        <td><b>0.12</b></td><td>0.09</td><td>0.07</td>
        <td>0.0</td><td>0.0</td><td>0.0</td>
        <td>0.0</td><td>0.41</td><td>0.11</td>
        <td>0.79</td><td>0.12</td><td>0.0</td>
        <td>0.38</td><td>0.42</td><td>0.0</td>
        <td>0.62</td><td>0.0</td>
      </tr>
  </tbody>
</table>

## Команда проекта

Имя, фамилия  | Группа | Логин
--- | --- | --- |
Пищулов Сергей | ФТ-301 | <a href=https://github.com/SergeyPishchulov>SergeyPishchulov</a>
Коновалов Артем | ФТ-301 | <a href=https://github.com/dabdya>dabdya</a>

