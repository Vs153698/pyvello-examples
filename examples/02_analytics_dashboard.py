import pyvello as ui

def nav_clicked(page_name: str):
    print(f"Navigating to {page_name}")

with ui.App(title="Enterprise SaaS Dashboard", theme="light", palette="red") as app:
    # 1. Dedicated Website Navigation Sidebar
    with ui.sidebar():
        # Brand & Workspace Header
        ui.title("Acme Analytics", variant="h3")
        ui.badge("Enterprise v2.4", variant="default")
        ui.separator()
        
        # Navigation Menu Links
        ui.text("Main Menu", class_name="text-xs font-mono text-muted-foreground uppercase tracking-wider")
        ui.button("Dashboard", variant="secondary", class_name="w-full justify-start")
        ui.button("Revenue & Growth", variant="ghost", class_name="w-full justify-start")
        ui.button("Customer Accounts", variant="ghost", class_name="w-full justify-start")
        ui.button("Integrations & API", variant="ghost", class_name="w-full justify-start")
        ui.button("Settings", variant="ghost", class_name="w-full justify-start")
        
        ui.separator()
        # Interactive Filter Controls
        ui.text("Data Dimensions", class_name="text-xs font-mono text-muted-foreground uppercase tracking-wider")
        timeframe = ui.select(
            label="Reporting Period",
            options=["Last 30 Days", "Quarter to Date", "Year to Date"],
            value="Last 30 Days"
        )
        region = ui.select(
            label="Geographic Region",
            options=["Global", "North America", "Europe", "Asia-Pacific"],
            value="Global"
        )
        
        ui.separator()
        # User Profile Footer
        ui.avatar(fallback="AR")
        ui.text("Alex Rivera (Admin)", class_name="text-xs font-medium")

    # 2. Main Page Viewport
    ui.title("Executive Revenue & Performance", variant="h2")
    ui.text("Real-time revenue velocity, enterprise cohort retention, and customer acquisition channels.")

    # 3. Executive KPI Metric Cards (3 Columns)
    col1, col2, col3 = ui.columns(3)
    with col1:
        ui.metric(label="Annual Recurring Revenue", value="$14.82M", delta="+18.4%")
    with col2:
        ui.metric(label="Active Enterprise Accounts", value="3,240", delta="+12.6%")
    with col3:
        ui.metric(label="Net Revenue Retention (NRR)", value="118.2%", delta="+3.1%")

    # 4. Analytics Visualizations (2 Columns: Velocity & Acquisition)
    chart1, chart2 = ui.columns(2)
    with chart1:
        ui.line_chart(
            data=[
                {"month": "Jan", "revenue": 920},
                {"month": "Feb", "revenue": 1040},
                {"month": "Mar", "revenue": 1180},
                {"month": "Apr", "revenue": 1290},
                {"month": "May", "revenue": 1420},
                {"month": "Jun", "revenue": 1580},
            ],
            x="month",
            y="revenue",
            title="Monthly Revenue Velocity ($k)",
        )
    with chart2:
        ui.bar_chart(
            data=[
                {"channel": "Direct Inbound", "conversions": 4200},
                {"channel": "Product-Led", "conversions": 3850},
                {"channel": "Partner Referrals", "conversions": 2640},
                {"channel": "Outbound Enterprise", "conversions": 1920},
            ],
            x="channel",
            y="conversions",
            title="Customer Acquisition by Channel",
        )

    # 5. Production Health Callout
    ui.callout("All telemetry pipelines and streaming CDC connectors are operating normally (P95 latency: 38ms).", variant="success")

if __name__ == "__main__":
    app.launch(port=8080)