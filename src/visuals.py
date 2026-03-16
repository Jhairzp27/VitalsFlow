import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

class Visualizer:
    """Capa de Visualización (View). Renderiza gráficos interactivos."""

    _COLORS_TEST_RESULTS = ["#FF5A5F", "#00A699", "#FFAA00"]

    def __init__(self, theme: str = "plotly_dark", bg_color: str = "rgba(0,0,0,0)"):
        self.theme = theme
        self.bg_color = bg_color

    def _apply_base_layout(self, fig: go.Figure) -> go.Figure:
        """Aplica el tema oscuro/claro de forma uniforme."""
        fig.update_layout(template=self.theme, paper_bgcolor=self.bg_color, plot_bgcolor=self.bg_color)
        return fig

    def plot_q1_trends(self, df: pd.DataFrame, window: int = 3) -> go.Figure:
        df_q1 = df.groupby('Mes_Anio').size().reset_index(name='Admisiones')
        
        df_q1['Media_Movil'] = df_q1['Admisiones'].rolling(window=window).mean()
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x=df_q1['Mes_Anio'], y=df_q1['Admisiones'], mode='lines+markers', 
            name='Volumen Real',
            line=dict(color='#00D26A', width=2, shape='spline')
        ))
        
        fig.add_trace(go.Scatter(
            x=df_q1['Mes_Anio'], y=df_q1['Media_Movil'], mode='lines',
            name=f'Tendencia ({window} Meses)',
            line=dict(color='gray', width=2, dash='dash', shape='spline')
        ))
        
        fig.update_layout(
            hovermode="x unified", 
            xaxis_title="Mes de Admisión", 
            yaxis_title="Cantidad de Pacientes",
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )
        return self._apply_base_layout(fig)

    def plot_q2_top_hospitals(self, df: pd.DataFrame) -> go.Figure:
        df_q2 = (
            df.groupby('Hospital')['Billing Amount']
            .sum()
            .reset_index()
            .sort_values('Billing Amount', ascending=False)
            .head(10)
        )
        fig = px.bar(
            df_q2,
            x='Billing Amount',
            y='Hospital',
            orientation='h',
            text=df_q2['Billing Amount'].apply(lambda x: f"${x / 1_000_000:.1f}M"),
            color='Billing Amount',
            color_continuous_scale='Blues',
        )
        fig.update_traces(textposition='inside')
        fig.update_layout(
            yaxis={'categoryorder': 'total ascending'},
            xaxis_title="Ingresos Totales ($)",
            yaxis_title="",
            coloraxis_showscale=False,
        )
        return self._apply_base_layout(fig)

    def plot_q3_avg_stay(self, df: pd.DataFrame, group_col: str) -> go.Figure:
        df_q3 = df.groupby(group_col)['Days Hospitalized'].mean().reset_index()
        fig = px.bar(
            df_q3,
            x=group_col,
            y='Days Hospitalized',
            text=df_q3['Days Hospitalized'].round(1),
            color=group_col,
            color_discrete_sequence=px.colors.qualitative.Pastel,
        )
        fig.update_traces(textposition='auto')
        nombre_eje = "Tipo de Admisión" if group_col == 'Admission Type' else "Condición Médica"
        fig.update_layout(showlegend=False, yaxis_title="Días Promedio", xaxis_title=nombre_eje)
        return self._apply_base_layout(fig)

    def plot_q4_test_results(self, df: pd.DataFrame) -> go.Figure:
        df_q4 = df['Test Results'].value_counts().reset_index()
        df_q4.columns = ['Resultado', 'Cantidad']
        pull_values = [0.1 if res == 'Abnormal' else 0 for res in df_q4['Resultado']]
        fig = go.Figure(data=[
            go.Pie(
                labels=df_q4['Resultado'],
                values=df_q4['Cantidad'],
                pull=pull_values,
                hole=0.4,
                marker_colors=self._COLORS_TEST_RESULTS,
            )
        ])
        return self._apply_base_layout(fig)

    def plot_q5_cost_distribution(self, df: pd.DataFrame) -> go.Figure:
        median_order = (
            df.groupby('Medical Condition')['Billing Amount']
            .median()
            .sort_values(ascending=False)
            .index
        )
        fig = px.box(
            df,
            x='Medical Condition',
            y='Billing Amount',
            color='Medical Condition',
            category_orders={'Medical Condition': median_order},
        )
        fig.update_layout(showlegend=False, xaxis_title="Condición Médica", yaxis_title="Facturación ($)")
        return self._apply_base_layout(fig)