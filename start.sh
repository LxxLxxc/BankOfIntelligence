#!/bin/bash
# start.sh – تشغيل مشروع BankOfIntelligence تلقائيًا

echo "🔁 جاري تشغيل BankOfIntelligence..."
export FLASK_APP=src/backend/server.py
flask run
