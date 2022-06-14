import React, { useState, useEffect } from 'react';
import './App.css';
import { csv } from 'd3';
import datasj from './covid-saojose.csv';
import { Line } from 'react-chartjs-2';

function App() {
  
  const [data, setData] = useState({});
  const [loading, setLoading] = useState(true);

  useEffect(()=> {
    const fetchData = async () => {
      setData(await (await csv(datasj)).reverse());
      setLoading(false);
    }

    fetchData();
  },[]);

  if(loading)
    return 'loading...';

  return (
    <div className="App">
      <h1>Dados Covid São José</h1>
      <Line
          data={{
              labels: data.map(({ date }) => date),
              datasets: [{
                  data: data.map(({ confirmed }) => confirmed),
                  label: 'Infected',
                  borderColor: '#3333ff',
                  fill: true,
              }],
          }}
      />
    </div>
  );
}

export default App;