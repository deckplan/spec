---
title: About Substrait
---
# Substrait: Cross-Language Serialization for Relational Algebra



## Project Vision

The Substrait project aims to create a well-defined, cross-language [specification](/spec/specification) for data compute operations. The specification declares a set of common operations, defines their semantics, and describes their behavior unambiguously. The project also defines extension points and serialized representations of the specification.

In many ways, the goal of this project is similar to that of the Apache Arrow project. Arrow is focused on a standardized memory representation of columnar data. Substrait is focused on what should be done to data.

See the [introductory tutorial](/tutorial/sql_to_substrait/) for a hands on introduction to Substrait

## Why not use SQL?

SQL is a well known language for describing queries against relational data.  It is designed to be simple and allow reading
and writing by humans.  Substrait is not intended as a replacement for SQL and works alongside SQL to provide capabilities that
SQL lacks.  SQL is not a great fit for systems that actually satisfy the query because it does not provide sufficient detail and
is not represented in a format that is easy for processing.  Because of this, most modern systems will first translate the SQL query
into a query plan, sometimes called the execution plan.  There can be multiple levels of a query plan (e.g. physical and logical),
a query plan may be split up and distributed across multiple systems, and a query plan often undergoes simplifying or optimizing
transformations. The SQL standard does not define the format of the query or execution plan and there is no open format that is
supported by a broad set of systems.  Substrait was created to provide a standard and open format for these query plans.



## Why not just do this within an existing OSS project?

A key goal of the Substrait project is to not be coupled to any single existing technology. Trying to get people involved in something can be difficult when it seems to be primarily driven by the opinions and habits of a single community. In many ways, this situation is similar to the early situation with Arrow. The precursor to Arrow was the Apache Drill ValueVectors concepts. As part of creating Arrow, [Wes](https://www.linkedin.com/in/wesmckinn/) and [Jacques](https://www.linkedin.com/in/jacquesnadeau/) recognized the need to create a new community to build a fresh consensus (beyond just what the Apache Drill community wanted). This separation and new independent community was a key ingredient to Arrow's current success. The needs here are much the same: many separate communities could benefit from Substrait, but each have their own pain points, type systems, development processes and timelines. To help resolve these tensions, one of the approaches proposed in Substrait is to set a bar that at least two of the top four OSS data technologies (Arrow, Spark, Iceberg, Trino) supports something before incorporating it directly into the Substrait specification. (Another goal is to support strong extension points at key locations to avoid this bar being a limiter to broad adoption.)



## Related Technologies

* [Apache Calcite](https://calcite.apache.org/): Many ideas in Substrait are inspired by the Calcite project. Calcite is a great JVM-based SQL query parsing and optimization framework. A key goal of the Substrait project is to expose Calcite capabilities more easily to non-JVM technologies as well as expose query planning operations as microservices.
* [Apache Arrow](https://arrow.apache.org/): The Arrow format for data is what the Substrait specification attempts to be for compute expressions. A key goal of Substrait is to enable Substrait producers to execute work within the Arrow Rust and C++ compute kernels.



## Why the name Substrait?

A strait is a narrow connector of water between two other pieces of water. In analytics, data is often thought of as water. Substrait is focused on instructions related to the data. In other words, what defines or supports the movement of water between one or more larger systems. Thus, the underlayment for the strait connecting different pools of water => sub-strait.
