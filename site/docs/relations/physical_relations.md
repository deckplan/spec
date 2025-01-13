# Physical Relations

There is no true distinction between logical and physical operations in Substrait. By convention, certain operations are classified as physical, but all operations can be potentially used in any kind of plan. A particular set of transformations or target operators may (by convention) be considered the "physical plan" but this is a characteristic of the system consuming substrait as opposed to a definition within Substrait.



## Hash Equijoin Operator

The hash equijoin join operator will build a hash table out of the right input based on a set of join keys. It will then probe that hash table for incoming inputs, finding matches. 

| Signature            | Value                                                        |
| -------------------- | ------------------------------------------------------------ |
| Inputs               | 2                                                            |
| Outputs              | 1                                                            |
| Property Maintenance | Distribution is maintained. Orderedness of the left set is maintained in INNER join cases, otherwise it is eliminated. |
| Direct Output Order  | Same as the [Join](logical_relations.md#join-operator) operator. |

### Hash Equijoin Properties

| Property            | Description                                                                                                                                                                                                            | Required                 |
|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------|
| Left Input          | A relational input.(Probe-side)                                                                                                                                                                                        | Required                 |
| Right Input         | A relational input.(Build-side)                                                                                                                                                                                        | Required                 |
| Left Keys           | References to the fields to join on in the left input.                                                                                                                                                                 | Required                 |
| Right Keys          | References to the fields to join on in the right input.                                                                                                                                                                | Required                 |
| Post Join Predicate | An additional expression that can be used to reduce the output of the join operation post the equality condition. Minimizes the overhead of secondary join conditions that cannot be evaluated using the equijoin keys. | Optional, defaults true. |
| Join Type           | One of the join types defined in the Join operator.                                                                                                                                                                    | Required                 |


## NLJ (Nested Loop Join) Operator

The nested loop join operator does a join by holding the entire right input and then iterating over it using the left input, evaluating the join expression on the Cartesian product of all rows, only outputting rows where the expression is true. Will also include non-matching rows in the OUTER, LEFT and RIGHT operations per the join type requirements.

| Signature            | Value                                                        |
| -------------------- | ------------------------------------------------------------ |
| Inputs               | 2                                                            |
| Outputs              | 1                                                            |
| Property Maintenance | Distribution is maintained. Orderedness is eliminated.       |
| Direct Output Order  | Same as the [Join](logical_relations.md#join-operator) operator. |

### NLJ Properties

| Property        | Description                                                  | Required                                       |
| --------------- | ------------------------------------------------------------ | ---------------------------------------------- |
| Left Input      | A relational input.                                          | Required                                       |
| Right Input     | A relational input.                                          | Required                                       |
| Join Expression | A boolean condition that describes whether each record from the left set "match" the record from the right set. | Optional. Defaults to true (a Cartesian join). |
| Join Type       | One of the join types defined in the Join operator.          | Required                                       |

## Duplicate Eliminated Join Operator
The Duplicate Eliminated Join, along with the [Duplicate Eliminated Get Operator](physical_relations.md#duplicate-eliminated-get-operator) are the two necessary operators that enable general subquery unnesting. (See the [Unnesting Arbitrary Queries](https://cs.emis.de/LNI/Proceedings/Proceedings241/383.pdf) paper for more information.)

The Duplicate Eliminated Join is essentially a [Regular Join Operator](logical_relations.md#join-operator). It can have any regular join type, and its execution is the same.  The only restriction is that the join must be a hash equi-join. The main difference is that one of its children has, somewhere in its subtree, a dependency on the deduplicated result of the other. Therefore, this operator pushes the deduplicated result to its dependent child via the Duplicate Eliminated Get Operator. The side that will be deduplicated is specified in the Duplicate Eliminated Side property. The other side is the one that depends on the deduplication.

The Duplicate Eliminated Join has two outputs.  The first output is no different than a regular join output.  The second output is the output to the duplicate eliminated get operator.  This output contains only the columns listed in the `duplicate_eliminated_columns` property.  This output contains only the columns listed in the `duplicate_eliminated_columns` property, corresponding to the side depicted by the `duplicate_eliminated_side`. Note that either the build side or the probe side can be deduplicated and then pushed to the other.

| Signature            | Value                                                                                                             |
| -------------------- |-------------------------------------------------------------------------------------------------------------------|
| Inputs               | 2                                                                                                                 |
| Outputs              | 2 One output is from the deduplicated columns in the Duplicate Eliminated Get, and the second is the join output. |
| Property Maintenance | It is the same as the [Hash Equijoin Operator](physical_relations.md#hash-equijoin-operator)                      |
| Direct Output Order  | Same as the [Join](logical_relations.md#join-operator) operator.                                                  |

### Duplicate Eliminated Join Properties

| Property                  | Description                                                                                                                                                                                                             | Required                 |
|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------|
| Left Input                | A relational input.                                                                                                                                                                                                     | Required                 |
| Right Input               | A relational input.                                                                                                                                                                                                     | Required                 |
| Left Keys                 | References to the fields to join on in the left input.                                                                                                                                                                  | Required                 |
| Right Keys                | References to the fields to join on in the right input.                                                                                                                                                                 | Required                 |    
| Post Join Predicate       | An additional expression that can be used to reduce the output of the join operation post the equality condition. Minimizes the overhead of secondary join conditions that cannot be evaluated using the equijoin keys. | Optional, defaults true. |
| Join Type                 | One of the join types defined in the Join operator.                                                                                                                                                                     | Required                 |
| Duplicate Eliminated Side | The side that is deduplicated and pushed into the other side.                                                                                                                                                           | Required                 |
| Duplicate Eliminated Columns | The columns that should be included in the deduplicated output.  These columns must be key columns. | Required |

## Duplicate Eliminated Get Operator
An operator that takes as its input the result of the deduplicated side of the Duplicate Eliminated Join. It simply scans the input and outputs the deduplicated values.
| Signature            | Value                                                                               |
| -------------------- |-------------------------------------------------------------------------------------|
| Inputs               | 1                                                                                   |
| Outputs              | 1                                                                                   |
| Property Maintenance | Distribution is not maintained due to the deduplication. Orderedness is eliminated. |
| Direct Output Order  | It will only project the deduplicated columns from it's input                       |

### Duplicate Eliminated Get Properties

| Property   | Description                                        | Required                    |
|------------|----------------------------------------------------|-----------------------------|
| Input      | A relational input.                                | Required                    |

## Merge Equijoin Operator

The merge equijoin does a join by taking advantage of two sets that are sorted on the join keys. This allows the join operation to be done in a streaming fashion.

| Signature            | Value                                                        |
| -------------------- | ------------------------------------------------------------ |
| Inputs               | 2                                                            |
| Outputs              | 1                                                            |
| Property Maintenance | Distribution is maintained. Orderedness is eliminated.       |
| Direct Output Order  | Same as the [Join](logical_relations.md#join-operator) operator. |

### Merge Join Properties

| Property            | Description                                                                                                                                                                                                             | Required                    |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|
| Left Input          | A relational input.                                                                                                                                                                                                     | Required                    |
| Right Input         | A relational input.                                                                                                                                                                                                     | Required                    |
| Left Keys           | References to the fields to join on in the left input.                                                                                                                                                                  | Required                    |
| Right Keys          | References to the fields to join on in the right input.                                                                                                                                                            | Reauired                    |    
| Post Join Predicate | An additional expression that can be used to reduce the output of the join operation post the equality condition. Minimizes the overhead of secondary join conditions that cannot be evaluated using the equijoin keys. | Optional, defaults true.    |
| Join Type           | One of the join types defined in the Join operator.                                                                                                                                                                     | Required                    |

## Exchange Operator

The exchange operator will redistribute data based on an exchange type definition. Applying this operation will lead to an output that presents the desired distribution.

| Signature            | Value                                                        |
| -------------------- | ------------------------------------------------------------ |
| Inputs               | 1                                                            |
| Outputs              | 1                                                            |
| Property Maintenance | Orderedness is maintained. Distribution is overwritten based on configuration. |
| Direct Output Order  | Order of the input.                                          |

### Exchange Types

|Type|Description|
|--|--|
|Scatter|Distribute data using a system defined hashing function that considers one or more fields. For the same type of fields and same ordering of values, the same partition target should be identified for different ExchangeRels|
|Single Bucket|Define an expression that provides a single `i32` bucket number. Optionally define whether the expression will only return values within the valid number of partition counts. If not, the system should modulo the return value to determine a target partition.|
|Multi Bucket|Define an expression that provides a `List<i32>` of bucket numbers. Optionally define whether the expression will only return values within the valid number of partition counts. If not, the system should modulo the return value to determine a target partition. The records should be sent to all bucket numbers provided by the expression.|
|Broadcast|Send all records to all partitions.|
|Round Robin|Send records to each target in sequence. Can follow either exact or approximate behavior. Approximate will attempt to balance the number of records sent to each destination but may not exactly distribute evenly and may send batches of records to each target before moving to the next.|

### Exchange Properties

| Property           | Description                                                  | Required                                                     |
| ------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Input              | The relational input.                                        | Required.                                                    |
| Distribution Type  | One of the distribution types defined above.                 | Required.                                                    |
| Partition Count    | The number of partitions targeted for output.                | Optional. If not defined, implementation system should decide the number of partitions. Note that when not defined, single or multi bucket expressions should not be constrained to count. |
| Expression Mapping | Describes a relationship between each partition ID and the destination that partition should be sent to. | Optional. A partition may be sent to 0..N locations. Value can either be a URI or arbitrary value. |



## Merging Capture

A receiving operation that will merge multiple ordered streams to maintain orderedness.

| Signature            | Value                                        |
| -------------------- | -------------------------------------------- |
| Inputs               | 1                                            |
| Outputs              | 1                                            |
| Property Maintenance | Orderedness and distribution are maintained. |
| Direct Output Order  | Order of the input.                          |

### Merging Capture Properties

| Property | Description                                                  | Required                    |
| -------- | ------------------------------------------------------------ | --------------------------- |
| Blocking | Whether the merging should block incoming data. Blocking should be used carefully, based on whether a deadlock can be produced. | Optional, defaults to false |



## Simple Capture

A receiving operation that will merge multiple streams in an arbitrary order.

| Signature            | Value                                                        |
| -------------------- | ------------------------------------------------------------ |
| Inputs               | 1                                                            |
| Outputs              | 1                                                            |
| Property Maintenance | Orderness is empty after this operation. Distribution are maintained. |
| Direct Output Order  | Order of the input.                                          |

### Naive Capture Properties

| Property | Description           | Required |
| -------- | --------------------- | -------- |
| Input    | The relational input. | Required |



## Top-N Operation

The top-N operator reorders a dataset based on one or more identified sort fields as well as a sorting function. Rather than sort the entire dataset, the top-N will only maintain the total number of records required to ensure a limited output. A top-n is a combination of a logical sort and logical fetch operations.

| Signature            | Value                                                        |
| -------------------- | ------------------------------------------------------------ |
| Inputs               | 1                                                            |
| Outputs              | 1                                                            |
| Property Maintenance | Will update orderedness property to the output of the sort operation. Distribution property only remapped based on emit. |
| Direct Output Order  | The field order of the input.                                |

### Top-N Properties

| Property    | Description                                                  | Required                 |
| ----------- | ------------------------------------------------------------ | ------------------------ |
| Input       | The relational input.                                        | Required                 |
| Sort Fields | List of one or more fields to sort by. Uses the same properties as the [orderedness](basics.md#orderedness) property. | One sort field required  |
| Offset      | A positive integer. Declares the offset for retrieval of records. | Optional, defaults to 0. |
| Count       | A positive integer. Declares the number of records that should be returned. | Required                 |



## Hash Aggregate Operation

The hash aggregate operation maintains a hash table for each grouping set to coalesce equivalent tuples.

| Signature            | Value                                                        |
| -------------------- | ------------------------------------------------------------ |
| Inputs               | 1                                                            |
| Outputs              | 1                                                            |
| Property Maintenance | Maintains distribution if all distribution fields are contained in every grouping set. No orderness guaranteed. |
| Direct Output Order  | Same as defined by [Aggregate](logical_relations.md#aggregate-operation) operation. |

### Hash Aggregate Properties

| Property         | Description                                                  | Required                                |
| ---------------- | ------------------------------------------------------------ | --------------------------------------- |
| Input            | The relational input.                                        | Required                                |
| Grouping Sets    | One or more grouping sets.                                   | Optional, required if no measures.      |
| Per Grouping Set | A list of expression grouping that the aggregation measured should be calculated for. | Optional, defaults to 0.                |
| Measures         | A list of one or more aggregate expressions. Implementations may or may not support aggregate ordering expressions. | Optional, required if no grouping sets. |



## Streaming Aggregate Operation

The streaming aggregate operation leverages data ordered by the grouping expressions to calculate data each grouping set tuple-by-tuple in streaming fashion. All grouping sets and orderings requested on each aggregate must be compatible to allow multiple grouping sets or aggregate orderings.

| Signature            | Value                                                        |
| -------------------- | ------------------------------------------------------------ |
| Inputs               | 1                                                            |
| Outputs              | 1                                                            |
| Property Maintenance | Maintains distribution if all distribution fields are contained in every grouping set. Maintains input ordering. |
| Direct Output Order  | Same as defined by [Aggregate](logical_relations.md#aggregate-operation) operation. |

### Streaming Aggregate Properties

| Property         | Description                                                  | Required                                |
| ---------------- | ------------------------------------------------------------ | --------------------------------------- |
| Input            | The relational input.                                        | Required                                |
| Grouping Sets    | One or more grouping sets. If multiple grouping sets are declared, sets must all be compatible with the input sortedness. | Optional, required if no measures.      |
| Per Grouping Set | A list of expression grouping that the aggregation measured should be calculated for. | Optional, defaults to 0.                |
| Measures         | A list of one or more aggregate expressions. Aggregate expressions ordering requirements must be compatible with expected ordering. | Optional, required if no grouping sets. |

## Consistent Partition Window Operation
A consistent partition window operation is a special type of project operation where every function is a window function and all of the window functions share the same sorting and partitioning. This allows for the sort and partition to be calculated once and shared between the various function evaluations.

| Signature            | Value                                                                |
| -------------------- |----------------------------------------------------------------------|
| Inputs               | 1                                                                    |
| Outputs              | 1                                                                    |
| Property Maintenance | Maintains distribution and ordering.                                 |
| Direct Output Order  | Same as Project operator (input followed by each window expression). |

### Window Properties

| Property           | Description                     | Required               |
| ------------------ | ------------------------------- | ---------------------- |
| Input              | The relational input.           | Required               |
| Window Functions | One or more window functions. | At least one required. |


## Expand Operation

The expand operation creates duplicates of input records based on the Expand Fields. Each Expand Field can be a Switching Field or an expression. Switching Fields are described below.  If an Expand Field is an expression then its value is consistent across all duplicate rows.

| Signature            | Value                                                                                                                                                                          |
| -------------------- |--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs               | 1                                                                                                                                                                              |
| Outputs              | 1                                                                                                                                                                              |
| Property Maintenance | Distribution is maintained if all the distribution fields are consistent fields with direct references. Ordering can only be maintained down to the level of consistent fields that are kept.|
| Direct Output Order  | The expand fields followed by an i32 column describing the index of the duplicate that the row is derived from.                                                                                                                                           |

### Expand Properties

| Property  | Description                          | Required |
| --------- |--------------------------------------| -------- |
| Input     | The relational input.                | Required |
| Direct Fields | Expressions describing the output fields.  These refer to the schema of the input.  Each Direct Field must be an expression or a Switching Field  | Required |

### Switching Field Properties

A switching field is a field whose value is different in each duplicated row.  All switching fields in an Expand Operation must have the same number of duplicates.

| Property  | Description                          | Required |
| --------- |--------------------------------------| -------- |
| Duplicates | List of one or more expressions.  The output will contain a row for each expression. | Required |

## Hashing Window Operation

A window aggregate operation that will build hash tables for each distinct partition expression.

| Signature            | Value                                                        |
| -------------------- | ------------------------------------------------------------ |
| Inputs               | 1                                                            |
| Outputs              | 1                                                            |
| Property Maintenance | Maintains distribution. Eliminates ordering.                 |
| Direct Output Order  | Same as Project operator (input followed by each window expression). |

### Hashing Window Properties

| Property           | Description                     | Required               |
| ------------------ | ------------------------------- | ---------------------- |
| Input              | The relational input.           | Required               |
| Window Expressions | One or more window expressions. | At least one required. |



## Streaming Window Operation

A window aggregate operation that relies on a partition/ordering sorted input.

| Signature            | Value                                                        |
| -------------------- | ------------------------------------------------------------ |
| Inputs               | 1                                                            |
| Outputs              | 1                                                            |
| Property Maintenance | Maintains distribution. Eliminates ordering.                 |
| Direct Output Order  | Same as Project operator (input followed by each window expression). |

### Streaming Window Properties

| Property           | Description                                                  | Required               |
| ------------------ | ------------------------------------------------------------ | ---------------------- |
| Input              | The relational input.                                        | Required               |
| Window Expressions | One or more window expressions. Must be supported by the sortedness of the input. | At least one required. |

