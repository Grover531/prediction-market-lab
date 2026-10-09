# Prediction Market Notes

## What is a market?

A market is a contract that allows participants to buy or sell outcomes of a future event.

## What is an event?

An event is the real world occurrence that determines whether a market resolves to YES or NO.

## What does a YES contract price mean?

The YES price represents the market's current implied probablity of the event occurring.

## What does a NO contract price mean?

The NO contract price is the amount you pay to bet that an event will not happen. The NO price represents the market's current implied probability of the event not occurring.

# Project Structure Notes

## data/

Stores market data collected from APIs.
Examples: 
- JSON files
- CSV files
- SQLite files

## src/

Contains the application code.
Examples: 
- Data collectors
- Database access code
- Future trading models

## tests/

Contains automated tests.
Examples:
- API validation tests
- Database tests
- Data quality checks

## docs/

Contains notes and research.
Examples:
- Prediction market concepts
- Architecture diagrams
- Development notes

# Collector v1 Requirements

The collector should: 

- Connect to a prediction market API
- Retrieve market data
- Print market information
- Handle errors gracefully

